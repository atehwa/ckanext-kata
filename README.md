ckanext-kata
============

Kata extension for CKAN. Used by Etsin (https://etsin.avointiede.fi/en/).  And fully clobbered by atehwa.

Installation
============

To install this extension

  pip install -e git://github.com/kata-csc/ckanext-kata.git#egg=ckanext-kata

.ini configuration
==================
Put following lines under [app:main]

    kata.contact_roles = Author, Maintainer, Publisher, Sponsor, Funder, Distributor, Producer
    kata.date_format = %d.%m.%Y
    
    # Hide certain extras fields from dataset read form:
    package_hide_extras = role
    
    # Hide certain extras fields from edit form
    kata.hide_extras_form = role pid
