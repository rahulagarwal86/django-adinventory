from django.contrib import admin
from adinventory.models import  AdSlot, AdUnit, SearchAd, Word

class AdUnitAdmin( admin.ModelAdmin ):
    
    model = AdUnit
    list_display = ( 'url', 'keyword_1', 'keyword_2' )
    ordering = ['url']
    search_fields = ['url']
    filter_horizontal = ['adslots']
    exclude = ['define_scripts', 'fetch_scripts']
    
class AdSlotAdmin( admin.ModelAdmin ):
    
    model = AdSlot
    list_display = [ 'slot_name']
    ordering = ['slot_name']
    search_fields = ['slot_name']

class SearchAdAdmin( admin.ModelAdmin ):
    model = SearchAd
    list_display = [ 'keyword_2' ]
    ordering = ['keyword_2']
    search_fields = ['keyword_2']
    filter_horizontal = ['adslots', 'param1', 'param2']
    exclude = ['define_scripts', 'fetch_scripts']

admin.site.register( AdSlot, AdSlotAdmin )
admin.site.register( AdUnit , AdUnitAdmin )
admin.site.register( SearchAd, SearchAdAdmin )
admin.site.register( Word )
