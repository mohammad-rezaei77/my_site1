# Generated by Django 3.2.15 on 2022-10-27 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post2',
            name='login_required',
            field=models.BooleanField(default=False),
        ),
    ]
