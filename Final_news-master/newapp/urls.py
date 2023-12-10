from django.contrib import admin
from django.urls import path
from .views import Article, ArticleId, PostCreate, PostUpdate, PostDelete, subscriptions

urlpatterns = [
    path('', Article.as_view()),
    path('news<int:pk>/', ArticleId.as_view()),
    path('create/', PostCreate.as_view()),
    path('<int:pk>/update/', PostUpdate.as_view()),
    path('<int:pk>/delete/', PostDelete.as_view()),
    path('subscriptions/', subscriptions, name='subscriptions'),
]