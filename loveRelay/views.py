from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Gift, Message, Bottle

# Create your views here.

def index(request):
    return HttpResponse("love relay")

class GiftView(View):
    def get(self, request):
        gifts = Gift.objects.all()
        data = [{
            'name': gift.name,
            'remain_num': gift.remain_num,
            'price': gift.price,
            'image': gift.image,
            'description': gift.description,
        } for gift in gifts]
        return JsonResponse({'gifts': data})

    def post(self, request):
        name = request.POST.get('name')
        remain_num = request.POST.get('remain_num')
        price = request.POST.get('price')
        image = request.POST.get('image')
        description = request.POST.get('description')
        gift = Gift.objects.create(name=name, remain_num=remain_num, price=price, image=image, description=description)
        return JsonResponse({'gift_id': gift.id})

class MessageView(View):
    def get(self, request):
        sender = request.user
        receiver = request.GET.get('receiver')
        messages = Message.objects.filter(sender=sender, receiver=receiver)
        data = [{
            'content': message.content,
            'sender': message.sender,
            'receiver': message.receiver,
        } for message in messages]
        return JsonResponse({'messages': data})

    def post(self, request):
        content = request.POST.get('content')
        sender = request.user
        receiver = request.POST.get('receiver')
        message = Message.objects.create(content=content, sender=sender, receiver=receiver)
        return JsonResponse({'message_id': message.id})


class BottleView(View):
    def get(self, request):
        sender = request.user
        receiver = request.GET.get('receiver')
        bottles = Bottle.objects.filter(sender=sender, receiver=receiver)
        data = [{
            'message': bottle.message,
            'gift': bottle.gift,
            'is_random': bottle.is_random,
            'is_sent': bottle.is_sent,
            'sender': bottle.sender,
            'receiver': bottle.receiver,
        } for bottle in bottles]
        return JsonResponse({'bottles': data})

    def post(self, request):
        message_id = request.POST.get('message_id')
        gift_id = request.POST.get('gift_id')
        is_random = request.POST.get('is_random')
        sender = request.user
        receiver = request.POST.get('receiver')
        bottle = Bottle.objects.create(message_id=message_id, gift_id=gift_id, is_random=is_random, sender=sender, receiver=receiver)
        return JsonResponse({'bottle_id': bottle.id})

