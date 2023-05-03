from django.urls import path
from . import views

app_name = 'redMap'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('add_record', views.add_record, name='add_record'),
    path('upload_photo', views.upload_photo, name='upload_photo'),
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('index/', views.index)
]
