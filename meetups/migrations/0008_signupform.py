# Generated by Django 4.0.3 on 2022-06-14 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0007_about_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
