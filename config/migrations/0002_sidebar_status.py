# Generated by Django 2.2.3 on 2019-08-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '展示'), (2, '下线')], default=1, verbose_name='状态'),
        ),
    ]
