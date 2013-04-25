import os, sys
sys.path.append('/home/kevin/Projects/KevinBlog/KevinBlog')
os.environ['DJANGO_SETTINGS_MODULE'] = 'KevinBlog.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
