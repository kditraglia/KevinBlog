import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('~/.virtualenvs/blogenv/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/kevin/Projects/KevinBlog/KevinBlog')
sys.path.append('/home/kevin/Projects/KevinBlog/KevinBlog/blog')

os.environ['DJANGO_SETTINGS_MODULE'] = 'KevinBlog.settings'

# Activate your virtual env
activate_env="/home/kevin/.virtualenvs/blogenv/bin/activate_this.py"
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
