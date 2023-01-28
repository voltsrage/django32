from django.contrib import admin

from .models import Article
# Register your models here.

# Setting for admin display for article
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['id','title','content','timestamp','updated'] # List will display id, title and content
	search_fields = ['title','content'] # list can be searched by title and content

admin.site.register(Article,ArticleAdmin)