from django.db import models
from member.const import MemberActiveCode


class Member(models.Model):
    member_id = models.AutoField(
        db_column='member_id',
        primary_key=True
    )
    id = models.CharField(
        db_column="id",
        null=False,
        max_length=50,
        help_text="로그인 ID"
    )
    password = models.CharField(
        db_column="password",
        null=False,
        max_length=150,
        help_text="패스워드"
    )
    password_change_date = models.DateTimeField(
        db_column="password_change_date",
        null=False,
        auto_now=True,
        help_text="비밀번호 변경일"
    )
    active_code = models.CharField(
        db_column="active_code",
        choices=MemberActiveCode.choices,
        default=MemberActiveCode.ACTIVE,
        max_length=1,
        help_text="1: 활성화, 8: 휴면, 9:탈퇴"
    )
    create_date = models.DateTimeField(
        db_column="create_date",
        null=False,
        auto_now=True,
        help_text="등록일"
    )

    class Meta:
        managed = False
        db_table = "member"