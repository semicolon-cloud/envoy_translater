"""
WSGI config for envoy_translator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

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
WSGI config for Envoy Translator.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from keystonemiddleware.auth_token import AuthProtocol

from envoy_translator.config import CONF

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "envoy_translator.settings")


application = get_wsgi_application()

# Here we replace the default application with one wrapped by
# the Keystone Auth Middleware.
conf = {
    "auth_plugin": "password",
    "username": CONF.identity.auth.username,
    "password": CONF.identity.auth.password,
    "project_name": CONF.identity.auth.project_name,
    "project_domain_id": CONF.identity.auth.project_domain_id,
    "user_domain_id": CONF.identity.auth.user_domain_id,
    "auth_url": CONF.identity.auth.auth_url,
    "interface": CONF.identity.auth.interface,
    "delay_auth_decision": True,
    "include_service_catalog": False,
    "token_cache_time": CONF.identity.token_cache_time,
}
application = AuthProtocol(application, conf)
