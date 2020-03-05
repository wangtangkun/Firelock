from django.db import models

# Create your models here.
class Department(models.Model):
    """
    部门表
    """
    name = models.CharField(max_length=32, verbose_name="部门名称")
    count = models.IntegerField(verbose_name="人数", default=0)

    def __str__(self):
        return self.name

class UserProfile(User):
    """
    用户表
    """
    username = models.EmailField(max_length=255, unique=True, )
    password = models.CharField(max_length=128)
    name = models.CharField('名字', max_length=32,null=True)
    department = models.ForeignKey('Department', default=None, blank=True, null=True)
    mobile = models.CharField('手机', max_length=32, default=None, blank=True, null=True)
    memo = models.TextField('备注', blank=True, null=True, default=None)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name