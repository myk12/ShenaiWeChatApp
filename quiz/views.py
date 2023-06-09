from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Question, Record, Profile
from datetime import datetime

# Create your views here.

class QuizView(View):
    @method_decorator(login_required)
    def get(self, request):
        # 获取10个随机问题
        questions = list(Question.objects.order_by('?')[:10])
        context = {"remaining_chance":10, "questions": questions}
        return render(request, 'quiz.html', context)

    @method_decorator(login_required)
    def post(self, request):
        post_conent = request.POST
        print(post_conent)
        score = post_conent.get('score')

        # 计算得分
        blood_bags = 0
        if 0 <= score and score < 10:
            blood_bags = score*5
        elif score == 10:
            blood_bags = score*5 + 10
        else:
            blood_bags = 0
        
        print(score)

        # 更新个人记录和个人信息
        record = Record(user=request.user, score=score, date=datetime.now())
        record.save()

        profile = Profile.objects.get(user=request.user)
        if not profile:
            profile = Profile(user=request.user, blood_bags=score, last_quiz_date=datetime.now())
        else:
            profile.blood_bags += score
            profile.last_quiz_date = datetime.now()
        profile.save()
        # 返回得分和已获得电子小血包
        return JsonResponse({'error_code': 0})

class RankView(View):
    @method_decorator(login_required)
    def get(self, request):
        # 获取所有用户信息，并按照总得分降序排序
        profiles = Profile.objects.order_by('-total_score')
        data = [{
            'username': profile.user.username,
            'total_score': profile.total_score,
            'rank': i + 1,
        } for i, profile in enumerate(profiles)]
        return JsonResponse({'rankings': data})

class ProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        # 获取个人信息和历史记录
        profile = Profile.objects.get(user=request.user)
        records = Record.objects.filter(user=request.user).order_by('-created_at')[:10]
        data = {
            'username': request.user.username,
            'total_score': profile.total_score,
            'history': [{
                'created_at': record.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'score': record.score,
            } for record in records]
        }
        return JsonResponse({'profile': data})