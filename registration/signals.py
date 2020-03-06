from django.dispatch import receiver
from .models import Profile
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender,instance, created, **kwargs):
    if created:
        profile=Profile.objects.create(user=instance)
        profile.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

