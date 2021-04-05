# Generated by Django 2.2.5 on 2020-08-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_body', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PostsRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.BigIntegerField(default=0)),
                ('dislikes', models.BigIntegerField(default=0)),
            ],
        ),
    ]