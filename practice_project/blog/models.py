from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class BlogPost(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.title}-{self.author}"
