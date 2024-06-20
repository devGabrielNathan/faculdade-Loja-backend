from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
import jwt
from datetime import datetime
from datetime import timedelta
from datetime import timezone


class UserController:
    # Registro
    @api_view(['POST'])
    def register(request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


    # Login
    @api_view(['POST'])
    def login(request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        expiry_time = datetime.now(timezone.utc) + timedelta(minutes=60)
        
        payload = {
            'user_uuid': str(user.user_uuid),
            'exp': expiry_time,
            'iat': datetime.now(timezone.utc),
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        
        response.data = {
            'jwt': token
        }

        return response
    
    
    # Autenticacao
    @api_view(['GET'])
    def user(request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except:
            raise AuthenticationFailed('Unauthenticated')
        
        # user = User.objects.get(payload["user_uuid"])
        user = User.objects.filter(user_uuid=payload["user_uuid"]).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
        # return Response(token)


    # Logout
    @api_view(['POST'])
    def logout(request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response
