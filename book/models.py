from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='项目名称')
    description = models.TextField(blank=True, verbose_name='项目描述')
    # start_date = models.DateField(verbose_name='开始日期')
    # end_date = models.DateField(null=True, blank=True, verbose_name='结束日期')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目管理'