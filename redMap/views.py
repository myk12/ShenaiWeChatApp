from django.shortcuts import render, redirect
from django.views import View
from .models import RedMapUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import BloodDonor, BloodRecord, BloodPhoto, BloodMessage

# Create your views here.
def index(request):
    return HttpResponse('index')

class ProfileView(View):
    @login_required
    def get(self, request):
        user = request.user
        user_profile = BloodDonor.objects.filter(user=user)
        rspJson = {}
        rspJson['hometown'] = user_profile.hometown
        rspJson['province'] = user_profile.province
        rspJson['city'] = user_profile.city
        rspJson['latitude'] = user_profile.latitude
        rspJson['longitude'] = user_profile.longitude

        return JsonResponse(rspJson)
    
    @login_required
    def post(self, request):
        user = request.user
        rspJson = {}
        post_content = request.POST
        user_profile = BloodDonor.objects.filter(user=user)
        user_profile.hometown = post_content.get('hometown')
        user_profile.province = post_content.get('province')
        user_profile.city = post_content.get('city')
        user_profile.latitude = post_content.get('latitude')
        user_profile.longitude = post_content.get('longitude')

        user_profile.save()
        rspJson['error_code'] = 0
        return JsonResponse(rspJson)

class DonationView(View):
    @login_required
    def get(self, request):
        user = request.user.user
        rspJson = {}
        records = BloodRecord.objects.filter(donor=user)

        record_list = []
        for record in records:
            rcd_json = {}
            rcd_json['datetime'] = record.datetime
            rcd_json['volume'] = record.volume
            record_list.append(rcd_json)

        rspJson['records'] = record_list
        return JsonResponse(rspJson)
    
    @login_required
    def post(self, request):
        user = request.user
        user_post = request.POST
        rspJson = {}

        BloodRecord.objects.create(
            donor = user,
            datetime = user_post.get('datetime'),
            volume = user_post.get('volume')
        )

        rspJson['error_code'] = 0
        return JsonResponse(rspJson)

@login_required
def upload_photo(request):
    if request.method == 'POST':
        photo = request.FILES['photo']
        caption = request.POST.get('caption', '')
        BloodPhoto.objects.create(donor=request.user.donor, photo=photo, caption=caption)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
