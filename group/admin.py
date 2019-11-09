from django.contrib import admin
from .models import Group, GroupMember

# Register your models here.

# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name','slug','description')
#     list_filter = ('name',)
#     search_fields = ('name','id','slug')
#     list_display_links = ('id','name')
#     list_per_page = 2
class GroupAdmin(admin.ModelAdmin):
    list_per_page = 2
    list_display = ('id','name','slug','description')

admin.site.register(Group,GroupAdmin)
admin.site.register(GroupMember)