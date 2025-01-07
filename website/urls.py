from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:id>/', views.articles_view2, name='articles'),
    path('create-article/', views.create_article, name='create_article'),
    path('create-video/', views.create_video, name='create_video'),
    path('allArticles/', views.allArticles, name='all_articles'),
    path('allvideos/', views.allVideos, name='all_videos'),
    path('sendMessage/', views.send_message, name='send_message'),
    path('cv/', views.cv, name='cv'),
    path('admin/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('messages/', views.messages_view, name='messages'),
    path('message/<int:id>/', views.message_view, name='message'),
]