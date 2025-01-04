from django.contrib import admin
from .models import Article, Comments, Article_category, YoutubeVideos, Message

# Register your models here.
admin.site.register(Article)
admin.site.register(Comments)
admin.site.register(Article_category)
admin.site.register(YoutubeVideos)
admin.site.register(Message)