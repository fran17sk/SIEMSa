from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve

EXEMPT_URLS = [  # Agrega aquí tus rutas públicas
    '/login/',
    '/logout/',
    '/admin/',
    
]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in EXEMPT_URLS:
            return redirect(settings.LOGIN_URL)
        return self.get_response(request)
