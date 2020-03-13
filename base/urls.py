from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('', include('django.contrib.auth.urls'), name='user'),
    path('home', views.homeView, name='home'),
    path('confirm', views.confirmView, name='confirm'),
    path('success', views.successView, name='success'),
    # path('<uuid:topic_id>/topic', views.topicView, name='topic'),
    # path('<uuid:topic_id>/delete_topic', views.deleteTopicView, name='delete_topic'),
    # path('create_topic', views.createTopicView, name='create_topic'),
    # path('news_details/<str:article_id>', views.newsDetailsView, name='news_details'),
    # path('article_trend_data/<uuid:topic_id>', views.articleTrendData, name='article_trend_data'),
    # path('article_trend_data', views.articleTrendData, name='article_trend_data'),
]