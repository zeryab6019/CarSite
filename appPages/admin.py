from django.contrib import admin
from . models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,obj):
        return format_html('<img src = "{}" width = "40" style = "border-radius: 50px">'.format(obj.photo.url))

    list_display = ('id','thumbnail' ,'first_name','last_name','designation','created_date')
    list_display_links = ('id','thumbnail', 'first_name','last_name')
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)


# Register your models here.


admin.site.register(Team,TeamAdmin)
