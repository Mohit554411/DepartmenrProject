# Generated by Django 4.0.6 on 2022-08-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('qualification', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('faculty_img', models.FileField(default=True, max_length=250, null=True, upload_to='faculty/')),
            ],
        ),
    ]
