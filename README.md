# django-bootstrap-icons

![PyPI](https://img.shields.io/pypi/v/django-bootstrap-icons)
![PyPI - Downloads](https://img.shields.io/pypi/dm/django-bootstrap-icons)
[![Django CI run test](https://github.com/christianwgd/django-bootstrap-icons/actions/workflows/django-test.yml/badge.svg)](https://github.com/christianwgd/django-bootstrap-icons/actions/workflows/django-test.yml)

A quick way to add [Bootstrap Icons](https://icons.getbootstrap.com) with Django 
template tags.

Embed bootstrap svg icons in your django templates with the possibility for styling 
and sizing.

## Installing

`django-bootstrap-icons` can be found on pypi. Run `pip install django-bootstrap-icons` 
to install the package on your machine.

## Getting Started

Using django-bootstrap-icons is easy. First, install the `django_bootstrap_icons` 
Django app in your settings file.

```
INSTALLED_APPS = [
    'django_bootstrap_icons'
]
```

Also, load the tag library in your template file:

```
{% load bootstrap_icons %}
```

Then, add an icon with the following tag. Give the name icon's name as the 
first parameter, and that's all that's required.

```
{% bs_icon 'alarm' %}
```

### Icon sizes

You can size the icons by setting the size parameter:

```
{% bs_icon 'alarm' size='1.5em' %}
```

### Icon styling

Set the color of an icon by specifying the color parameter:

```
{% bs_icon 'alarm' color='red' %}
```

For further styling, you can add extra css classes:

```
{% bs_icon 'alarm' extra_classes="your-classname1 your-classname2" %}
```

#### Vertical alignment

By default all sgv bootstrap icons are vertical aligned to the middle. Sometimes this is 
not appropriate, especially when rendering beside text. To align with text *django-bootstrap-icons*
provides some css classes to set the desired vertical alignment. 

Include the css file into your template

```
<link rel="stylesheet" href="{% static 'bootstrap_icons/css/bootstrap_icons.css' %}">
```

and add the class to the *extra_classes* parameter

```
{% bs_icon 'alarm' extra_classes="bi-valign-bottom" %}
```

The following classes are available:

```
.bi-valign-default /* This is a compromise also provided by bootstrap
                     for the icon font. The value is vertical-align: -.125em; 
                     (see https://github.com/twbs/icons/issues/601 for details) */
.bi-valign-middle /* this is the real default, so you may not need it */
.bi-valign-bottom
.bi-valign-text-top
.bi-valign-text-bottom
```
 
### Custom icons
There's a template tag for your custom icons. Store the custom icons in some 
static directory. SET the BS_ICONS_CUSTOM_PATH setting to point to that static directory.

```
{% custom_icon 'your-custom-svg-name' %}
```

The custom template accepts the same parameter as the bootstrap icon template.

In fact you could download the bootstrap icons from bootstrap, store them in 
your static files and use them with the custom_icon template tag. This would 
avoid the use of CDN completely. 

### Material Design Icons

*django-bootstrap-icons* works fine with Material Design Icons. There is a template
tag for MDI:

```
{% md_icon 'alarm' %}
```

Material Design Icons get some additional css classes *mdi* and *mdi-<icon-name>* to 
style them globally.

To use Material Design Icons side-by-side with bootstrap icons *django-bootstrap-icons* 
makes some adjustments in rendering the icons:

* The base size of Material Design Icons is larger than the size of bootstrap icons. 
  For the default size (no size attribute given), *django-bootstrap* icons are resized.
  If you want to have the same size as Bootstrap Icons, set them to a size factor of 1.25.
  If Bootstrap Icon is of size 2em, set Material Icon to 2.5em. (Although the base size 
  in mdi svgs is 24 the real size of the icon is 20 because of some empty space, that
  surrounds the icons).
  
* Because of that empty white space of the MDI (sort of some internal "padding" in svg)
  you need to include the django-bootstrap-icons css file to make some adjustments to 
  the alignment.

```
<link rel="stylesheet" href="{% static 'bootstrap_icons/css/bootstrap_icons.css' %}">
```

## Configuration

You can specify the source from which the icons are loaded:

```
BS_ICONS_BASE_URL = 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/'
```

BS_ICONS_BASE_URL defaults to the latest boostrap-icons CDN that was available 
when releasing this package. Change the URL to use an older or newer one.

To add custom icons to your app you need to set the path where these can be found. 
The default setting is *custom-icons*, so you would add your icons 
to */your-app/static/custom-icons/*.

```
BS_ICONS_CUSTOM_PATH = 'custom-icons'
```

### Configure Material Design Icons

Material Desing Icons are loaded from the default URL:

```
MD_ICONS_BASE_URL = 'https://cdn.jsdelivr.net/npm/@mdi/svg@6.4.95/'
```

You can change it to your desired location by overriding this setting.       

### Configure icon cache

To avoid fetching icons multiple times, configure the icon cache directory:

```
BS_ICONS_CACHE = os.path.join(STATIC_ROOT, 'icon_cache')
```

This will ensure that icons will be loaded only once with their individual svg properties 
and stored to a local file. On each subsequent use the icon will be simply loaded from file.

### Configure icon not found return

In case icons are not found you can configure, what to display:

```
BS_ICONS_NOT_FOUND = f"Icon <{icon_path}> does not exist"
```

This shows the error message if you for example misspelled an icon name.

If you're running your app offline you may want to display some value that has the same size as the icon:

```
BS_ICONS_NOT_FOUND = '<?xml version="1.0" ?>\
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="red" class="bi bi-x-circle" viewBox="0 0 16 16">\
	<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>\
	<path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>\
</svg>'
```

## License

This project is licensed under the MIT License - see the 
[LICENSE](https://github.com/christianwgd/django-bootstrap-icons/blob/master/LICENCE) file for details

## Acknowledgments

* Thanks to [Bootstrap Icons](https://icons.getbootstrap.com)!
* Thanks to [Material Design Icons](https://google.github.io/material-design-icons/)!

## Releases
- see CHANGELOG.md

## Run the sample app
```
git clone https://github.com/christianwgd/django-bootstrap-icons.git
cd django-bootstrap-icons
<create a virtual environment with your preferred tooling (virtualenv/venv/pipenv)
pip install -U -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Output of the example app: 
![example](https://github.com/christianwgd/django-bootstrap-icons/blob/master/sample-app-result.png "Sample App Output")

## Run the tests
Setup the sample app (see above)
```
python manage.py test
```
