from django.contrib import admin
from adinventory.models import  AdSlot, AdUnit

class AdUnitAdmin( admin.ModelAdmin ):
    
    model = AdUnit
    list_display = ( 'url', 'keyword_1', 'keyword_2' )
    ordering = ['url']
    search_fields = ['url']
    filter_horizontal = ['adslots']
    exclude = ['define_scripts', 'fetch_scripts']

admin.site.register( AdSlot )
admin.site.register( AdUnit , AdUnitAdmin )
