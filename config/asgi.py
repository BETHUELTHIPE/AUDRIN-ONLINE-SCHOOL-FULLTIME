import os
import django

from channels.routing import ProtocolTypeRouter
from channels.routing import AsgiHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": AsgiHandler(),
        # Just HTTP for now. (We can add other protocols later.)
    }
)
