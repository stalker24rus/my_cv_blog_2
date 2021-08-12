

def add_user_post(form, user):
    """Logic for additional user post to DB"""
    try:
        new_post = form.save(commit=False)
        new_post.author = user
        new_post.save()
        return None
    except Exception as e:
        print(e)
        return -1
