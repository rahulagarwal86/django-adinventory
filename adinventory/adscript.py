TOP_SCRIPT = """
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

MID_SCRIPT = '''
            <script type="text/javascript">
            googletag.cmd.push(function() {
            '''

EXPANDO_BOTTOM = '''
                 googletag.pubads().enableSyncRendering();
                 googletag.pubads().enableSingleRequest();
                '''
BOTTOM_SCRIPT = '''
                            googletag.enableServices();
                            });
                            </script>
                            '''
