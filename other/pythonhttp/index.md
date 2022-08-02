

## http client
https://docs.python.org/3/library/http.client.html

## config file 
https://docs.python.org/3/library/configparser.html


## SSL 
https://stackoverflow.com/questions/51390968/python-ssl-certificate-verify-error
I have found this over here

I found this solution, insert this code at the beginning of your source file:

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context 


## JSON
