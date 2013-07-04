from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'blog.views.index'),
    (r'^admin/', include(admin.site.urls)),
    (r'^write_blog/', 'blog.views.write_blog'),
    (r'^upload_view/', 'blog.views.upload_view'),
    (r'^show_pics/', 'blog.views.show_pics'),
    url(
        r'^blog/view/(?P<slug>[^\.]+)',
        'blog.views.view_post',
        name='view_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+)',
        'blog.views.view_category',
        name='view_blog_category'),
)

