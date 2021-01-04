# django-bootstrap-icons

A quick way to add [Bootstrap Icons](https://icons.getbootstrap.com) with Django template tags.

This package contains Bootstrap Icons v1.2.2 (Jan 2021). 

The icons are embedded from the icon font. If you'd rather like to use the svg images try this one: [django_bs_icons](https://github.com/mattburlage/django_bs_icons). 

## Installing

`django-bootstrap-icons` can be found on pypi. Run `pip install django-bootstrap-icons` to install the package on your machine.

## Getting Started

Using django-bootstrap-icons is easy. First, install the `django_material_icons` Django app in your settings file.

```
INSTALLED_APPS = [
    'django_bootstrap_icons'
]
```

Also, include the following tags in your base template file. It includes the CDN link to the bootstrap icons web font. If you have your own source for the web font, feel free to opt out of this tag!
```
{% load django_bootstrap_icons %}

{% include_bootstrap_icons %}
```

Then, add an icon with the following tag. Give the name icon's name as the first parameter, and that's all that's required.
```
{% load django_bootstrap_icons %}

{% bs_icon 'alarm' %}
```

### Icon styling

To style the icons, you can add extra css classes:

```
{% bs_icon 'alarm' extra_classes='your-class-name' %}
```

Sizing classes are included in the bootstrap icon css:

![Icon sizes](https://github.com/christianwgd/django-bootstrap-icons/blob/master/django_bootstrap_icons/static/img/icon-sizes.png "Icon sizes")

```
{% bs_icon 'alarm' extra_classes='bi-xs' %}
{% bs_icon 'alarm' extra_classes='bi-sm' %}
{% bs_icon 'alarm' extra_classes='bi-2x' %}
{% bs_icon 'alarm' extra_classes='bi-3x' %}
{% bs_icon 'alarm' extra_classes='bi-5x' %}
{% bs_icon 'alarm' extra_classes='bi-7x' %}
{% bs_icon 'alarm' extra_classes='bi-10x' %}
```

If you have bootstrap css included, you can use the bootstrap color classes:

![Icon colors](https://github.com/christianwgd/django-bootstrap-icons/blob/master/django_bootstrap_icons/static/img/icon-colors.png "Icon colors")

```
{% bs_icon 'alarm' extra_classes='text-success' %}
{% bs_icon 'alarm' extra_classes='text-info' %}
{% bs_icon 'alarm' extra_classes='text-warning' %}
{% bs_icon 'alarm' extra_classes='text-danger' %}
{% bs_icon 'alarm' extra_classes='text-primary' %}
{% bs_icon 'alarm' extra_classes='text-secondary' %}
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/christianwgd/django-bootstrap-icons/blob/master/LICENSE) file for details

## Acknowledgments

* Thanks bootstrap Icons!
* Thanks to **Doug Dresser** [dwdresser](https://github.com/dwdresser) for the django_material_icon app that i used as a template
