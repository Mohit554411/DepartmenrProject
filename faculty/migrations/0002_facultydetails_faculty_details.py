# Generated by Django 4.0.6 on 2022-08-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultydetails',
            name='faculty_details',
            field=models.TextField(default=True),
        ),
    ]