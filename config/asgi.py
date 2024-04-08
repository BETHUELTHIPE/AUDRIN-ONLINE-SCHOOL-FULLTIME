import os
import django
from channels.routing import ProtocolTypeRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DJANGO-LMS.config.settings")
django.setup()

application = ProtocolTypeRouter({})