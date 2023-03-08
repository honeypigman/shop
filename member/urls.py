from django.urls import path
from member.views.base import MemberView

urlpatterns = [
    path('', MemberView.as_view()),
]