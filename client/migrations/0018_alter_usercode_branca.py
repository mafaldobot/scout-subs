# Generated by Django 4.1.5 on 2023-07-25 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('client', '0017_document_usercode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercode',
            name='branca',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='auth.group'),
        ),
    ]
