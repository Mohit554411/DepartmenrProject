# Generated by Django 4.0.6 on 2022-08-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_alter_activitydetails_activity_img1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitydetails',
            name='activity_img2',
            field=models.ImageField(blank=True, default=True, max_length=250, null=True, upload_to='activity/'),
        ),
        migrations.AlterField(
            model_name='activitydetails',
            name='activity_img3',
            field=models.ImageField(blank=True, default=True, max_length=250, null=True, upload_to='activity/'),
        ),
    ]
