# Generated by Django 5.0.6 on 2024-07-05 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_creator_email_post_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_posts',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.news'),
        ),
    ]
