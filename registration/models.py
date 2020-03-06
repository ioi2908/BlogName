from django.db import models
from django.contrib.auth.models import User

# User = get_user_model()


class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.user.username


