# Generated by Django 2.0.7 on 2020-02-25 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=models.TextField(default='season description in few lines'),
        ),
    ]