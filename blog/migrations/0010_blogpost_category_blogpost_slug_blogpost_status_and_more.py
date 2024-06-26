# Generated by Django 5.0.4 on 2024-04-27 07:04

import django.db.models.deletion
import django.utils.timezone
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_comment_author_name_remove_comment_blog_post_and_more'),
        ('profiles', '0003_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Publish')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='post-default.jpg', upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='publication_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(to='blog.tag'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.CreateModel(
            name='BlogPostX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('tags', models.ManyToManyField(related_name='blog_posts', to='blog.tag')),
            ],
        ),
    ]
