# Generated by Django 5.0.6 on 2024-07-05 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Post_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.creator')),
                ('comment_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.news')),
            ],
        ),
    ]