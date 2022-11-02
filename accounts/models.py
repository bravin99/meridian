from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

def avatar_path(instance, filename):
    return f"avatars/{instance}/{filename}"

class User(AbstractUser):
    avatar = models.ImageField(upload_to=avatar_path)

    def __str__(self):
        return f"{self.username}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    country = models.CharField(max_length=100, blank=True, default="Kenya")

    def __str__(self):
        return f"{self.user.username}'s profile"


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()