from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
import jwt
from datetime import datetime
from datetime import timezone
from datetime import timedelta
from .repositories import UserDAO

class UserController:
    # Registro e autenticação automática
    @api_view(['POST'])
    def register_controller(request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserDAO.save_user(serializer)

        # Geração do token JWT após o registro
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
            'jwt': token,
            'user': serializer.data
        }

        return response


    # Login e autenticação automática
    @api_view(['POST'])
    def login_controller(request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            raise AuthenticationFailed('Email and password are required!')

        user = UserDAO.get_user_by_email(email)

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        # Geração do token JWT ao fazer login
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
    

    # Perfil do usuário
    @api_view(['GET'])
    def user_profile_controller(request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated - token expired')
        
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Unauthenticated - invalid token')
        
        user = UserDAO.get_user_by_uuid(payload["user_uuid"])
        serializer = UserSerializer(user)
        return Response(serializer.data)


    # Logout
    @api_view(['POST'])
    def logout_controller(request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response
