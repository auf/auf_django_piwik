# -*- coding: utf-8 -*-

import re
from settings import PIWIK_TOKEN, PIWIK_HOST, PIWIK_TRACKCODE

ire_body = re.compile(re.escape('</body>'), re.IGNORECASE)


class TrackMiddleware:

    def process_response(self, request, response):
        """
        Trackcode injection avant le body s'il y a un token piwik dans la conf
        locale.
        """
        if PIWIK_TOKEN is None:
            return response

        if request.is_secure():
            protocol = "https"
        else:
            protocol = "http"

        track = PIWIK_TRACKCODE % {
                'host': PIWIK_HOST,
                'token': PIWIK_TOKEN,
                'protocol': protocol,
                }

        content = response.content
        content_with_trackcode = ire_body.sub('%s</body>' % track, content)
        response.content = content_with_trackcode
        return response
