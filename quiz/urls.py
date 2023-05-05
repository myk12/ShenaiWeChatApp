from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    # 知识问答接口
    path('question/', views.QuizView.as_view(), name='quiz'),
    # 排行榜接口
    path('rank/', views.RankView.as_view(), name='rank'),
    # 个人中心接口
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
