from django.db import models
from group.models import Group
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    group = models.ForeignKey(Group,related_name='posts',on_delete=models.CASCADE)
    img = models.ImageField(upload_to="photo/%Y/%m/%d/",blank=True)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('group:single',kwargs={'slug':self.group.slug})

    class Meta:
        ordering = ['-created_at']
        # unique_together = ['user','message']