from django.db import models
from django.contrib.auth.models import User

class PohMengPost(models.Model):
    content = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
      
# Create your models here.
