# Generated by Django 3.2.13 on 2022-05-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=100),
        ),
    ]
