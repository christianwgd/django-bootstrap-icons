import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-bootstrap-icons',
    version='0.1.0',
    packages=[
        'django_bootstrap_icons',
    ],
    include_package_data=True,
    description='A quick way to add Bootstrap Icons with Django template tags.',
    long_description=long_description,
    author='Christian Wiegand',
    license='MIT',
    url='https://github.com/christianwgd/django-bootstrap-icons',
    keywords=['django', 'bootstrap', 'icons', 'templatetags'],
    install_requires=[
        'django',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
