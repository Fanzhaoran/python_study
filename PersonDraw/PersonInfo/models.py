from django.db import models
from django.utils import timezone
from datetime import datetime


class Person(models.Model):
    GENDER_CHOICES = (
        (u'M', u'男'),
        (u'W', u'女'),
    )
    name = models.CharField("姓名", max_length=50)  # 必须指定默认字段
    gender = models.CharField("性别", max_length=2, choices=GENDER_CHOICES)
    id_no = models.CharField("工号", max_length=30, unique=True)  # 工号
    birth_date = models.DateField("出生年月", default=datetime(1990, 1, 1))
    experience = models.IntegerField("工作经验年限")
    Level = models.CharField("岗位", max_length=50)
    work_zone = models.CharField("部门", max_length=50)
    skill = models.TextField("技术")
    create_time = models.DateTimeField("创建时间", default=timezone.now)

    class Meta:
        ordering = ("-create_time",)
        db_table = "个人信息"
        verbose_name = "简介"
        verbose_name_plural = "简介"

    def __str__(self):
        return self.name + '_' + self.id_no  # 返回的姓名_工号


class Program(models.Model):
    """
    # 项目的基本信息
    """
    name = models.CharField("项目名", max_length=50)
    module = models.CharField("模块", max_length=50)

    def __str__(self):
        return self.name + '-' + self.module

    class Meta:
        ordering = ("name",)
        db_table = "项目"
        verbose_name = "项目"
        verbose_name_plural = "项目"


class ProgramInFo(models.Model):
    """
    # 个人在项目中的信息
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_item', blank=True)
    program = models.ManyToManyField(Program, related_name='program_info', blank=True)
    module_name = models.CharField("模块名称", max_length=50, blank=True)
    bugs_Any = models.IntegerField("发现bug数量", blank=True)
    bugs_deal = models.IntegerField("解决bug数量", blank=True)
    bugs_start_time = models.DateField("发现bug起始时间", blank=True)
    bugs_end_time = models.DateField("解决bug结束时间", blank=True)
    work_list = models.TextField("主要成就", blank=True)

    class Meta:
        ordering = ("module_name",)
        db_table = "业绩"
        verbose_name = "业绩"
        verbose_name_plural = "业绩"

    def __str__(self):
        # print(self.person.name)
        # print(self.person.id_no)
        # print(self.module_name)
        return self.person.name + self.person.id_no + self.module_name
