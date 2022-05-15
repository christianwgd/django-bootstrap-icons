import xml
import os

from django.conf import settings
from django.test import TestCase, override_settings

from django_bootstrap_icons.templatetags.bootstrap_icons import get_static, render_svg, \
    custom_icon, get_icon, bs_icon, md_icon


class BootstrapIconsTest(TestCase):

    def test_get_static(self):
        static_root = settings.STATIC_ROOT
        self.assertEqual(
            get_static('test'),
            f'{static_root}/custom-icons/test.svg'
        )

    def test_render_svg(self):
        icon_path = get_static('apps')
        content = xml.dom.minidom.parse(icon_path)
        rendered = render_svg(content, size=None, color=None, extra_classes=None)
        self.assertIn('id="test-icon"', rendered)
        self.assertIn('viewBox="0 0 24 24"', rendered)
        self.assertIn('width="24"', rendered)

    def test_render_svg_size(self):
        icon_path = get_static('apps')
        content = xml.dom.minidom.parse(icon_path)
        rendered = render_svg(content, size='20px', color=None, extra_classes=None)
        self.assertIn('width="20px"', rendered)
        self.assertIn('height="20px"', rendered)

    def test_render_svg_color(self):
        icon_path = get_static('apps')
        content = xml.dom.minidom.parse(icon_path)
        self.assertIn(
            'fill="red"',
            render_svg(content, size=None, color='red', extra_classes=None)
        )

    def test_render_svg_extra_classes(self):
        icon_path = get_static('apps')
        content = xml.dom.minidom.parse(icon_path)
        self.assertIn(
            'class="class_a, class_b"',
            render_svg(content, size=None, color=None, extra_classes='class_a, class_b')
        )

    def test_custom_icon(self):
        rendered = custom_icon('apps', size=None, color=None, extra_classes=None)
        self.assertIn('id="test-icon"', rendered)
        self.assertIn('viewBox="0 0 24 24"', rendered)
        self.assertIn('width="24"', rendered)

    def test_get_icon_cache_not_found(self):
        base_url = getattr(
            settings,
            'BS_ICONS_BASE_URL',
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.2/',
        )
        icon_not_found = getattr(
            settings, 'BS_ICONS_NOT_FOUND'
        )
        icon_name = 'abcde'
        icon_path = f'{base_url}icons/{icon_name}.svg'
        ico = get_icon(icon_path, icon_name, size=None, color=None, extra_classes=None)
        self.assertEqual(ico, icon_not_found)

    # Make sure we test without cache
    @override_settings(BS_ICONS_CACHE=None)
    def test_boostrap_icon(self):
        asterisk_icon = bs_icon('asterisk', size=None, color=None, extra_classes=None)
        self.assertIn(
            'class="bi bi-asterisk"', asterisk_icon
        )

    # Make sure we test without cache
    # @override_settings(BS_ICONS_CACHE=None)
    def test_material_design_icon(self):
        asterisk_icon = md_icon('asterisk', size=None, color=None, extra_classes=None)
        self.assertIn(
            'id="mdi-asterisk"', asterisk_icon
        )
        self.assertIn(
            'class="mdi mdi-asterisk"', asterisk_icon
        )

    def test_bootstrap_icon_cache(self):
        cache_path = getattr(
            settings,
            'BS_ICONS_CACHE',
            None
        )
        bs_icon_file = os.path.join(cache_path, 'asterisk_None_None_None.svg')
        # delete cached icon file
        _ = os.remove(bs_icon_file) if os.path.exists(bs_icon_file) else None
        self.assertFalse(os.path.exists(bs_icon_file))
        # load icon into chache
        asterisk_icon = bs_icon('asterisk', size=None, color=None, extra_classes=None)
        self.assertIn(
            'class="bi bi-asterisk"', asterisk_icon
        )
        # check if icon file is in cache
        self.assertTrue(os.path.exists(bs_icon_file))

    def test_material_design_icon_cache(self):
        cache_path = getattr(
            settings,
            'BS_ICONS_CACHE',
            None
        )
        md_icon_file = os.path.join(cache_path, 'asterisk_20_None_mdi_mdi-asterisk.svg')
        # delete cached icon file
        os.remove(md_icon_file)
        self.assertFalse(os.path.exists(md_icon_file))
        # load icon into chache
        asterisk_icon = md_icon('asterisk', size=None, color=None, extra_classes=None)
        self.assertIn(
            'id="mdi-asterisk"', asterisk_icon
        )
        self.assertIn(
            'class="mdi mdi-asterisk"', asterisk_icon
        )
        # check if icon file is in cache
        self.assertTrue(os.path.exists(md_icon_file))
