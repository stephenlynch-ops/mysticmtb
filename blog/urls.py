from . import views
from django.urls import path


urlpatterns = [
    path('', views.open_home_page, name='open_home_page'),
    path('trails/', views.PostList.as_view(), name='trails_list'),
]
