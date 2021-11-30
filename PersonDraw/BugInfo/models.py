from django.db import models
from PersonInfo.models import Person


# Create your models here.
class BugInfo(models.Model):
    function_bug = models.IntegerField('功能缺陷', blank=0)
    flow_bug = models.IntegerField('流程异常处理', blank=0)
    unique_bug = models.IntegerField('参数唯一性约束', blank=0)
    beyond_bug = models.IntegerField('参数范围约束', blank=0)
    need_bug = models.IntegerField('必选参数约束', blank=0)
    interface_bug = models.IntegerField('接口规范', blank=0)
    datatype_bug = models.IntegerField('数据类型约束', blank=0)
    law_bug = models.IntegerField('非法字符约束', blank=0)
    other_bug = models.IntegerField('其他',  blank=0)

    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        ordering = ("person",)
        db_table = "bug类型"
        verbose_name = "bug类型"
        verbose_name_plural = "bug类型"

    def __str__(self):
        return self.person.name
