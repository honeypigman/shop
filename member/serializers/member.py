from rest_framework import serializers
from rest_framework import status
from rest_framework.exceptions import ValidationError
from member.const import MemberActiveCode
from member.models.base import Member


class MemberSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    active_code = serializers.ChoiceField(choices=MemberActiveCode, default=MemberActiveCode.ACTIVE)
    create_date = serializers.DateTimeField()

    def validate(self, data):
        if Member.objects.filter(id=data.get('id')):
            raise ValidationError(detail='회원ID중복', code=status.HTTP_400_BAD_REQUEST)
        return data

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    class Meta:
        model = Member
        fields = ['id', 'password', 'active_code', 'create_date']
