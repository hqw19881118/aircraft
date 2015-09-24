# coding=utf-8
from django.db import models
import sys

reload(sys)
sys.setdefaultencoding("utf8")

# Create your models here.
class BulletInfo(models.Model):
    made_date = models.DateField(verbose_name=u'制造日期')
    made_in = models.CharField(max_length=100, verbose_name=u'产地')
    bullet_model = models.CharField(max_length=100, verbose_name=u'弹药型号')
    bullet_num = models.IntegerField(verbose_name=u'挂弹数量')
    bullet_price = models.FloatField(verbose_name=u'每枚价格(美金)')

    def __str__(self):
        return '{}, {}'.format(self.made_in, self.bullet_model)


# some other models