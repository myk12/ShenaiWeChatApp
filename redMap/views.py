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

@login_required
def map(request):
    donors = BloodDonor.objects.all()
    return render(request, 'map.html', {'donors': donors})

@login_required
def profile(request):
    return HttpResponse("Test login success")
    #donor = request.user.donor
    #records = donor.records.all()
    #photos = donor.photos.all()
    #messages = donor.messages.all()
    #return render(request, 'profile.html', {'donor': donor, 'records': records, 'photos': photos, 'messages': messages})

#@login_required
def add_record(request):
    if request.method == 'POST':
        volume = request.POST['volume']
        BloodRecord.objects.create(donor=request.user.donor, volume=volume)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

#@login_required
def upload_photo(request):
    if request.method == 'POST':
        photo = request.FILES['photo']
        caption = request.POST.get('caption', '')
        BloodPhoto.objects.create(donor=request.user.donor, photo=photo, caption=caption)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

class RegisterView(View):
    def get(self, request):
        return render(request, "redMap/register.html")
    
    def post(self, request):
        rname = request.POST.get("rname")
        rpasswd = request.POST.get("rpasswd")
        email = request.POST.get("email")

        # if successfully registered, redirect to login page
        users = RedMapUser.objects.all()
        
        res_user = RedMapUser.objects.filter(username=rname).count()

        if res_user != 0:
            HttpResponse("user exists.")
        
        
        try:
            user = RedMapUser.objects.create_user(username=rname, password=rpasswd, email=email)
            print('>>>', user)
        except Exception as e:
            print(e)
            return HttpResponse("Failed to register.")
        
        return redirect('login/')

class LoginView(View):
    def get(self, request):
        return render(request, "redMap/login.html")
    
    def post(self, request):
        lname = request.POST.get("lname")
        lpasswd = request.POST.get("lpasswd")
        print(lname, lpasswd)

        user = authenticate(request, username=lname, password=lpasswd)
        print(user)

        if user is not None:
            login(request, user)

            return HttpResponse("login success!")
        
        else:

            return HttpResponse("login failed.")
        