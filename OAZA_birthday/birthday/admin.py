from django.contrib import admin

# Register your models here.
from .models import Group, Animator, Person

class GroupAdmin(admin.ModelAdmin):
    search_fields = ['name']


class AnimatorAdmin(admin.ModelAdmin):
    search_fields = ['name']


class PersonAdmin(admin.ModelAdmin):
    search_fields= ['first_name', 'last_name']


admin.site.register(Group, GroupAdmin)
admin.site.register(Animator, AnimatorAdmin)
admin.site.register(Person, PersonAdmin)