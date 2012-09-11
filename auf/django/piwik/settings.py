# -*- coding: utf-8 -*-


from django.conf import settings

PIWIK_TOKEN = getattr(settings, 'PIWIK_TOKEN', None)

PIWIK_HOST = getattr(settings, 'PIWIK_HOST', 'piwik.auf.org')

PIWIK_TRACKCODE = """
<!-- Piwik -->
<script type="text/javascript">
    var pkBaseURL = "%(protocol)s://%(host)s/";
    document.write(unescape("%%3Cscript src='" + pkBaseURL + "piwik.js' type='text/javascript'%%3E%%3C/script%%3E"));
    </script><script type="text/javascript">
    try {
        var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", %(token)s);
        piwikTracker.trackPageView();
        piwikTracker.enableLinkTracking();
    }
    catch( err ) {}
</script>
<noscript>
    <p><img src="%(protocol)s://%(host)s/piwik.php?idsite=%(token)s" style="border:0" alt="" /> </p>
</noscript>
<!-- End Piwik Tracking Code -->
"""
