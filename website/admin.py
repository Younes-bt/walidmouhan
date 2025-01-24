from django.contrib import admin
from .models import Article, Comments, Article_category, YoutubeVideos, Message, Profession, Profile, Book, Book_genre, Book_operation, books_operation_situations, Response_to_Book_requests, City, University

# Register your models here.
admin.site.register(Article)
admin.site.register(Comments)
admin.site.register(Article_category)
admin.site.register(YoutubeVideos)
admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Profession)
admin.site.register(Book)
admin.site.register(Book_genre)
admin.site.register(Book_operation)
admin.site.register(books_operation_situations)
admin.site.register(Response_to_Book_requests)
admin.site.register(City)
admin.site.register(University)