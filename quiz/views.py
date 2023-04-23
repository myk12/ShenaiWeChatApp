from django.shortcuts import render
from django.http import JsonResponse
from .models import Question, UserInfo

# Create your views here.

def index(request):
    user, created = UserInfo.objects.get_or_create(name=request.user.username)
    questions = Question.objects.order_by('?')[:5]
    context = {'questions': questions, 'user': user}
    return render(request, 'quiz/index.html', context)

def answer(request):
    question_id = request.POST.get('question_id')
    selected_option = request.POST.get('option')
    question = Question.objects.get(id=question_id)
    if int(selected_option) == question.answer:
        user, created = UserInfo.objects.get_or_create(name=request.user.username)
        user.energy += 20
        user.save()
        result = {'result': 'correct', 'energy': user.energy}
    else:
        result = {'result': 'incorrect'}
    return JsonResponse(result)

def getQuiz(request):
    user, created = UserInfo.objects.get_or_create(name=request.user.username)
    questions = Question.objects.order_by('?')[:5]
    context = {'questions': "q1", 'user': 'u1'}

    return JsonResponse(context)