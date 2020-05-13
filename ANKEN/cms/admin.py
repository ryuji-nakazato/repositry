from django.contrib import admin
from cms.models import Anken, Sintyoku, Task
# Register your models here.

# admin.site.register(Anken)


class AnkenAdmin(admin.ModelAdmin):
    list_display = ('id', 'enduser', 'hansha',)
    list_display_links = ('id', 'enduser', 'hansha',)


admin.site.register(Anken, AnkenAdmin)


class SintyokuAdmin(admin.ModelAdmin):
    list_display = ('id', 'kinyubi', 'shosai',)
    list_display_links = ('id', 'kinyubi', 'shosai',)


admin.site.register(Sintyoku, SintyokuAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'kanryoflg', 'task', 'tantou',)
    list_display_links = ('id', 'kanryoflg', 'task', 'tantou',)


admin.site.register(Task, TaskAdmin)
