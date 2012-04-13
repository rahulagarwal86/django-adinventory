from django.db import models
from django.db.models.signals import  post_save

class AdSlot( models.Model ):
    
    slot_name = models.CharField( max_length = 20, help_text = 'Slot name which is used in template for defining AdInventory.' )
    addslot_script = models.TextField( help_text = 'Define Unit script of AdSlot.' )
    fillslot_script = models.TextField( help_text = 'Fill Unit script of AdSlot.' )
    
    def __unicode__( self ):
        return self.slot_name

class AdUnit( models.Model ):
    
    url = models.CharField( max_length = 250 , help_text = 'Relative url of the page on which adinventory need to be called, could also be the regex url.' )
    keyword_1 = models.CharField( max_length = 10 , help_text = 'First parameter which is stored in google adsense inventory account.' )
    keyword_2 = models.CharField( max_length = 50, blank = True, null = True, help_text = 'Second parameter which is stored in google adsense inventory account.(Non Mendatory)' )
    swosh_slot = models.BooleanField( default = False, help_text = 'Check if swosh ad is present on page.' )
    adslots = models.ManyToManyField( AdSlot , blank = True, null = True, help_text = 'Slots which need to be displayed on Page.' )
    define_scripts = models.TextField( blank = True )
    fetch_scripts = models.TextField( blank = True )

    def __unicode__( self ):
        return self.url
    
    def save( self ):
        super( AdUnit, self ).save()
        ad_units = self.adslots.values( 'slot_name', 'addslot_script', 'fillslot_script' )
        DEFINE_SCRIPT = ''
        FILL_DICT = {}
        for each in ad_units:
            DEFINE_SCRIPT = DEFINE_SCRIPT + str( each['addslot_script'] )
            slot_name = str( each['slot_name'] )
            FILL_DICT[slot_name] = ( each['fillslot_script'] )
        self.define_scripts = DEFINE_SCRIPT
        self.fetch_scripts = repr( FILL_DICT )
        super( AdUnit, self ).save()
        
        
class SearchAd( models.Model ):
    
    param1 = models.ManyToManyField( 'Word', related_name = 'keyword1' )
    param2 = models.ManyToManyField( 'Word', related_name = 'keyword2', blank = True, null = True )
    keyword_1 = models.CharField( max_length = 10 , help_text = 'First parameter which is stored in google adsense inventory account.' )
    keyword_2 = models.CharField( max_length = 50, blank = True, null = True, help_text = 'Second parameter which is stored in google adsense inventory account.(Non Mendatory)' )
    swosh_slot = models.BooleanField( default = False, help_text = 'Check if swosh ad is present on page.' )
    adslots = models.ManyToManyField( AdSlot , blank = True, null = True, help_text = 'Slots which need to be displayed on Page.' )
    define_scripts = models.TextField( blank = True )
    fetch_scripts = models.TextField( blank = True )
    
    def __unicode__( self ):
        return self.keyword_2
    
    def save( self ):
        super( SearchAd, self ).save()
        ad_units = self.adslots.values( 'slot_name', 'addslot_script', 'fillslot_script' )
        DEFINE_SCRIPT = ''
        FILL_DICT = {}
        for each in ad_units:
            DEFINE_SCRIPT = DEFINE_SCRIPT + str( each['addslot_script'] )
            slot_name = str( each['slot_name'] )
            FILL_DICT[slot_name] = ( each['fillslot_script'] )
        self.define_scripts = DEFINE_SCRIPT
        self.fetch_scripts = repr( FILL_DICT )
        super( SearchAd, self ).save()

class Word( models.Model ):
    
    name = models.CharField( max_length = 500 )
    
    def __unicode__( self ):
        return self.name
