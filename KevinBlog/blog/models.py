from django.db import models
from django.db.models import permalink

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')
    tag = models.ForeignKey('blog.Tag')

    @property
    def numComments(self):
        return Comment.objects.filter(post=self).count()

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_tag', None, { 'slug': self.slug })

class Comment(models.Model):
    user = models.CharField(max_length=50)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    post = models.ForeignKey('blog.Blog')

    def __unicode__(self):
        return '%s' % self.user
