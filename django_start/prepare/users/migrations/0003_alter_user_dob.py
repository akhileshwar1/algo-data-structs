# Generated by Django 3.2.8 on 2021-10-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
