from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.feed, name='createpost'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('newpost', views.create_post, name='create_post'),
]