from rest_framework import serializers
from member.const import MemberActiveCode
from member.models.base import Member


class MemberSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)
    active_code = serializers.ChoiceField(choices=MemberActiveCode, default=MemberActiveCode.ACTIVE)
    create_date = serializers.DateTimeField()

    class Meta:
        model = Member
        fields = ['id', 'password', 'active_code', 'create_date']
