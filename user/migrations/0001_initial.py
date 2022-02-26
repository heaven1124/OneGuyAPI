# Generated by Django 4.0.2 on 2022-02-25 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
                ('auth_key', models.CharField(max_length=100, verbose_name='口令')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='注册时间')),
                ('status', models.IntegerField(choices=[(0, '未激活'), (1, '正常'), (2, '注销')], verbose_name='状态')),
            ],
            options={
                'verbose_name': '客户信息',
                'verbose_name_plural': '客户信息',
                'db_table': 't_app_user',
            },
        ),
    ]