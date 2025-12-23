from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api import ArticleViewSet  # ← если создали api.py

router = DefaultRouter()
router.register(r'api/articles', ArticleViewSet)

urlpatterns = [
    path('articles', views.article_list, name='article_list'),
    path('articles/create', views.article_create, name='article_create'),
    path('articles/<int:id>/edit', views.article_edit, name='article_edit'),
    path('articles/<int:id>/delete', views.article_delete, name='article_delete'),
    path('', include(router.urls)),  # ← добавляет API маршруты
]