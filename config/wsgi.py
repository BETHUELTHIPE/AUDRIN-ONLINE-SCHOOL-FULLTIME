

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
#os.environ["DJANGO_SETTINGS_MODULE"] = "DJANGO-LMS.settings" 
application = get_wsgi_application()
