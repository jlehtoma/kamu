# Django settings for kamu project.
import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG
JS_DEBUG = False

COMPRESS_ENABLED = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
# This is used at least for new supporting members
NOTIFICATIONS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kamu',
        'USER': 'kamu',
        'PASSWORD': 'kamu'
    }
}

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Helsinki'

# Language code for this installation. All choices can be found here:
LANGUAGES_EXT=(('en', 'English', 'in English'),
               ('fi', 'Finnish', 'suomeksi'))
LANGUAGES=[(l[0], l[1]) for l in LANGUAGES_EXT]

LOCALE_PATHS = [
    SITE_ROOT + '/locale'
]

# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'fi'
DATE_FORMAT = 'd.m.Y'
TIME_FORMAT = 'H:i'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.dirname(__file__) + '/media/'
MEDIA_TMP_DIR = 'tmp/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.dirname(__file__) + '/static/'
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/coffeescript', 'coffee --compile --stdio'),
)
COMPRESS_JS_FILTERS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ljqf))w56l68l26zgtn**2u198y0j5$82o^ac%m0x23l=hq_75'

INTERNAL_IPS = ( '127.0.0.1', )

CACHE_BACKEND = 'locmem://'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    #"django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "i18n.context_processors.other_languages",
)


MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    'i18n.middleware.SetDefaultLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    'httpstatus.middleware.HttpStatusErrorsMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    #'django.contrib.admin',

    'sorl.thumbnail',
    'compressor',

    'social',
    'parliament',
    'eduskunta',
    'cms',
    'south',
    'tastypie',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Activation window from the sending of the activation e-mail
ACCOUNT_ACTIVATION_DAYS = 3
# URL for redirection when the user needs to login and nothing
# else is specified in the code, like when using pre-canned
# functionality in django-register
LOGIN_URL = '/account/login/'
DEFAULT_FROM_EMAIL = 'Kansan muisti <noreply@kansanmuisti.fi>'
SERVER_EMAIL = 'noreply@kansanmuisti.fi'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

TASTYPIE_DEFAULT_FORMATS = ['json']

FACEBOOK_ENABLED = False
FACEBOOK_APP_ID = "Set this in settings_local"
FACEBOOK_APP_SECRET = "Set this in settings_local"
# Optional
FACEBOOK_DOMAIN = None

KAMU_OPINIONS_MAGIC_USER = 'kamu'

FAST_TEST = False

try:
    from settings_local import *
except ImportError:
    pass

if 'LOCAL_INSTALLED_APPS' in locals():
    INSTALLED_APPS += LOCAL_INSTALLED_APPS
    del LOCAL_INSTALLED_APPS
if 'LOCAL_MIDDLEWARE_CLASSES' in locals():
    MIDDLEWARE_CLASSES += LOCAL_MIDDLEWARE_CLASSES
    del LOCAL_MIDDLEWARE_CLASSES

if FAST_TEST and 'test' in sys.argv:
    DATABASE_NAME = 'kamu.db'
    DATABASE_ENGINE = 'sqlite3'
    SOUTH_TESTS_MIGRATE = False
