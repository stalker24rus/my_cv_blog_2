import logging
from core.views import exception_catcher
from django.http import HttpResponse
from django.shortcuts import render
import os


logger = logging.getLogger(__name__)
MSG_500 = "Возникла ошибка сервера. Мы извещены об этом и как можно быстрее \
        приступим к ее устранению."
ERR_500 = HttpResponse(MSG_500)


def get_content(pathname: str) -> str:
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, pathname)
    f = open(file_path, "r")
    content = f.read()
    f.close()
    return content


# Create your views here.
@exception_catcher(logger, ERR_500)
def index(request):
    return render(request, 'cv/index.html', {'text_body': get_content('media/ru/index.md')})


@exception_catcher(logger, ERR_500)
def about(request):
    return render(request, 'cv/index.html', {'text_body': get_content('media/ru/about.md')})


@exception_catcher(logger, ERR_500)
def developer(request):
    return render(request, 'cv/index.html', {'text_body': get_content('media/ru/developer.md')})


@exception_catcher(logger, ERR_500)
def engineer(request):
    return render(request, 'cv/index.html', {'text_body': get_content('media/ru/engineer.md')})


@exception_catcher(logger, ERR_500)
def portfolio(request):
    return render(request, 'cv/index.html', {'text_body': get_content('media/ru/portfolio.md')})
