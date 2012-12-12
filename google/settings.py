# -*- coding: utf-8 -*-

"""
google.settings
~~~~~~~~~~~~~~~

This module implements the default Django Google settings.

:copyright: (c) 2012 by Alexis Tabary.
:license: Apache2, see LICENSE for more details.

"""

from django.conf import settings

GOOGLE_ANALYTICS_ID = getattr(settings, 'GOOGLE_ANALYTICS_ID', None)
