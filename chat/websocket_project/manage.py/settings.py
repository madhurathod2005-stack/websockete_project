INSTALLED_APPS = [
    'channels',
    'chat',
]

ASGI_APPLICATION = "websocket_project.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'channels',
    'chat',
]
ASGI_APPLICATION = 'config.asgi.application'
ASGI_APPLICATION = 'chatproject.asgi.application'