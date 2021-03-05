from django.contrib import admin
from .models import Developer, Skill

class SkillInline(admin.StackedInline):
    model = Skill
    extra = 2


class DeveloperAdmin(admin.ModelAdmin):
    fieldsets = [
        ('country',    {'fields':['country']}),
        (None,         {'fields': ['name']}),
        ('experience', {'fields':['experience']}),
    ]
    inlines = [SkillInline]    

# Register your models here.
admin.site.register(Developer, DeveloperAdmin)

