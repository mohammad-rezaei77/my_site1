# Generated by Django 3.2 on 2022-09-26 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220926_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post2',
            old_name='categorys',
            new_name='category',
        ),
    ]