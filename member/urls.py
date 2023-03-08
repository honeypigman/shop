from django.urls import path
from member.views.base import MemberViewSet

member = MemberViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

member_detail = MemberViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', member),
    path('<int:pk>/', member_detail),
]