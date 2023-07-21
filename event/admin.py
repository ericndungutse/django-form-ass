from django.contrib import admin
from event.models import Event,Category
# Register your models here.
@admin.register(Event)
class EventAmin(admin.ModelAdmin):
    list_display =( 'id', 'title', 'description', 'start_date', 'end_date', 'location', 'is_free', 'category_id')

@admin.register(Category)
class CategoryAmin(admin.ModelAdmin):
    list_display = ("id", "name")
