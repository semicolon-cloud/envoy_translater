# Copyright (C) 2015 Catalyst IT Ltd
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Django settings for envoy_translater.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

from envoy_translater.config import CONF as et_conf

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Application definition

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_swagger",
    "envoy_translater.listeners",
    "envoy_translater.api",
)

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "envoy_translater.middleware.KeystoneHeaderUnwrapper",
    "envoy_translater.middleware.RequestLoggingMiddleware",
)

if "test" in sys.argv:
    # modify MIDDLEWARE
    MIDDLEWARE = list(MIDDLEWARE)
    MIDDLEWARE.remove("envoy_translater.middleware.KeystoneHeaderUnwrapper")
    MIDDLEWARE.append("envoy_translater.middleware.TestingHeaderUnwrapper")

ROOT_URLCONF = "envoy_translater.urls"

WSGI_APPLICATION = "envoy_translater.wsgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "NAME": "default",
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": ["/etc/envoy_translater/templates/"],
        "NAME": "include_etc_templates",
    },
]

AUTHENTICATION_BACKENDS = []

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "envoy_translater.api.exception_handler.exception_handler",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_PERMISSION_CLASSES": [],
}

SECRET_KEY = et_conf.django.secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = et_conf.django.debug
if DEBUG:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].append(
        "rest_framework.renderers.BrowsableAPIRenderer"
    )

ALLOWED_HOSTS = et_conf.django.allowed_hosts

SECURE_PROXY_SSL_HEADER = (
    et_conf.django.secure_proxy_ssl_header,
    et_conf.django.secure_proxy_ssl_header_value,
)

DATABASES = et_conf.django.databases

if et_conf.django.logging:
    LOGGING = et_conf.django.logging
else:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "filename": et_conf.django.log_file,
            },
        },
        "loggers": {
            "envoy_translater": {
                "handlers": ["file"],
                "level": "INFO",
                "propagate": False,
            },
            "django": {
                "handlers": ["file"],
                "level": "INFO",
                "propagate": False,
            },
            "keystonemiddleware": {
                "handlers": ["file"],
                "level": "INFO",
                "propagate": False,
            },
        },
    }
