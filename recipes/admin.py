from django.contrib.auth import get_user_model
from django.contrib import admin

# Register your models here.
from .models import Recipe,RecipeIngredient

User = get_user_model()

# Allows child objects to be entered in the same pass as there parents
class RecipeIngredientInline(admin.StackedInline):
	model = RecipeIngredient
	extra = 0 # by default there are 3 instances (2 extra), this limits it to none
	readonly_fields = ['quantity_as_float','as_imperial','as_mks']

class RecipeAdmin(admin.ModelAdmin):
	inlines = [RecipeIngredientInline]
	list_display = ['name','user']
	readonly_fields = ['timestamp','updated']
	raw_id_fields = ['user']

admin.site.register(Recipe,RecipeAdmin)