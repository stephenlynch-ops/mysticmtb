from django.urls import path
from . import views


urlpatterns = [
    path('', views.OpenHomePage, name='open_home_page'),
    path('cafe/', views.open_cafe_page, name='open_cafe_page'),
    path('gallery/', views.open_gallery_page, name='open_gallery_page'),
    path('trails/', views.PostList.as_view(), name='PostList'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
