# Generated by Django 5.0.4 on 2024-04-30 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_rename_comment_text_commentreply_reply_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comment'),
        ),
    ]
