# Generated by Django 2.1.3 on 2018-12-21 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments_author',
            new_name='comment_author',
        ),
    ]
