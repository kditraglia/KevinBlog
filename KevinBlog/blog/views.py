import akismet
from blog.models import Blog, Category, Comment
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext

my_api_key = '65c78bc3166d'

def index(request):
    return render_to_response('index.html', {
        'comments' : Comment.objects.all()[:5],
        'categories': Category.objects.all(),
        'allposts': Blog.objects.all().order_by('-posted')[:5]
    }, context_instance=RequestContext(request))

def write_blog(request):
    return render_to_response('write_blog.html', {
    }, context_instance=RequestContext(request))

def view_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        is_spam = akismet.comment_check(my_api_key,"http://ditraglia.net",
          get_client_ip(request), request.META.get('HTTP_USER_AGENT'),
          comment_content=request.POST['comment'])
        if not is_spam:
          comment = Comment(
             user=request.POST['username'],
             body=request.POST['comment'],
             post=post)
          comment.save()
        else:
          return HttpResponse("PLEASE STOP SPAMMING ME")

    return render_to_response('view_post.html', {
		    'categories': Category.objects.all(),
        'post': post,
		    'allposts': Blog.objects.all()[:5],
		    'comments': Comment.objects.filter(post=post),
    }, context_instance=RequestContext(request))

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'categories': Category.objects.all(),
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5],
        'allposts': Blog.objects.all()[:5]
    }, context_instance=RequestContext(request))