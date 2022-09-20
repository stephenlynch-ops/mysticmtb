from . import views
from django.urls import path


urlpatterns = [
    path('', views.open_home_page, name='open_home_page'),
    path('trails/', views.PostList.as_view(), name='PostList'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
