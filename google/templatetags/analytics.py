# -*- coding: utf-8 -*-

"""
google.templatetags.analytics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements Google Analytics related template tags.

:copyright: (c) 2012 by Alexis Tabary.
:license: Apache2, see LICENSE for more details.

"""

from django import template
from django.template import Context

from google import settings

register = template.Library()


@register.simple_tag()
def analytics(analytics_id=None):
    """
    Include Google Analytics javascript inside a web page.

    Syntax::

        {% load analytics %}
        {% analytics %}

    """

    # Get the analytics id
    if not analytics_id:
        analytics_id = settings.GOOGLE_ANALYTICS_ID

    # Return the string
    if analytics_id is None:
        return ''
    else:
        t = template.loader.get_template('google/analytics.html')
        return t.render(Context(
            {
                'google': {
                    'analytics_id': analytics_id,
                },
            },
        ))
