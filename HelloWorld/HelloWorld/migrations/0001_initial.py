# Generated by Django 2.1.5 on 2019-12-30 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appId', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('createTime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
