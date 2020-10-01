from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self, *a, **k):
        super().save(*a, **k)
        img = Image.open(self.profile_image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.profile_image.path)

    def __str__(self):
        return f'{self.user.username} Profile'