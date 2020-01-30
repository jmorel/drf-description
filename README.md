# DRF-description

Minimal illustration of a DRF issue: actions named `description` make any access to the view fail with an error 500
and the message below.

To reproduce run the server using `python manage.py runserver` and navigate to `http://127.0.0.1:8000/dummy/foo/description.json`

```
TypeError at /dummy/foo/description.json
'NoneType' object is not callable

Request Method: GET
Request URL: http://127.0.0.1:8000/dummy/foo/description.json
Django Version: 3.0.2
Python Executable: /Users/jeremy/.virtualenvs/drf-description/bin/python
Python Version: 3.7.3
Python Path: ['/Users/jeremy/drf-description', '/Users/jeremy/.virtualenvs/drf-description/lib/python37.zip', '/Users/jeremy/.virtualenvs/drf-description/lib/python3.7', '/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/lib-dynload', '/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/site-packages']
Server time: Thu, 30 Jan 2020 08:19:50 +0000
Installed Applications:
['django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'django_extensions']
Installed Middleware:
['django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware']


Traceback (most recent call last):
  File "/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/site-packages/rest_framework/viewsets.py", line 114, in view
    return self.dispatch(request, *args, **kwargs)
  File "/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/Users/jeremy/.virtualenvs/drf-description/lib/python3.7/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)

Exception Type: TypeError at /dummy/foo/description.json
Exception Value: 'NoneType' object is not callable
Request information:
USER: AnonymousUser

GET: No GET data

POST: No POST data

FILES: No FILES data

COOKIES: No cookie data

META:
COLORFGBG = '15;0'
COLORTERM = 'truecolor'
CONTENT_LENGTH = ''
CONTENT_TYPE = 'text/plain'
CPPFLAGS = '-I/usr/local/opt/openssl/include'
DJANGO_SETTINGS_MODULE = 'drfdescription.settings'
GATEWAY_INTERFACE = 'CGI/1.1'
HOME = '/Users/jeremy'
HTTP_ACCEPT = 'text/html;version=0.0, */*;version=0.0'
HTTP_ACCEPT_ENCODING = 'gzip, deflate, br'
HTTP_ACCEPT_LANGUAGE = 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
HTTP_CONNECTION = 'keep-alive'
HTTP_HOST = '127.0.0.1:8000'
HTTP_SEC_FETCH_MODE = 'navigate'
HTTP_SEC_FETCH_SITE = 'none'
HTTP_SEC_FETCH_USER = '?1'
HTTP_UPGRADE_INSECURE_REQUESTS = '1'
HTTP_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
ITERM_PROFILE = 'Default'
ITERM_SESSION_ID = 'w0t3p0:88F911CB-4B09-439D-9CE9-7335F583114C'
LANG = 'fr_FR.UTF-8'
LC_TERMINAL = 'iTerm2'
LC_TERMINAL_VERSION = '3.3.7'
LDFLAGS = '-L/usr/local/opt/openssl/lib'
LESS = '-R'
LOGNAME = 'jeremy'
LSCOLORS = 'Gxfxcxdxbxegedabagacad'
OLDPWD = '/Users/jeremy/drf-description/drfdescription'
PAGER = 'less'
PATH = '/Users/jeremy/.virtualenvs/drf-description/bin:/Users/jeremy/google-cloud-sdk/bin:/Users/jeremy/dotfiles/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:/Library/Apple/bin'
PATH_INFO = '/dummy/foo/description.json'
PIP_RESPECT_VIRTUALENV = 'true'
PIP_VIRTUALENV_BASE = '/Users/jeremy/.virtualenvs'
PWD = '/Users/jeremy/drf-description'
QUERY_STRING = ''
REMOTE_ADDR = '127.0.0.1'
REMOTE_HOST = ''
REQUEST_METHOD = 'GET'
RUN_MAIN = 'true'
SCRIPT_NAME = ''
SERVER_NAME = '1.0.0.127.in-addr.arpa'
SERVER_PORT = '8000'
SERVER_PROTOCOL = 'HTTP/1.1'
SERVER_SOFTWARE = 'WSGIServer/0.2'
SHELL = '/bin/zsh'
SHLVL = '1'
SSH_AUTH_SOCK = '/private/tmp/com.apple.launchd.8AfS5AnnIZ/Listeners'
SUBSTRA_PATH = '/tmp/substra'
SUBSTRA_SRC_PATH = '/Users/jeremy/substra'
TERM = 'xterm-256color'
TERM_PROGRAM = 'iTerm.app'
TERM_PROGRAM_VERSION = '3.3.7'
TERM_SESSION_ID = 'w0t3p0:88F911CB-4B09-439D-9CE9-7335F583114C'
TMPDIR = '/var/folders/z9/tjd43wyd11j9h9tn51m84jjm0000gn/T/'
TZ = 'UTC'
USER = 'jeremy'
VIRTUALENVWRAPPER_HOOK_DIR = '/Users/jeremy/.virtualenvs'
VIRTUALENVWRAPPER_PROJECT_FILENAME = '.project'
VIRTUALENVWRAPPER_PYTHON = '/usr/local/bin/python3'
VIRTUALENVWRAPPER_SCRIPT = '/usr/local/bin/virtualenvwrapper.sh'
VIRTUALENVWRAPPER_VIRTUALENV_ARGS = '--no-site-packages'
VIRTUALENVWRAPPER_WORKON_CD = '1'
VIRTUAL_ENV = '/Users/jeremy/.virtualenvs/drf-description'
VIRTUAL_ENV_DISABLE_PROMPT = '1'
WORKON_HOME = '/Users/jeremy/.virtualenvs'
XPC_FLAGS = '0x0'
XPC_SERVICE_NAME = '0'
ZSH = '/Users/jeremy/.oh-my-zsh'
ZSH_CUSTOM = '/Users/jeremy/dotfiles/zsh_custom'
_ = '/Users/jeremy/.virtualenvs/drf-description/bin/python'
__CF_USER_TEXT_ENCODING = '0x1F5:0x0:0x1'
wsgi.errors = <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>
wsgi.file_wrapper = ''
wsgi.input = <django.core.handlers.wsgi.LimitedStream object at 0x10916db38>
wsgi.multiprocess = False
wsgi.multithread = True
wsgi.run_once = False
wsgi.url_scheme = 'http'
wsgi.version = '(1, 0)'

Settings:
Using settings module drfdescription.settings
ABSOLUTE_URL_OVERRIDES = {}
ADMINS = []
ALLOWED_HOSTS = []
APPEND_SLASH = True
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
AUTH_PASSWORD_VALIDATORS = '********************'
AUTH_USER_MODEL = 'auth.User'
BASE_DIR = '/Users/jeremy/drf-description'
CACHES = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_KEY_PREFIX = '********************'
CACHE_MIDDLEWARE_SECONDS = 600
CSRF_COOKIE_AGE = 31449600
CSRF_COOKIE_DOMAIN = None
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_PATH = '/'
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = False
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
CSRF_TRUSTED_ORIGINS = []
CSRF_USE_SESSIONS = False
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': '/Users/jeremy/drf-description/db.sqlite3', 'ATOMIC_REQUESTS': False, 'AUTOCOMMIT': True, 'CONN_MAX_AGE': 0, 'OPTIONS': {}, 'TIME_ZONE': None, 'USER': '', 'PASSWORD': '********************', 'HOST': '', 'PORT': '', 'TEST': {'CHARSET': None, 'COLLATION': None, 'NAME': None, 'MIRROR': None}}}
DATABASE_ROUTERS = []
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000
DATETIME_FORMAT = 'N j, Y, P'
DATETIME_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M:%S.%f', '%m/%d/%Y %H:%M', '%m/%d/%Y', '%m/%d/%y %H:%M:%S', '%m/%d/%y %H:%M:%S.%f', '%m/%d/%y %H:%M', '%m/%d/%y']
DATE_FORMAT = 'N j, Y'
DATE_INPUT_FORMATS = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y', '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y']
DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = False
DECIMAL_SEPARATOR = '.'
DEFAULT_CHARSET = 'utf-8'
DEFAULT_EXCEPTION_REPORTER_FILTER = 'django.views.debug.SafeExceptionReporterFilter'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
DEFAULT_INDEX_TABLESPACE = ''
DEFAULT_TABLESPACE = ''
DISALLOWED_USER_AGENTS = []
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = '********************'
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = '********************'
EMAIL_SUBJECT_PREFIX = '[Django] '
EMAIL_TIMEOUT = None
EMAIL_USE_LOCALTIME = False
EMAIL_USE_SSL = False
EMAIL_USE_TLS = False
FILE_CHARSET = 'utf-8'
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None
FILE_UPLOAD_HANDLERS = ['django.core.files.uploadhandler.MemoryFileUploadHandler', 'django.core.files.uploadhandler.TemporaryFileUploadHandler']
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440
FILE_UPLOAD_PERMISSIONS = 420
FILE_UPLOAD_TEMP_DIR = None
FIRST_DAY_OF_WEEK = 0
FIXTURE_DIRS = []
FORCE_SCRIPT_NAME = None
FORMAT_MODULE_PATH = None
FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'
IGNORABLE_404_URLS = []
INSTALLED_APPS = ['django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'django_extensions']
INTERNAL_IPS = []
LANGUAGES = [('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kab', 'Kabyle'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmål'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')]
LANGUAGES_BIDI = ['he', 'ar', 'fa', 'ur']
LANGUAGE_CODE = 'en-us'
LANGUAGE_COOKIE_AGE = None
LANGUAGE_COOKIE_DOMAIN = None
LANGUAGE_COOKIE_HTTPONLY = False
LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_COOKIE_PATH = '/'
LANGUAGE_COOKIE_SAMESITE = None
LANGUAGE_COOKIE_SECURE = False
LOCALE_PATHS = []
LOGGING = {}
LOGGING_CONFIG = 'logging.config.dictConfig'
LOGIN_REDIRECT_URL = '/accounts/profile/'
LOGIN_URL = '/accounts/login/'
LOGOUT_REDIRECT_URL = None
MANAGERS = []
MEDIA_ROOT = ''
MEDIA_URL = ''
MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware']
MIGRATION_MODULES = {}
MONTH_DAY_FORMAT = 'F j'
NUMBER_GROUPING = 0
PASSWORD_HASHERS = '********************'
PASSWORD_RESET_TIMEOUT_DAYS = '********************'
PREPEND_WWW = False
ROOT_URLCONF = 'drfdescription.urls'
SECRET_KEY = '********************'
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_SECONDS = 0
SECURE_PROXY_SSL_HEADER = None
SECURE_REDIRECT_EXEMPT = []
SECURE_REFERRER_POLICY = None
SECURE_SSL_HOST = None
SECURE_SSL_REDIRECT = False
SERVER_EMAIL = 'root@localhost'
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_AGE = 1209600
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = False
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_FILE_PATH = None
SESSION_SAVE_EVERY_REQUEST = False
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SETTINGS_MODULE = 'drfdescription.settings'
SHORT_DATETIME_FORMAT = 'm/d/Y P'
SHORT_DATE_FORMAT = 'm/d/Y'
SIGNING_BACKEND = 'django.core.signing.TimestampSigner'
SILENCED_SYSTEM_CHECKS = []
STATICFILES_DIRS = []
STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_ROOT = None
STATIC_URL = '/static/'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': [], 'APP_DIRS': True, 'OPTIONS': {'context_processors': ['django.template.context_processors.debug', 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth', 'django.contrib.messages.context_processors.messages']}}]
TEST_NON_SERIALIZED_APPS = []
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
THOUSAND_SEPARATOR = ','
TIME_FORMAT = 'P'
TIME_INPUT_FORMATS = ['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = False
USE_TZ = True
USE_X_FORWARDED_HOST = False
USE_X_FORWARDED_PORT = False
WSGI_APPLICATION = 'drfdescription.wsgi.application'
X_FRAME_OPTIONS = 'DENY'
YEAR_MONTH_FORMAT = 'F Y'


You're seeing this error because you have DEBUG = True in your
Django settings file. Change that to False, and Django will
display a standard page generated by the handler for this status code.

```