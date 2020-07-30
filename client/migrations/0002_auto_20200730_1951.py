# Generated by Django 3.0.7 on 2020-07-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_squashed_0026_document_signed_doc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'permissions': [('approved', 'The user is approved'), ('staff', 'The user is staff of the non primary group')]},
        ),
        migrations.AlterField(
            model_name='document',
            name='compilation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
