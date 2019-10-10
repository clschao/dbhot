"""
Django settings for supercrm project.

Generated by 'django-admin startproject' using Django 1.11.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hy3#2c5svc_92_4xmd$@jec253#v@8o_w2=6vz!n(j&ozfqspv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sales.apps.SalesConfig',
    'rbac.apps.RbacConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'sales.utils.mymiddleware.UserAuth',
    'rbac.rbacs.mymiddleware.PermissionAuth',
]

ROOT_URLCONF = 'supercrm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'supercrm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'supercrm',
        'HOST':'127.0.0.1',
        'PORT':3306,
        'USER':'root',
        'PASSWORD':'666'

    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'statics'),
]


PER_PAGE_NUM = 10 #每页显示多少条数据
PAGE_NUM_SHOW = 5 #显示的页码数

PERMISSION_KEY = 'permissions'
MENU_KEY = 'menu_dict'



# 创建日志的路径
LOG_PATH = os.path.join(BASE_DIR, 'log')
# 如果地址不存在，则自动创建log文件夹
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


# LOGGING = {
#     "version": 1, #保留字段,不能变
#     "disable_existing_loggers": False,  # 是否禁用已经存在的日志实例(django自带的报错),一般不禁用.
#     "formatters": { #用来记录日志的输出格式
#         "default": {
#             "format": '%(levelname)s|%(asctime)s|%(module)s|%(lineno)d|%(message)s'
#         },
#         "simple": {
#             "format": '%(asctime)s|%(levelname)s|%(message)s'
#         }
#     },
#     'filters': {  # 定义日志的过滤器
#         'require_debug_true': {  # 只有在setting中的 DEBUG = True 的时候才会生效
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     "handlers": {  #定义日志的详细格式
#         "console": {
#             "level": "DEBUG",
#             "formatter": "simple",
#             'class': 'logging.StreamHandler', #用来定义日志的切分格式
#             'filters': ['require_debug_true'], #只有在debug=True的时候才会在屏幕上显示内容
#         },
#         "admin": {
#             "level": "INFO",
#             "formatter": "default",
#             'class': 'logging.handlers.RotatingFileHandler', # 按照大小来切割
#             "filename": "%s/issue.log"%LOG_PATH,# 日志位置
#             "maxBytes": 1024 * 1024 * 10, # 日志的大小
#             "encoding": "utf-8", #编码格式
#             "backupCount": 5 #最多保留5个
#         },
#         "error": {
#             "level": "ERROR",
#             "formatter": "default",
#             'class': 'logging.handlers.TimedRotatingFileHandler', # 按照时间来切分
#             "filename": "%s/issue.log"%LOG_PATH,
#             "when": "D", # 每天一切， 可选值有S/秒 M/分 H/小时 D/天 W0-W6/周(0=周一) midnight/如果没指定时间就默认在午夜
#             "encoding": "utf-8"
#         }
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console", "admin"],
#             "level": "DEBUG"
#         },
#         "default": {
#             "handlers": ["admin", "error"],
#             "level": "INFO",
#             'propagate': True,  # 是否向上一级logger实例传递日志信息
#         }
#     }
# }


LOGGING = {
    # version只能为1,定义了配置文件的版本，当前版本号为1.0
    "version": 1,
    # True表示禁用logger
    "disable_existing_loggers": False,
    # 格式化
    'formatters': {
        'default': {
            'format': '%(levelno)s %(funcName) %(module)s %(asctime)s %(message)s '
        },
        'simple': {
            'format': '%(levelno)s %(module)s %(created)s %(message)s'
        }
    },

    'handlers': {
        'stu_handlers': {
            'level': 'DEBUG',
            # 日志文件指定为5M, 超过5m重新命名，然后写入新的日志文件
            'class': 'logging.handlers.RotatingFileHandler',
            # 指定文件大小
            'maxBytes': 5 * 1024,
            # 指定文件地址
            'filename': '%s/log.txt' % LOG_PATH,
            'formatter': 'default'
        },
        'uauth_handlers': {
            'level': 'DEBUG',
            # 日志文件指定为5M, 超过5m重新命名，然后写入新的日志文件
            'class': 'logging.handlers.RotatingFileHandler',
            # 指定文件大小
            'maxBytes': 5 * 1024 * 1024,
            # 指定文件地址
            'filename': '%s/uauth.txt' % LOG_PATH,
            'formatter': 'simple',
            'encoding':'utf-8'
        }
    },
    'loggers': {
        'stu': {
            'handlers': ['stu_handlers'],
            'level': 'INFO'
        },
        'auth': {
            'handlers': ['uauth_handlers'],
            'level': 'INFO'
        }
    },

    'filters': {

        }
}



