# Generated by Django 3.2.15 on 2022-10-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20221015_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sql_test',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
