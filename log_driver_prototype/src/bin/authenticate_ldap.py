#!/usr/bin/env python

# From Steve
# name password: anonldap atsadmin
# account is in the domain "ultra-ats"
# might need to be specified as ultra-ats anonldap)
# search root: cn=users, dc=ultra-ats, dc=com
# authentication type: simple

import ldap
try:
    #l = ldap.open("armstrong.ultra-ats.com")
    l = ldap.open("strongarm.ultra-ats.com")
    l.protocol_version = ldap.VERSION3
    #username = "cn=anonldap, cn=Users, dc=ultra-ats, dc=com"
    username = "cn=anonldap, dc=ultra-ats, dc=com"
    password  = "atsadmin"
    l.simple_bind(username, password)
except ldap.LDAPError, e:
    print e

baseDN = "cn=users, dc=ultra-ats, dc=com"
searchScope = ldap.SCOPE_SUBTREE
searchFilter = "cn=*jack*"
retrieveAttributes = None 

try:
    ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
    result_set = []
    while 1:
        result_type, result_data = l.result(ldap_result_id, 0)
        if (result_data == []):
            print "Did not find anything"
            break
        else:
            ## here you don't have to append to a list
            ## you could do whatever you want with the individual entry
            ## The appending to list is just for illustration. 
            if result_type == ldap.RES_SEARCH_ENTRY:
                result_set.append(result_data)
    print result_set
except ldap.LDAPError, e:
	print e
