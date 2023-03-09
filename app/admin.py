from django.contrib import admin

from .models import *

admin.site.register(Fanlar)


class TestAdmin(admin.ModelAdmin):
    list_display = ['fan',"ID"]
    
    list_per_page = 10
admin.site.register(Test,TestAdmin)

