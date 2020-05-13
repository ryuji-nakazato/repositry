# Generated by Django 3.0.2 on 2020-02-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20200210_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='anken',
            name='archiveflag',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='anken',
            name='donyu',
            field=models.DateField(verbose_name='導入時期'),
        ),
        migrations.AlterField(
            model_name='anken',
            name='jutyu',
            field=models.DateField(verbose_name='受注時期'),
        ),
    ]
