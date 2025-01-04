from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
User = get_user_model()

# Create your models here.

class Article_category(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    imgUrl = CloudinaryField('image', blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Article_category, on_delete=models.CASCADE, null=True, blank=True)
    pdfID = models.CharField(max_length=500, null=True, blank=True)
    pdfUrlView = models.CharField(max_length=1500, null=True, blank=True)
    pdfUrlDownload = models.CharField(max_length=1500, null=True, blank=True)
    magazin = models.CharField(max_length=1500, null=True, blank=True)
    resume = models.TextField(max_length=5000, null=True, blank=True)
    puplished_day = models.DateField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_author")
    created_at = models.DateTimeField(auto_now=True)
    readCount = models.IntegerField(null=False, blank=False, default=0)
    downloadCount = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return f'{self.title} by {self.author.username}'
    
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_authors")
    content = models.TextField(null=False, blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.author} commented on post {self.article.title}'

class YoutubeVideos(models.Model):
    vidLink = models.CharField(max_length=1000, null=False, blank=False)
    title = models.CharField(max_length=1500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Message(models.Model):
    author = models.CharField(max_length=300, null=False, blank=False)
    email_or_phone = models.CharField(max_length=300, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    sentTo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages', null=True, blank=True)
    seen = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.author}'
