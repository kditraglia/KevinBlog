from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'KevinBlog.blog.views.index'),
    url(
        r'^blog/view/(?P<slug>[^\.]+).html',
        'KevinBlog.blog.views.view_post',
        name='view_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+).html',
        'KevinBlog.blog.views.view_category',
        name='view_blog_category'),
)
