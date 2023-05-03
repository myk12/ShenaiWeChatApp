from django.urls import path
from . import views

app_name = 'loveRelay'

urlpatterns = [
    path("", views.index, name='index'),
    path('gifts/', views.GiftListView.as_view(), name='gift_list'),
    path('gifts/<int:pk>/', views.GiftDetailView.as_view(), name='gift_detail'),
    path('messages/', views.MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('bottles/', views.BottleListView.as_view(), name='bottle_list'),
    path('bottles/<int:pk>/', views.BottleDetailView.as_view(), name='bottle_detail'),
]