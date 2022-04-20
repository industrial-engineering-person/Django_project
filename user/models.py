from django.db import models

# isomnia로 user추가
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_type = models.IntegerField() # 0: 사용자, 1:사장님, 2:배달기사 =>접근권한 관리를 위해
    def __str__(self):
        return self.user_name
    
