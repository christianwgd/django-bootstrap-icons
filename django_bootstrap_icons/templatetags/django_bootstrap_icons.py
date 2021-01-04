""" django bootstrap icons templatetags """
from django.template import Library

BOOTSTRAP_ICON_CLASS = 'bi'

register = Library()


@register.inclusion_tag('django_bootstrap_icons/icon.html')
def bs_icon(icon_name, extra_classes=None):
    """
    Template tag for rendering a bootstrap icon
    :param str icon_name: Name of material icon to render
    :param str extra_classes: String of classes to add to icon
    """
    # add extra classes onto material class tag
    class_str = BOOTSTRAP_ICON_CLASS
    if extra_classes:
        class_str += ' {}'.format(extra_classes)

    return {
        'classes': class_str,
        'icon_name': icon_name,
    }


@register.inclusion_tag('django_bootstrap_icons/include_bootstrap_icons.html')
def include_bootstrap_icons():
    """
    Template tag for loading the stylesheet for the icon web font
    """
    return {}
