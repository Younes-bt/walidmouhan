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
        return f'{self.author} at {self.created_at}'


class Book_genre(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.title
    
class City(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.title
class Profession(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.title
class University(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.title
class Response_to_Book_requests(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.title
class books_operation_situations(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=300, null=False, blank=False)
    pub_year = models.IntegerField(null=True, blank=False)
    pict = CloudinaryField('image', blank=True, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    genres = models.ManyToManyField(Book_genre, related_name='books')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_added', null=False)


    def __str__(self):
        return f'{self.title} by {self.author}, added by : {self.owner.username}'


class Profile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    pict = CloudinaryField('image', blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    books_added = models.ManyToManyField(Book, related_name='added_by', null=True, blank=True)
    books_borrwed = models.ManyToManyField(Book, related_name='borrwed_by', null=True, blank=True)
    books_actually_borrwed = models.ManyToManyField(Book, related_name='borrwed_now', null=True, blank=True)
    rating = models.IntegerField(blank=False, null=False, default=5)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.full_name
    

class Book_operation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='operation')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_in_operation')
    borrwer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_in_borrowing_operation')
    response = models.ForeignKey(Response_to_Book_requests, on_delete=models.CASCADE)
    situation = models.ForeignKey(books_operation_situations, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.title} is {self.situation.title}'
