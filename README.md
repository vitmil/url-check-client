# About url check client
url_check_client.py is a client to make requests vs web app running on url-check.vimi.space.

Note:
If your firewall blocks outgoing connection, to reach the service on url-check.vimi.space, 
outgoing traffic must be allowed for:

- tcp port 8000 for http requests
- tcp port 8443 for https requests

# Syntax to pass target: 

## Output formatted text
url_check_client.py  -t www.site.com

url_check_client.py  -t http://www.site.com

url_check_client.py  -t https://www.site.com

url_check_client.py  -t www.site.com  -o hr 



## Output json format
url_check_client.py -t www.site.com  -o json


# Syntax to pass file: 

## Output formatted text
url_check_client.py -f <file> 

url_check_client.py -f <file> -o hr 

## Output json format 
url_check_client.py -f <file> -o json 




# What does Url Check do

#### https://url-check.vimi.space/about

Url Check is a Web Application and RESTful Web Services (written in Python and Fast API) you can use to get various informations about a specific (or more) URL.

## General info:

 • HTTP status code
 
 • Server type
 
 • IP address
 
 • Hostname
 
 • CNAME
 
 • URL redirections
 
 • IP address of redirections
 
 • Landing URL

## Domain info:

 • NS authoritative
 
 • Domain name
 
 • Domain creation date
 
 • Domain update date
 
 • Domain expiration
 
 • Domain registrar
 
 • Domain registrant organization
 
 • Geolocation info


## SSL certificate info:

 • subject common name
 
 • issuer country name
 
 • issuer organization name
 
 • issuer common name
 
 • version
 
 • serial number
 
 • validity start date 
 
 • expiration date 
 
 • subject Alternative name
 
 • OCSP CA issuers
 
 • OCSP CRL distribution points
 