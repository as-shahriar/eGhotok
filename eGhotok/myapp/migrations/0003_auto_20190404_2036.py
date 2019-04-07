# Generated by Django 2.1.5 on 2019-04-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190404_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='fb',
            field=models.URLField(blank=True),
        ),
    ]
