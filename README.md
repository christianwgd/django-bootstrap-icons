# django-bootstrap-icons

![PyPI](https://img.shields.io/pypi/v/django-bootstrap-icons)
![PyPI - Downloads](https://img.shields.io/pypi/dm/django-bootstrap-icons)

A quick way to add [Bootstrap Icons](https://icons.getbootstrap.com) with Django 
template tags.

Embed bootstrap svg icons in your django templates with the possibility for styling 
and sizing.

## Installing

`django-bootstrap-icons` can be found on pypi. Run `pip install django-bootstrap-icons` 
to install the package on your machine.

## Getting Started

Using django-bootstrap-icons is easy. First, install the `django_material_icons` 
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
static directory. SET the BS_ICON_CUSTOM_PATH setting to point to that static directory.

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
BS_ICONS_BASE_URL = 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/'
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
MD_ICONS_BASE_URL = 'https://cdn.jsdelivr.net/npm/@mdi/svg@5.9.55/'
```

You can change it to your desired location by overriding this setting.        

## Example App

There's an [Example App](https://github.com/christianwgd/django-bootstrap-icons-sample) 
that shows how django bootstrap icons work on GitHub

Output of the example app:
![example](https://github.com/christianwgd/django-bootstrap-icons/blob/master/sample-app-result.png "Sample App Output")


## License

This project is licensed under the MIT License - see the 
[LICENSE](https://github.com/christianwgd/django-bootstrap-icons/blob/master/LICENCE) file for details

## Acknowledgments

* Thanks to [Bootstrap Icons](https://icons.getbootstrap.com)!
* Thanks to [Material Design Icons](https://google.github.io/material-design-icons/)!

## Releases

* django-bootstrap-icons 0.5.0 (April 2021): Refactor to use bootstrap svg icons from CDN
* django-bootstrap-icons 0.5.1 (April 2021): Fix incorrect template tag names in documentation
* django-bootstrap-icons 0.5.2 (April 2021): Handle error if custom icon svg does not exist
* django-bootstrap-icons 0.5.3 (April 2021): Add css to specify vertical alignment of sgv icons
* django-bootstrap-icons 0.5.4 (April 2021): Fix some documentation issues, no need to install 
  since it affects only documentation
* django-bootstrap-icons 0.5.5 (April 2021): Add support for Material Design Icons, no need to install 
  as long as you don't want to use MDI.

## Migration

If you had installed an earlier version of this package, you have to change some things:

* Please remove the *include_bootstrap_icons* template tag, 
  since this is no longer needed.

* Change the name of the loading tag from 
  *django_bootstrap_icons* to *bootstrap_icons*.