from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'