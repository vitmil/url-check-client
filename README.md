# About url check client
url_check_client.py is a client to make requests vs URL CHECK, a RESTful Web Services running on https://129.152.26.254

Note:
If your firewall blocks outgoing connection, to reach the service on url-check (IP 129.152.26.254), 
outgoing traffic must be allowed for:

- tcp port 8000 for http requests
- tcp port 8443 for https requests

# Syntax to pass target: 

## Output formatted text
url_check_client.py  -t www.site.com

url_check_client.py  -t http://site.com

url_check_client.py  -t https://site.com

## Output json format wants -o json argument

url_check_client.py -t www.site.com  -o json



# Syntax to pass file: 

## Output formatted text

url_check_client.py -f \<file> 


## Output json format wants -o json argument

url_check_client.py -f \<file> -o json 



# What does Url Check do

#### https://https://129.152.26.254/about

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
 
