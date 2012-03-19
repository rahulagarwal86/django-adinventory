"""
    Settings File for Google Adsense Script
    Replace Googletag function with your adsense Function received from Google DFP/Adsence
"""

"""
 This script function is called if no expando banner is present on the page
"""
TOP_SCRIPT = '''
            <script type="text/javascript">
            var googletag = googletag || {};
            googletag.cmd = googletag.cmd || [];
            (function() {
            var gads = document.createElement('script');
            gads.async = true; gads.type = 'text/javascript';
            gads.src = "http://www.googletagservices.com/tag/js/gpt.js";
            var node = document.getElementsByTagName('script')[0];
            node.parentNode.insertBefore(gads, node);
            })();
            </script>
            '''

"""
 This script function is called if expando banner is present on the page
"""
EXPANDO_TOP_SCRIPT = '''
                    <script type='text/javascript'>
                    (function() {
                    var useSSL = 'https:' == document.location.protocol;
                    var src = (useSSL ? 'https:' : 'http:') +
                    '//www.googletagservices.com/tag/js/gpt.js';
                    document.write('<scr' + 'ipt src="' + src + '"></scr' + 'ipt>');
                    })();
                    </script>
                    '''

"""
This is Start lines of define unit function
"""
MID_SCRIPT = '''
            <script type="text/javascript">
            googletag.cmd.push(function() {
            '''

"""
 This is End lines of define unit function and is called if expando banner is present on the page
"""
EXPANDO_BOTTOM = '''
                 googletag.pubads().enableSyncRendering();
                 googletag.pubads().enableSingleRequest();
                '''
"""
 This is End lines of define unit function and is called if no expando banner is present on the page
"""           
BOTTOM_SCRIPT = '''
                googletag.enableServices();
                });
                </script>
                '''
