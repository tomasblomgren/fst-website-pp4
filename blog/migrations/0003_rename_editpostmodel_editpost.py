# Generated by Django 3.2.16 on 2023-04-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_editpostmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EditPostModel',
            new_name='EditPost',
        ),
    ]
