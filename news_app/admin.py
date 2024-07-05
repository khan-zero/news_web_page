from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Creator)
admin.site.register(models.News)
admin.site.register(models.News_posts)
admin.site.register(models.Post_comments)
