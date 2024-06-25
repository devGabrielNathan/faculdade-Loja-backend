from .models import User

class UserDAO:
    @staticmethod
    def get_user_by_email(email):
        return User.objects.filter(email=email).first()


    @staticmethod
    def get_user_by_uuid(user_uuid):
        return User.objects.filter(user_uuid=user_uuid).first()


    @staticmethod
    def save_user(serializer):
        return serializer.save()
