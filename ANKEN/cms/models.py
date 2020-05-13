from django.db import models
from django.utils import timezone
# Create your models here.


class Anken(models.Model):
    enduser = models.CharField('E/U', max_length=255)
    hansha = models.CharField('販社', max_length=255)
    product = models.CharField('プロダクト', max_length=255)
    sbkk = models.CharField('SBKKトスアップ', max_length=255, blank=True)
    hansui = models.CharField('販推', max_length=255, blank=True)
    sisuisin = models.CharField('SI推進', max_length=255)
    hitouch = models.CharField('ハイタッチ担当', max_length=255, blank=True)
    donyusien = models.CharField('導入支援', max_length=255, blank=True)
    jutyu = models.DateField('受注時期', blank=False)
    donyu = models.DateField('導入時期', blank=False)
    kakudo = models.CharField('確度', max_length=255, blank=True)
    kyougou = models.CharField('競合', max_length=255, blank=True)
    kousinjikoku = models.DateField(verbose_name='', blank=True, null=True, auto_now=True)
    archiveflag = models.BooleanField(verbose_name='', default=False)
    mitumorigaku = models.DecimalField('見積もり金額', max_digits=10, decimal_places=0, blank=True, null=True)
    arari = models.DecimalField('粗利額', max_digits=10, decimal_places=0, blank=True, null=True)
    joukyo = models.CharField('状況', max_length=255, blank=True)

    def __str__(self):
        return self.enduser


class Sintyoku(models.Model):
    sintyoku = models.ForeignKey(Anken, verbose_name='案件', related_name='sintyokus', on_delete=models.CASCADE)
    kinyubi = models.DateField('記入日', blank=True, default=timezone.now)
    shosai = models.TextField('進捗内容', blank=True)

    def __str__(self):
        return self.shosai


class Todo(models.Model):
    todo = models.ForeignKey(Anken, verbose_name='案件', related_name='todos', on_delete=models.CASCADE)
    kanryoflg = models.BooleanField(verbose_name='', default=False)
    task = models.TextField('タスク', blank=True)
    kigen = models.DateField('期限', blank=True)

    def __str__(self):
        return self.todo


class Task(models.Model):
    anken = models.ForeignKey(Anken, verbose_name='案件', related_name='tasks', on_delete=models.CASCADE)
    kanryoflg = models.BooleanField(verbose_name='', default=False)
    task = models.TextField('タスク', blank=True)
    kigen = models.DateField('期限', blank=True)
    tantou = models.CharField('担当', max_length=255, blank=True)

    def __str__(self):
        return self.task

