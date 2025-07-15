# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/', LoginView.as_view()),
    path('api/', include('users.urls')),
    path('api/', include('movies.urls')), # Esto activa todas las rutas de la app movies
]