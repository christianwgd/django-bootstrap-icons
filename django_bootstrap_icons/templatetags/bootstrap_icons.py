""" django bootstrap icons templatetags """
import os
import xml.dom.minidom
import requests

from django.conf import settings
from django.contrib.staticfiles.finders import find
# noinspection PyProtectedMember
from django.template import Library
from django.utils.html import format_html


register = Library()


def get_static(icon_name):
    """
    Get the correct path in development and production
    :param icon_name:
    :return: icon path
    """
    custom_path = getattr(
        settings,
        'BS_ICONS_CUSTOM_PATH',
        'custom-icons'
    )
    if settings.DEBUG:
        return os.path.join(
            find(custom_path), '.'.join((icon_name, 'svg'))
        )
    return os.path.join(
        settings.STATIC_ROOT, custom_path, '.'.join((icon_name, 'svg'))
    )


def render_svg(content, size, color, extra_classes):
    """
    Render the svg with custom properties
    :param content:
    :param size:
    :param color:
    :param extra_classes:
    :return:
    """
    svg = content.getElementsByTagName('svg')

    if extra_classes:
        if 'class' in svg[0].attributes:
            svg[0].attributes['class'].value += ' ' + extra_classes
        else:
            svg[0].setAttribute('class', extra_classes)

    if size:
        svg[0].setAttribute('width', size)
        svg[0].setAttribute('height', size)

    if not 'color' in svg[0].attributes:
        svg[0].setAttribute('fill', "currentColor")
    if color:
        svg[0].setAttribute('fill', color)

    return content.toprettyxml()


@register.simple_tag
def custom_icon(icon_name, size=None, color=None, extra_classes=None):
    """
    Template tag for rendering a custom icon
    :param str icon_name: Name of custom icon to render
    :param str size: size of custom icon to render
    :param str color: color of custom icon to render
    :param str extra_classes: String of classes to add to icon
    """
    if icon_name is None:
        return ''

    icon_path = get_static(icon_name)
    try:
        content = xml.dom.minidom.parse(icon_path)
    except FileNotFoundError:
        return f"Icon <{icon_path}> does not exist"
    return format_html(render_svg(content, size, color, extra_classes))


@register.simple_tag
def bs_icon(icon_name, size=None, color=None, extra_classes=None):
    """
    Template tag for rendering a bootstrap icon
    :param str icon_name: Name of bootstrap icon to render
    :param str size: size of bootstrap icon to render
    :param str color: color of bootstrap icon to render
    :param str extra_classes: String of classes to add to icon
    """
    if icon_name is None:
        return ''

    base_url = getattr(
        settings,
        'BS_ICONS_BASE_URL',
        'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/'
    )
    icon_path = os.path.join(
        base_url, 'icons', '.'.join((icon_name, 'svg'))
    )
    resp = requests.get(icon_path)
    if resp.status_code >= 400:
        return f"Icon <{icon_path}> does not exist"

    content = xml.dom.minidom.parseString(resp.text)
    return format_html(render_svg(content, size, color, extra_classes))


@register.simple_tag
def md_icon(icon_name, size=None, color=None, extra_classes=None):
    """
    Template tag for rendering a material design icon
    :param str icon_name: Name of bootstrap icon to render
    :param str size: size of bootstrap icon to render
    :param str color: color of bootstrap icon to render
    :param str extra_classes: String of classes to add to icon
    """
    if icon_name is None:
        return ''

    base_url = getattr(
        settings,
        'MD_ICONS_BASE_URL',
        'https://cdn.jsdelivr.net/npm/@mdi/svg@5.9.55/'
    )
    icon_path = os.path.join(
        base_url, 'svg', '.'.join((icon_name, 'svg'))
    )
    resp = requests.get(icon_path)
    if resp.status_code >= 400:
        return f"Icon <{icon_path}> does not exist"

    # Set same size for mdi like bi
    if size is None:
        size = '20'

    # set some classes, so one can style the icons globally
    if extra_classes is None:
        extra_classes = f'mdi mdi-{icon_name}'
    else:
        extra_classes = f'mdi mdi-{icon_name} {extra_classes}'

    content = xml.dom.minidom.parseString(resp.text)
    return format_html(render_svg(content, size, color, extra_classes))
