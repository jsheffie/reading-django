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
    username = "anonldap@ultra-ats.com"
    password  = "atsadmin"
    l.simple_bind(username, password)
except ldap.LDAPError, e:
    print e

baseDN = "cn=Users, dc=ultra-ats, dc=com"
searchScope = ldap.SCOPE_SUBTREE
searchFilter = "cn=*jeff*"
#searchFilter = "cn=*jack*"
retrieveAttributes = None 
#retrieveAttributes = ["displayName","sAMAccountName"]
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
    for itm in result_set:
        user_dn=itm[0][0]
        user_dict=itm[0][1]
        print "-----------------------------------"
        print "%s" % (user_dn) 
        print "-----------------------------------"
        for (key, value) in user_dict.iteritems():
            print "Key: %-30s, %s" % (key, value)
        #foo = itm[0][0]
        #print "-----> %s" % ( foo)
        #print "---> %s" % (type(itm[foo]))
except ldap.LDAPError, e:
    print e
