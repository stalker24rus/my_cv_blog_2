from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm, SearchForm, PostForm, LoginForm, \
        ImageForm
from .services.add_post import add_user_post
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request, tag_slug=None):
    # posts = Post.published.all()
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)  # posts in each page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts,
                   'tag': tag})


def post_detail(request, year, month, day, author, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             # author=author,
                             )

    # List of active comment for this post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        #  A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_posts': similar_posts
                   })


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)

        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recomends you read " \
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'razorstent@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
            search_query = SearchQuery(query)

            results = Post.published.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gt=0.1).order_by('-similarity')

    return render(request,
                  'blog/post/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})


@login_required
def post_add(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            add_user_post(form, request.user)
            return HttpResponseRedirect('/blog') 
        else:
            messages.error(request, 'Форма заполнена с ошибками')
            return render(request,
                          'blog/post/add.html',
                          {'form': form})
    else:
        return render(request, 
                      'blog/post/add.html',
                      {'form': form})


@login_required
def post_change(request, post_id):
    """Change data of Post in database"""
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)
    
    print('Request method is: ', request.method)

    if request.method == 'POST':
        if post.author.id == request.user.id:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Публикация обновлена успешно.')
                return render(request,
                             'blog/post/change.html',
                             {'form': form})
            else:
                messages.error(request, 'Форма заполнена с ошибками')
                return render(request,
                             'blog/post/change.html',
                             {'form': form})
        else:
            msg_text = 'Вам запрещено изменять эту публикацию.'\
                       'Вы не являетесь владельцем этой публикации.'
            messages.error(request,msg_text)

            return render(request, 
                         'blog/post/change.html',
                         {'form': form})

    else:
        return render(request, 
                      'blog/post/change.html',
                      {'form': form})


@login_required
def post_delete(request, post_id):
    """Delete post by id. Check owner """
    post = Post.objects.get(id=post_id)
    # Check user id: delete the post can only author that a post
    if post.author.id == request.user.id:
        post.delete()
    return HttpResponseRedirect('/blog')


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 
                          'blog/images/upload.html', 
                          {'form': form, 
                           'img_obj': img_obj
                          }
                         )
    else:
        form = ImageForm()
        return render(request,
                      'blog/images/upload.html',
                      {'form': form}
                     )
