from django.contrib import admin
from personal.models import Search_input

class SearchAdmin(admin.ModelAdmin):
    readonly_fields = ('date_search',)

admin.site.register(Search_input,SearchAdmin)



