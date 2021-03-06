# Generated by Django 2.1.3 on 2018-11-19 23:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emaiverfyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaiverfyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间'),
        ),
        migrations.AlterField(
            model_name='emaiverfyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '忘记密码')], default='register', max_length=8, verbose_name='验证码类型'),
        ),
    ]
