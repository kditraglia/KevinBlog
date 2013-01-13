
from blog.models import Blog, Category, Comment
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'allposts': Blog.objects.all().order_by('-posted')[:5]
    }, context_instance=RequestContext(request))

def view_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        comment = Comment(
           user=request.POST['username'],
           body=request.POST['comment'],
           post=post)
        comment.save()

    return render_to_response('view_post.html', {
		'categories': Category.objects.all(),
                'post': post,
		'allposts': Blog.objects.all()[:5],
		'comments': Comment.objects.filter(post=post),
    }, context_instance=RequestContext(request))

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'categories': Category.objects.all(),
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5],
        'allposts': Blog.objects.all()[:5]
    }, context_instance=RequestContext(request))
