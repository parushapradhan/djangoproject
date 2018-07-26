from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class image(models.Model):
    imagery=models.ImageField(help_text="upload image")
    message=models.TextField(help_text="description of art")
    votes = models.IntegerField(default=0, help_text="Enter Vote Count")
    published_date = models.DateTimeField(blank=True, null=True)
    #def well(self):
     #   return self.imagery
    '''def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
'''
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Contact(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    emailAddress = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject