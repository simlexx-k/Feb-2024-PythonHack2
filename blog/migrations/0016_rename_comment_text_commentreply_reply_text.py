# Generated by Django 5.0.4 on 2024-04-30 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_commentreply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentreply',
            old_name='comment_text',
            new_name='reply_text',
        ),
    ]
