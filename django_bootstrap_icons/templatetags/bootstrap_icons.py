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

    if 'color' not in svg[0].attributes:
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


def icon(icon_path, icon_name, size=None, color=None, extra_classes=None):
    """
    Manage caching of bootstrap icons
    :param str icon_path: icon path given by CDN
    :param str icon_name: Name of custom icon to render
    :param str size: size of custom icon to render
    :param str color: color of custom icon to render
    :param str extra_classes: String of classes to add to icon
    """
    cache_path = getattr(
        settings,
        'BS_ICONS_CACHE',
        None
    )
    cache_file = None

    if cache_path:
        if not os.path.exists(cache_path):
            os.makedirs(cache_path)
        cache_name = f'{icon_name}_{size}_{color}_{extra_classes}.svg'
        cache_file = os.path.join(cache_path, cache_name)
        if os.path.exists(cache_file):
            # icon exists in cache, use that
            return open(cache_file, 'r').read()

    # cached icon doesn't exist or no cache configured, create and return icon
    try:
        resp = requests.get(icon_path)
        if resp.status_code >= 400:
            # return f"Icon <{icon_path}> does not exist"
            return getattr(
                settings,
                'BS_ICONS_NOT_FOUND',
                f"Icon <{icon_path}> does not exist"
            )
        content = xml.dom.minidom.parseString(resp.text)
        svg = render_svg(content, size, color, extra_classes)
        # if cache configured write icon to cache
        if cache_path and cache_file:
            open(cache_file, 'w').write(svg)
    except requests.ConnectionError:
        return getattr(
            settings,
            'BS_ICONS_NOT_FOUND',
            f"Icon <{icon_path}> does not exist"
        )
    return svg


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
        'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/',
    )
    icon_path = f'{base_url}icons/{icon_name}.svg'

    svg = icon(icon_path, icon_name, size, color, extra_classes)
    resp = format_html(svg)
    return resp


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

    # set some classes, so one can style the icons globally
    if extra_classes is None:
        extra_classes = f'mdi mdi-{icon_name}'
    else:
        extra_classes = f'mdi mdi-{icon_name} {extra_classes}'

    # Set same size for mdi like bi
    if size is None:
        size = '20'

    base_url = getattr(
        settings,
        'MD_ICONS_BASE_URL',
        'https://cdn.jsdelivr.net/npm/@mdi/svg@5.9.55/'
    )
    icon_path = f'{base_url}svg/{icon_name}.svg'

    svg = icon(icon_path, icon_name, size, color, extra_classes)
    resp = format_html(svg)
    return resp
