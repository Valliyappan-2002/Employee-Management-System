# Generated by Django 3.2.9 on 2022-09-11 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VasanMeena', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='pswd',
            field=models.CharField(default='vs', max_length=15),
        ),
    ]
