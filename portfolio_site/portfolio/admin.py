
from django.contrib import admin
from .models import Project, Rating

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_rating')
    inlines = [RatingInline]

admin.site.register(Project, ProjectAdmin)
