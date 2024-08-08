from django.contrib import admin
from .models import News, Category



class NewsAdmin(admin.ModelAdmin):
    list_display = ("date_time", "title", "image", "author", "category","highlight1","highlight2","highlight2","recent_post1","recent_post2","recent_post3")
admin.site.register(News,NewsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(Category, CategoryAdmin)
