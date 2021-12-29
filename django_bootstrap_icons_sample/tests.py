import xml

from django.conf import settings
from django.test import TestCase

from django_bootstrap_icons.templatetags.bootstrap_icons import get_static, render_svg, custom_icon, get_icon


class BootstrapIconsTest(TestCase):

    def setUp(self):
        self.apps_xml = (
                '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
                'version="1.1" id="mdi-apps" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">\n\t'
                '<path d="M16,20H20V16H16M16,14H20V10H16M10,8H14V4H10M16,8H20V4H16M10,14H14V10H10M4,14H8V10H4M4,'
                '20H8V16H4M10,20H14V16H10M4,8H8V4H4V8Z"/>\n</svg>\n'
        )

    def test_get_static(self):
        static_root = settings.STATIC_ROOT
        self.assertEqual(
            get_static('test'),
            f'{static_root}/custom-icons/test.svg'
        )

    def test_render_svg(self):
        icon_path = get_static('apps')
        content = xml.dom.minidom.parse(icon_path)
        self.assertIn(
            self.apps_xml,
            render_svg(content, size=None, color=None, extra_classes=None)
        )

    def test_render_svg_size(self):
        icon_path = get_static('apps')
        content = xml.dom.minidom.parse(icon_path)
        self.assertIn(
            'width="20px" height="20px"',
            render_svg(content, size='20px', color=None, extra_classes=None)
        )

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
        self.assertIn(
            self.apps_xml,
            custom_icon('apps', size=None, color=None, extra_classes=None)
        )

    def test_get_icon_cache_not_found(self):
        base_url = settings.BS_ICONS_BASE_URL
        icon_name = 'abcde'
        icon_path = f'{base_url}icons/{icon_name}.svg'
        ico = get_icon(icon_path, icon_name, size=None, color=None, extra_classes=None)
        pass

    def test_icon_from_cache(self):
        pass

    def test_icon_load_cache(self):
        pass

    def test_bootstrap_icon(self):
        pass

    def test_material_design_icon(self):
        pass
