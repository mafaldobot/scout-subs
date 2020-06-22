# Generated by Django 3.0.7 on 2020-06-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0023_auto_20200622_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicaldata',
            name='health_care_certificate',
            field=models.FileField(default=None, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='medicaldata',
            name='vac_certificate',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
