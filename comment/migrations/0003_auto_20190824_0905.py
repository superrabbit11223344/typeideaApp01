# Generated by Django 2.2.3 on 2019-08-24 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=2000, null=True, verbose_name='评论目标'),
        ),
    ]
