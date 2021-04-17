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
{% custom_icon 'your-custom-svg-name' %}
```


### Custom icons
There's a template tag for your custom icons. Store the custom icons in some 
static directory. SET the BS_ICON_CUSTOM_PATH setting to point to that static directory.

```
{% bs_icon 'alarm' extra_classes='your-class-name' %}
```

The custom template accepts the same parameter as the bootstrap icon template.

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

## Example App

There's an [Example App](https://github.com/christianwgd/django-bootstrap-icons-sample) 
that shows how django bootstrap icons work on GitHub

Output of the example app:
![example](https://github.com/christianwgd/django-bootstrap-icons/blob/master/sample-app-result.png "Sample App Output")


## License

This project is licensed under the MIT License - see the 
[LICENSE](https://github.com/christianwgd/django-bootstrap-icons/blob/master/LICENCE) file for details

## Acknowledgments

* Thanks to [bootstrap Icons](https://icons.getbootstrap.com)!

## Releases

* django-bootstrap-icons 0.5.0 (April 2021): Refactor to use bootstrap svg icons from CDN
* django-bootstrap-icons 0.5.1 (April 2021): Fix incorrect template tag names in documentation
* django-bootstrap-icons 0.5.2 (April 2021): Handle error if custom icon svg does not exist

## Migration

If you had installed an earlier version of this package, you have to change some things:

* Please remove the *include_bootstrap_icons* template tag, 
  since this is no longer needed.

* Change the name of the loading tag from 
  *django_bootstrap_icons* to *bootstrap_icons*.