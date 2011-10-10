#!/usr/bin/env python
import ldap

#hostname="armstrong.ultra.ats.com"
hostname="ldap://strongarm.ultra-ats.com"
protover = ldap.VERSION3
#protover = ldap.VERSION2

thingies = [
    { "hostname": hostname,
      "protocol_version": protover,
      "username": "cn=administrator, dc=ultra-ats, dc=com",
      "password": "Tas@78744",
      "baseDN"  : "cn=users, dc=ultra-ats, dc=com",
     },
#    { "hostname": hostname,
#      "protocol_version": protover,
#      "username": "cn=anonldap, cn=users, dc=ultra-ats, dc=com",
#      "password": "atsadmin",
#      "baseDN"  : "cn=users, dc=ultra-ats, dc=com",
#     },
#    { "hostname": hostname,
#      "protocol_version": protover,
#      "username": "cn=ultra-ats\\anonldap, cn=Users, dc=ultra-ats, dc=com",
#      "password": "atsadmin",
#      "baseDN"  : "cn=users, dc=ultra-ats, dc=com",
#     },
#    { "hostname": hostname,
#      "protocol_version": protover,
#      "username": "cn=anonldap, cn=Users, dc=ultra-ats, dc=com",
#      "password": "atsadmin",
#      "baseDN"  : "cn=Users, dc=ultra-ats, dc=com",
#     },
#    { "hostname": hostname,
#      "protocol_version": protover,
#      "username": "cn=anonldap, cn=Users, dc=ultra-ats, dc=com",
#      "password": "atsadmin",
#      "baseDN"  : "dc=ultra-ats, dc=com",
#     },
#    { "hostname": hostname,
#      "protocol_version": protover,
#      "username": "cn=anonldap, cn=Users, dc=ultra-ats, dc=com",
#      "password": "atsadmin",
#      "baseDN"  : "cn=Users, dc=ultra-ats, dc=com",
#     },
#    { "hostname": hostname,
#      "protocol_version": protover,
#      "username": "cn=Users, dc=ultra-ats, dc=com",
#      "password": "",
#      "baseDN"  : "cn=Users, dc=ultra-ats, dc=com",
#     },
#    { "hostname": hostname,
#      "protocol_version": protover,
#      "username": "dc=ultra-ats, dc=com",
#      "password": "",
#      "baseDN"  : "dc=ultra-ats, dc=com",
#     },

    ]

cnt=0
for thingie in thingies:
    cnt = cnt+1
    print "Trying thingie %d: hostname: %s username: %s" % ( cnt, thingie["hostname"], thingie["username"])
    try:
        #ldap.set_option()
        #l = ldap.open(thingie["hostname"])
        l = ldap.initialize(thingie["hostname"])
        l.protocol_version = thingie["protocol_version"]
        #l.simple_bind(thingie["username"], thingie["password"])
        #l.simple_bind_s(thingie["username"], thingie["password"])
        l.bind(thingie["username"], thingie["password"])
        #l.simple_bind()
        # disableing OPT_REFERRALS option is needed for active directory
        # http://publib.boulder.ibm.com/infocenter/iseries/v5r3/index.jsp?topic=%2Fapis%2Fldap_set_option.htm
        l.set_option(ldap.OPT_REFERRALS, 0)
        # SCOPE_BASE (to search the object itself), 
        # SCOPE_ONELEVEL (to search the object's immediate children)
        # SCOPE_SUBTREE (to search the object and all its descendants).
        #searchScope = ldap.SCOPE_BASE
        searchScope = ldap.SCOPE_SUBTREE
        searchFilter = "(&(objectClass=User)(sAMAccountName="+jds+"))"
        #searchFilter = "(&(objectClass=User))"
        #searchFilter = "cn=*jack*"
        retrieveAttributes = ["displayName"]
    
        try:
            
            ldap_result_id = l.search(thingie["baseDN"], searchScope, searchFilter, retrieveAttributes)
            result_set = []
            while 1:
                print "search success"
                result_type, result_data = l.result(ldap_result_id, 0)
                #result_type, result_data = l.result(ldap_result_id, 60)
                print "result success"
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
            print "SEARCH:FAILED with thingie %d" % ( cnt)
            print "    ", e

        
        
    except ldap.LDAPError, e:
        print "BIND:FAILED with thingie %d" % ( cnt)
        print "    ", e
        continue
    
