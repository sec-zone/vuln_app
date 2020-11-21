from django.contrib import admin
from .models import BlogUser, Email


class BlogUserFields(admin.ModelAdmin):
    list_display = ('username', 'create_date', 'update_date')

# Register your models here.
admin.site.register(BlogUser, BlogUserFields)
admin.site.register(Email)