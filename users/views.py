# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'Usuario creado con éxito'}, status=status.HTTP_201_CREATED)
    
# O si es una vista personalizada:
class LoginView(APIView):
    def get(self, request):
        # Tu lógica aquí
        return render(request, 'login.html')