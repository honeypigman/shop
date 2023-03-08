from django.db import models


class MemberActiveCode(models.IntegerChoices):
    ACTIVE = 1          # 활성화
    INACTIVE = 8        # 휴면
    OUT = 9             # 탈퇴