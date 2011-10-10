# Django settings for logging_auth_prototype2 project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/home/jds/workspace/logging_auth_prototype2/src/sqlite.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
SECRET_KEY = 'kw5kn2wqyvc)*#tgv@2f-o9m5!)(yqr)_zl%p1v@78))nrv)_*'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'logging_auth_prototype2.urls'

TEMPLATE_DIRS = (
)

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
#    'django.contrib.auth.backends.RemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)


AUTH_LDAP_SERVER_URI = "ldap://strongarm.ultra-ats.com"

import ldap
#from django_auth_ldap.config import LDAPSearch

#AUTH_LDAP_BIND_DN = "anonldap"
#AUTH_LDAP_BIND_PASSWORD = "atsadmin"
##AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=ultra-ats,dc=com",
#AUTH_LDAP_USER_SEARCH = LDAPSearch("cn=users,dc=ultra-ats,dc=com",
##AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=ultra-ats,dc=com",
#    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")


#AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=ultra-ats,dc=com"
#AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,cn=users,dc=ultra-ats,dc=com"
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,dc=ultra-ats,dc=com"
AUTH_LDAP_START_TLS = True

#AUTH_LDAP_GLOBAL_OPTIONS = {
#                            ldap.OPT_REFERRALS: 0,
#                            }
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

import logging

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
