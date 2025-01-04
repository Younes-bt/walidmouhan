from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, YoutubeVideos, Message, User
import markdown2
from .forms import ArticleForm, YtbVids
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.


def index(request):
    articles = Article.objects.all().order_by('-created_at')
    artiles1 = articles[:3]
    artiles2 = articles[3:6]
    articles6 = articles[:6]

    videos = YoutubeVideos.objects.all().order_by('-created_at')
    videos1 = videos[:3]
    videos2 = videos[3:6]
    videos6 = videos[:6]
    return render(request, 'website/index.html', {
        'articles1':artiles1,
        'articles2':artiles2,
        'articles6': articles6,
        'videos1': videos1,
        'videos2': videos2,
        'videos6':videos6

    })

# def articles_view(request, id):
#     try:
#         article = Article.objects.get(id=id)
#         pdfID = article.pdfID
#         pdfID = pdfID.split('/')[5]
#         article.readCount += 1
#         article.save()
#         html_content = markdown2.markdown(article.content)
#         return render(request, 'website/articles.html', {
#             'article' : article,
#             'content' : html_content,
#             'pdfid' : pdfID,
#         })
#     except Exception as e:
#         message = 'هذا الرابط غير موجود'
#         return render(request, 'website/error.html', {
#             'message': message,
#             'error': str(e), 
#         })

def articles_view2(request,id):
    article = Article.objects.get(pk=id)
    if article :
        pdfID = article.pdfID
        pdfID = pdfID.split('/')[5]
        article.readCount += 1
        article.save()
        html_content = markdown2.markdown(article.content)
        return render(request, 'website/articles.html', {
            'article' : article,
            'content' : html_content,
            'pdfid' : pdfID,
        })
    else :
        message = 'هذا الرابط غير موجود'
        return render(request, 'website/error.html', {
            'message': message,
        })


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST , request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Set the logged-in user as the author
            article.save()
            messages.success(request, 'Article created successfully!')
            return redirect('index')  # Replace 'articles' with your desired URL name
    else:
        form = ArticleForm()

    return render(request, 'website/create_article.html', {'form': form})


@login_required
def create_video(request):
    if request.method == 'POST':
        form = YtbVids(request.POST)
        if form.is_valid():
            youtubeVideo = form.save(commit=False)
            youtubeVideo.save()
            messages.success(request, 'Article created successfully!')
            return redirect('index')  # Replace 'articles' with your desired URL name
    else:
        form = YtbVids()

    return render(request, 'website/create_video.html', {'form': form})


def allArticles(request):
    if request.method == 'POST':
        searchFor = request.POST.get('search-For', '')
        allArticles = Article.objects.all()
        articles = []
        for article in allArticles :
            if searchFor in article.title:
                articles.append(article)
        
        return render(request, 'website/allArticles.html', {
        'articles':articles,
        })

    articles = Article.objects.all().order_by('-created_at')
    most_read = Article.objects.all().order_by('-readCount')[0:5]
    return render(request, 'website/allArticles.html', {
        'articles':articles,
        'most_read_artcles':most_read,
    })

def allVideos(request):
    if request.method == 'POST':
        searchFor = request.POST.get('search-For', '')
        allVideos = YoutubeVideos.objects.all().order_by('created_at')
        videos = []
        for video in allVideos :
            if searchFor in video.title:
                videos.append(video)
        
        return render(request, 'website/allvideos.html', {
        'videos':videos,
        })

    videos = YoutubeVideos.objects.all().order_by('-created_at')
    most_read = Article.objects.all().order_by('-readCount')[0:5]
    return render(request, 'website/allvideos.html', {
        'videos':videos,
        'most_read_artcles':most_read,
    })

def send_message(request):
    if request.method == 'POST':
        author = request.POST.get('name', '').strip()
        email_or_phone = request.POST.get('email_or_phone', '').strip()
        content = request.POST.get('message', '').strip()

        if not author or not email_or_phone or not content:
            return HttpResponse("All fields are required.", status=400)

        # Save the message to the database
        message = Message.objects.create(
            author=author,
            email_or_phone=email_or_phone,
            content=content,
            sentTo= User.objects.get(username='Walid_Mouhan')
        )
        return redirect('index')
    # If GET request, render a template or show an error
    return HttpResponse("Invalid request method.", status=405)

def cv(request):
    return render(request, 'website/cv.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=email, password=password)

        
        if user is not None:
            auth_login(request, user)
            return redirect('index')

        else :
            return render(request, 'website/login.html', {
                'message' : 'كلمة المرور أو الإيميل خطأ، تحقق من معلومات الدخول'
            })
    return render(request, 'website/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def messages_view(request):
    messages_list = Message.objects.all()
    messages_list_not_seen = Message.objects.filter(sentTo=request.user, seen=False)
    messages_list_seen = Message.objects.filter(sentTo=request.user, seen=True)

    return render(request, 'website/messages.html', {
        'messages':messages_list,
        'messagesnotseen':messages_list_not_seen,
        'messagesnotseenCount':messages_list_not_seen.count,
        'messagesseen':messages_list_seen,
        'messagesseenCount':messages_list_seen.count,
    })

def message_view(request, id):
    message = Message.objects.get(pk=id)
    message.seen = True
    message.save()

    return render(request, 'website/message.html', {
        'message':message
    })