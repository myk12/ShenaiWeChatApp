from django.urls import path
from . import views

app_name = 'redMap'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('donation', views.DonationView.as_view(), name='donation'),
    path('upload_photo', views.upload_photo, name='upload_photo'),
]
