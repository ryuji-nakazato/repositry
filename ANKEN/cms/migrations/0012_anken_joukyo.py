# Generated by Django 3.0.2 on 2020-03-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='anken',
            name='joukyo',
            field=models.CharField(blank=True, max_length=255, verbose_name='状況'),
        ),
    ]
