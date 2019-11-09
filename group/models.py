from django import template
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from django.db import models

# Create your models here.

register = template.Library()
User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    member = models.ManyToManyField(User,through="GroupMember")

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('group:all')

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='membership',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='group_users',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    class Meta:
        unique_together = ['group', 'user']