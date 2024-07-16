""" django bootstrap icons templatetags """
import os
from pathlib import Path
import requests
from defusedxml.minidom import parse, parseString

from django.conf import settings
from django.contrib.staticfiles.finders import find
# noinspection PyProtectedMember
from django.core.exceptions import ImproperlyConfigured
from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


def get_static(icon_name):
    """
    Get the correct path in development and production
    :param icon_name:
    :return: icon path
    """
    custom_dir = getattr(
        settings,
        'BS_ICONS_CUSTOM_PATH',
        'custom-icons'
    )

    if settings.DEBUG:
        custom_path = find(custom_dir)
        if not custom_path:
            ex_msg = "BS_ICONS_CUSTOM_PATH does not exist."
            raise ImproperlyConfigured(ex_msg)
    else:
        custom_path = os.path.join(settings.STATIC_ROOT, custom_dir)

    if not os.path.exists(custom_path):
        ex_msg = "BS_ICONS_CUSTOM_PATH does not exist."
        raise ImproperlyConfigured(ex_msg)

    return os.path.join(
        custom_path, '.'.join((icon_name, 'svg'))
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
        content = parse(icon_path)
    except FileNotFoundError:
        return f"Icon `{icon_path}` does not exist"
    return mark_safe(render_svg(content, size, color, extra_classes))


def get_icon(icon_path, icon_name, size=None, color=None, extra_classes=None):
    """
    Manage caching of bootstrap icons
    :param icon_path icon_path: icon path given by CDN or local path
    :param str icon_name: Name of custom icon to render
    :param str size: size of custom icon to render
    :param str color: color of custom icon to render
    :param str extra_classes: String of classes to add to icon
    :type icon_path: str or Path
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
        cache_name = f'{icon_name}_{size}_{color}_{extra_classes}.svg'.replace(' ', '_')
        cache_file = os.path.join(cache_path, cache_name)
        if os.path.exists(cache_file):
            # icon exists in cache, use that
            with open(cache_file, 'r', encoding="utf-8") as icon_file:
                return icon_file.read()

    # cached icon doesn't exist or no cache configured, create and return icon
    try:
        if isinstance(icon_path, Path):
            # icon_path is local path
            with icon_path.open("r") as icon_file:
                svg_string = icon_file.read()
        else:
            # icon_path is URL
            resp = requests.get(icon_path, timeout=20)
            if resp.status_code == 404:
                # co-opt FileNotFoundError for HTTP 404
                msg = "Got HTTP 404 when downloading icon"
                raise FileNotFoundError(msg)
            resp.raise_for_status()
            svg_string = resp.text

    except FileNotFoundError:
        # The icon was not found (on disk, or on the web)
        return getattr(
            settings,
            "BS_ICONS_NOT_FOUND",
            f"Icon `{icon_path}` does not exist",
        )

    # RequestException includes ConnectionError, Timeout, HTTPError and TooManyRedirects
    except (requests.exceptions.RequestException, OSError):
        # We failed to get the icon, but it might exist
        return getattr(
            settings, "BS_ICONS_NOT_FOUND", f"Failed to read icon `{icon_path}`"
        )

    content = parseString(svg_string)
    svg = render_svg(content, size, color, extra_classes)

    # if cache configured write icon to cache
    if cache_path and cache_file:
        with open(cache_file, "w", encoding="utf-8") as icon_file:
            icon_file.write(svg)

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

    base_path = getattr(settings, "BS_ICONS_BASE_PATH", None)

    if base_path:
        icon_path = Path(base_path, "icons", f"{icon_name}.svg")
    else:
        base_url = getattr(
            settings,
            "BS_ICONS_BASE_URL",
            "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/",
        )
        icon_path = f"{base_url}icons/{icon_name}.svg"

    svg = get_icon(icon_path, icon_name, size, color, extra_classes)
    return mark_safe(svg)


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

    base_path = getattr(settings, "MD_ICONS_BASE_PATH", None)

    if base_path:
        icon_path = Path(base_path, "svg", f"{icon_name}.svg")
    else:
        base_url = getattr(
            settings,
            "MD_ICONS_BASE_URL",
            "https://cdn.jsdelivr.net/npm/@mdi/svg@7.2.96/",
        )
        icon_path = f"{base_url}svg/{icon_name}.svg"

    svg = get_icon(icon_path, icon_name, size, color, extra_classes)
    return mark_safe(svg)
