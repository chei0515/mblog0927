from django.contrib import admin
from mytest.models import  Post, Mood

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('nickname', 'message', 'enabled', 'pub_time')



admin.site.register(Post,PostAdmin)
admin.site.register(Mood)
