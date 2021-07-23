# Generated by Django 3.1.2 on 2021-03-17 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('client', '0006_documenttype_max_instances'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_documents', models.BooleanField(default=False)),
                ('group', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
    ]
