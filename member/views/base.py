from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from member.models.base import Member
from member.serializers.member import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects
    serializer_class = MemberSerializer

    def list(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        queryset = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

