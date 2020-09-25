from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        # CustomUsersにならないようにするやつ
        verbose_name_plural = 'CustomUser'
