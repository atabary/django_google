django_google
=============

Django Google is an Apache2 Licensed library, intending to make it easy to use Google services
like Google Analytics with Django Projects. It does currently support only Google Analytics.

Configuration
-------------

Add ``GOOGLE_ANALYTICS_ID`` with the correct analytics id to the settings of your Django project.

Usage
-----

On the page where you want to add Google Analytics javascript, add ``{% load analytics %}`` and ``{% analytics %}`` right before the closing ``</body>`` tag.

If ``GOOGLE_ANALYTICS_ID`` is not defined in the settings of your django project, the templatetag will simply output ``''``, leaving your webpage clean.
