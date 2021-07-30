from django.shortcuts import render
import os


def get_content(pathname: str) -> str:
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, pathname)
    f = open(file_path, "r")
    content = f.read()
    f.close()
    return content


# Create your views here.
def index(request):
    return render(request, 'cv/index.html', {'text_body': get_content('media/ru/index.md')})


def about(request):
    return render(request, 'cv/index.html', {'text_body': get_content('media/ru/about.md')})


def developer(request):
    return render(request, 'cv/index.html', {'text_body': get_content('media/ru/developer.md')})


def engineer(request):
    return render(request, 'cv/index.html', {'text_body': get_content('media/ru/engineer.md')})


def portfolio(request):
    return render(request, 'cv/index.html', {'text_body': get_content('media/ru/portfolio.md')})
