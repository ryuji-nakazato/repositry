# Generated by Django 3.0.2 on 2020-02-05 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anken',
            name='donyu',
            field=models.CharField(blank=True, max_length=255, verbose_name='導入時期'),
        ),
        migrations.AddField(
            model_name='anken',
            name='hansui',
            field=models.CharField(blank=True, max_length=255, verbose_name='販推'),
        ),
        migrations.AddField(
            model_name='anken',
            name='jutyu',
            field=models.CharField(blank=True, max_length=255, verbose_name='受注時期'),
        ),
        migrations.AddField(
            model_name='anken',
            name='product',
            field=models.CharField(blank=True, max_length=255, verbose_name='プロダクト'),
        ),
        migrations.AddField(
            model_name='anken',
            name='sisuisin',
            field=models.CharField(blank=True, max_length=255, verbose_name='SI推進'),
        ),
    ]