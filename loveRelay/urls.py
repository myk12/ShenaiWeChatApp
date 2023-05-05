from django.urls import path
from . import views

app_name = 'loveRelay'

urlpatterns = [
    path("", views.index, name='index'),
    path('gifts/', views.GiftView.as_view(), name='gifts'),
    path('messages/', views.MessageView.as_view(), name='message_list'),
    path('bottles/', views.BottleView.as_view(), name='bottle_list'),
]