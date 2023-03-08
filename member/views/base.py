from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from member.models.base import Member
from member.serializers.MemberSerializer import *


class MemberView(APIView):
    def get(self, request):
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)