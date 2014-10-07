__author__ = 'Yorick Chollet'

import re

#TODO move to constants

HTTP_STATUS = {
    200: "200 OK",
    404: "404 Not Found",
    302: "302 Found",
    400: "400 Bad Request"
}

URI_PARTS = {
    'G': 'timegate',
    'T': 'timemap'
}

HTTPRE = re.compile('https?://', re.IGNORECASE)
WWWRE = re.compile('www.', re.IGNORECASE)