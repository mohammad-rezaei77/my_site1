# Generated by Django 3.2 on 2022-09-26 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_categorys_post2_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categorys',
            new_name='category',
        ),
    ]