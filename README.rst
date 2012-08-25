=====================
DjangoCMS tabs plugin
=====================

Features
--------

1. Drag&Drop reordering of tabs and titles

2. Unlimited, auto-discovered custom templates

3. Native support for http://twitter.github.com/bootstrap/javascript.html#tabs

Requirements
------------

- django-inline-ordering http://pypi.python.org/pypi/django-inline-ordering/
- sekizai http://pypi.python.org/pypi/django-sekizai
- to use the built in support for twitter-bootstrap, you need to provide
  twitter-bootstrap's javascript, and some specific way to include the
  libraries, look at the templates directory for details.

Installation
------------

1. Install requirements and put ``cmsplugin_s3slider`` on your python path 
   (requirements will be installed automatically if you use ``pip`` 
   with ``-e https://github.com/bclermont/cmsplugin-tabs.git``

2. Add ``cmsplugin_tabs``, and ``sekizai`` to your installed apps

3. Run ``syncdb`` or ``migrate cmsplugin_tabs`` (if you use South).

4. Add CMS_PLUGIN_PROCESSORS = [ 'cmsplugin_tabs.plugin_processors.tabs_plugin_processor' ]
   to your settings file.

5. Very simple template is included with the project. It's compatible with
   twitter-bootstrap's tabs

Usage
-----

The easiest approach is to use a nice feature of cmsplugin_tabs -
the template autodiscovery. In order to take advantage of it, add your custom 
templates in the cms/plugins/tabs/ subdirectory of any of template dirs scanned
by Django.

If you don't want to use the autodiscovery, you can hardcode available templates
in settings.py using following setting:

::

    CMSPLUGIN_TABS_TEMPLATES = (
        ('app/template.html', 'Template #1', ),
        ('app/other_template.html', 'Template #2', ),
    )

Create a TabsHeader plugin in a page, there you mark how many tabs will you use.
Also set up an according number of titles for the tabs.

Each one of the next ``n`` plugins you insert in the placeholder will be one of
the tabs' contents.

Template context variables
--------------------------
The header plugin instance lives in a variable called `wrapper`. The wrapped
plugins' already rendered content lives in a list called `plugins`.

Take a look at `cmsplugin_tabs/templates/cms/plugins/tabs/bootstrap-tabs.html
for an example.