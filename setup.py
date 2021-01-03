import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-bootstrap-icons',
    version='0.1.0',
    packages=[
        'django_bootstrap_icons',
    ],
    include_package_data=True,
    description='A quick way to add Bootstrap Icons with Django template tags.',
    long_description=README,
    author='Christian Wiegand',
    license='MIT',
    url='https://github.com/christianwgd/django-bootstrap-icons',
    keywords=['django', 'bootstrap', 'icons', 'templatetags'],
    install_requires=[
        'django',
    ],
)
