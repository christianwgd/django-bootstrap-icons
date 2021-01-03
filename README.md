# django-bootstrap-icons

A quick way to add [Bootstrap Icons](https://icons.getbootstrap.com) with Django template tags.

This package contains Bootstrap Icons v1.2.2 (Jan 2021).

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

## Contributing

Please read [CONTRIBUTING.md](https://github.com/christianwgd/django-bootstrap-icons/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Christian Wiegand** - *Creator* - [christianwgd](https://github.com/christianwgd)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/christianwgd/django-bootstrap-icons/blob/master/LICENSE) file for details

## Acknowledgments

* Thanks bootstrap Icons!
* Thanks to **Doug Dresser** [dwdresser](https://github.com/dwdresser) for the django_material_icon app that i used as a template
