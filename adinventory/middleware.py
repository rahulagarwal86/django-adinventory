from adinventory.models import AdUnit

from django.utils.safestring import mark_safe

class AdMiddleware( object ):
    """
    Middleware to manages AdInventory on particular page or set of pages.
    """
    def process_template_response( self, request, response ):
        from adinventory.settings import TOP_SCRIPT, EXPANDO_TOP_SCRIPT, MID_SCRIPT, EXPANDO_BOTTOM, BOTTOM_SCRIPT
        path = request.get_full_path()
        if( path.find( "?google_debug" ) ):
            path = path.split( "?google_debug" )[0]
        try:
            page_ad = AdUnit.objects.get( url = path )
        except:
            raise
            try:
                path = '/' + str( path.split( '/' )[1] ) + '/'
                page_ad = AdUnit.objects.get( url = path )
            except:
                page_ad = None
        GAM_HEAD = ''
        FILL_DICT = {}
        if page_ad:
            PARAM_SCRIPT = '''    
                            googletag.pubads().setTargeting("''' + page_ad.keyword_1 + '''", "''' + page_ad.keyword_2 + '''");
                            '''
            DEFINE_SCRIPT = page_ad.define_scripts
            fetch_dict = eval( page_ad.fetch_scripts )
            for slot, script in fetch_dict.items():
                slot_name = str( slot )
                FILL_DICT[slot_name] = mark_safe( script )
            if page_ad.swosh_slot:
                TOP_SCRIPT = EXPANDO_TOP_SCRIPT
                EXPANDO_BOTTOM = EXPANDO_BOTTOM
            else:
                TOP_SCRIPT = TOP_SCRIPT
                EXPANDO_BOTTOM = ''
            GAM_HEAD = TOP_SCRIPT + MID_SCRIPT + DEFINE_SCRIPT + PARAM_SCRIPT + EXPANDO_BOTTOM + BOTTOM_SCRIPT
        response.context_data['GAM_HEAD'] = mark_safe( GAM_HEAD )
        response.context_data['FILL_DICT'] = FILL_DICT
        return response
