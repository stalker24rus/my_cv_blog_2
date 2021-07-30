from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from blog.sitemaps import PostSitemap
from cv import views as site_views
from django.views.generic import RedirectView


sitemaps = {
    'posts': PostSitemap
}


urlpatterns = [
    path('', site_views.index, name='index'),
    path('about/', site_views.about, name='about'),
    path('developer/', site_views.developer, name='developer'),
    path('engineer/', site_views.engineer, name='engineer'),
    path('portfolio/', site_views.portfolio, name='portfolio'),
    path('', include('cv.urls',  namespace='cv')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
