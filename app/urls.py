from django.urls import path
from .views import (HomePageView, AboutPageView, BlogListView
, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView,)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk', BlogListView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/delete', BlogCreateView.as_view(), name='blog_delete'),
