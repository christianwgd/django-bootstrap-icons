import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-bootstrap-icons',
    version='0.6.3',
    packages=setuptools.find_packages(),
    include_package_data=True,
    description='A quick way to add Bootstrap Icons with Django template tags.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Christian Wiegand',
    license='MIT',
    url='https://github.com/christianwgd/django-bootstrap-icons',
    keywords=['django', 'bootstrap', 'icons', 'templatetags'],
    install_requires=[
        'django',
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
