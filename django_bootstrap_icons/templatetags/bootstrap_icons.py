""" django bootstrap icons templatetags """
import os
import requests
import xml.dom.minidom

from django.conf import settings
from django.contrib.staticfiles.finders import find
from django.template import Library
from django.utils.html import format_html


register = Library()


def get_static(icon_name):
    custom_path = getattr(
        settings,
        'BS_ICONS_CUSTOM_PATH',
        'custom-icons'
    )
    if settings.DEBUG:
        return os.path.join(
            find(custom_path), '.'.join((icon_name, 'svg'))
        )
    else:
        return os.path.sjoin(
            settings.STATIC_ROOT, custom_path, '.'.join((icon_name, 'svg'))
        )


@register.simple_tag
def custom_svg(icon_name, size=None, color=None, extra_classes=None):
    if icon_name is None:
        return ''
    try:
        icon_path = get_static(icon_name)
        content = xml.dom.minidom.parse(icon_path)
        svg = content.getElementsByTagName('svg')

        if extra_classes:
            svg[0].attributes['class'].value += ' '+extra_classes
        if size:
            svg[0].attributes['width'].value = size
            svg[0].attributes['height'].value = size
        if color:
            svg[0].attributes['fill'].value = color

        result = content.toprettyxml()
    except:
        result=''
        import traceback
        traceback.print_exc()

    return format_html(result)


@register.simple_tag
def bs_icon_svg(icon_name, size=None, color=None, extra_classes=None):
    """
        Template tag for rendering a bootstrap icon
        :param str icon_name: Name of bootstrap icon to render
        :param str size: size of bootstrap icon to render
        :param str color: color of bootstrap icon to render
        :param str extra_classes: String of classes to add to icon
        :param boolean custom: True if this is a custom icon added by you
               make sure you have added the BS_ICONS_CUSTOM_PATH in settings.py
        """
    if icon_name is None:
        return ''

    try:
        base_url = getattr(
            settings,
            'BS_ICONS_BASE_URL',
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/'
        )
        icon_path = os.path.join(
            base_url, 'icons', '.'.join((icon_name, 'svg'))
        )

        resp = requests.get(icon_path)
        content = xml.dom.minidom.parseString(resp.text)
        svg = content.getElementsByTagName('svg')

        if extra_classes:
            svg[0].attributes['class'].value += ' '+extra_classes
        if size:
            svg[0].attributes['width'].value = size
            svg[0].attributes['height'].value = size
        if color:
            svg[0].attributes['fill'].value = color

        result = content.toprettyxml()
    except:
        result=''
        import traceback
        traceback.print_exc()

    return format_html(result)


