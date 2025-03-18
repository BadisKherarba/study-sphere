"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
import chatbot.routing
from chat.middleware import JwtAuthMiddleware

# Combine the URL patterns from both apps:
combined_websocket_urlpatterns = chat.routing.websocket_urlpatterns + chatbot.routing.websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JwtAuthMiddleware(  # our JWT middleware wraps the connection
         AuthMiddlewareStack(
             URLRouter(combined_websocket_urlpatterns)
         )
    ),
})
