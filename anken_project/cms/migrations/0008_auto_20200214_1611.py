# Generated by Django 3.0.2 on 2020-02-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20200214_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='anken',
            name='arari',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='anken',
            name='mitumorigaku',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]