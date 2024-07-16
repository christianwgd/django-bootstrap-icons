# Change Log

<!-- GENERATOR_PLACEHOLDER -->

## [0.9.0](https://github.com/christianwgd/django-bootstrap-icons/compare/0.8.7...v0.9.0) (2024-07-16)


### Features

* Add BS_ICONS_BASE_PATH and MD_ICONS_BASE_PATH to use local copies of icon sets. ([#26](https://github.com/christianwgd/django-bootstrap-icons/issues/26)) ([021664a](https://github.com/christianwgd/django-bootstrap-icons/commit/021664adabb203cf851041b23f334efe0d406f4d))
* Add BS_ICONS_BASE_PATH and MD_ICONS_BASE_PATH to use local copies of icon sets. ([#26](https://github.com/christianwgd/django-bootstrap-icons/issues/26)) ([344960e](https://github.com/christianwgd/django-bootstrap-icons/commit/344960e51a1b4f48712a10d732b87693125eddc3))

## 0.8.7

### Changed
- Support Django 5: Remove deprecation warning for format_html
- Update default Bootstrap Icons CDN to version 1.11.2

## 0.8.6

### Changed
- Change from pylint to ruff
- Address vulnerability in xml.minidom by using defusedxml
- Increase test coverage

## 0.8.5

### Changed
- Update default Bootstrap Icons CDN to version 1.11.1

## 0.8.4

### Changed
- Update default Bootstrap Icons CDN to version 1.11.0
- Update requirements for sample app

## 0.8.3

### Changed
- Update default Bootstrap Icons CDN to version 1.10.4
- Update default Material Icons CDN to 7.2.96
- Switch to pytest for testing

## 0.8.2

### Changed
- Update default Bootstrap Icons CDN to version 1.10.2
- Update default Material Icons CDN to 7.0.96

## 0.8.1

### Fixed
- Vertical alignment couldn't be set by extra_classes

## 0.8.0

### Changed
- Update default Bootstrap Icons CDN to version 1.9.0
- Update default Material Icons CDN to 6.9.96

### Fixed
- Set alignment to default if no class is provided for bi and mdi icons

## 0.7.9

- Update default Bootstrap Icons CDN to version 1.8.2
- Update default Material Icons CDN to 6.6.96

## 0.7.8

- Fix default alingment of icons from -0.125em to rem 

## 0.7.7

- Update default bootstrap icons CDN to version 1.8.1

## 0.7.6

- Update default bootstrap icons CDN to version 1.8.0

## 0.7.5

### Changed
- Include sample app in repository
- Added basic tests
- Moved release information to CHANGELOG.md

### Fixed
- Replace blanks in cache file names with underscores

## 0.7.4

### Updated
- Update default bootstrap icons CDN to version 1.7.2

## 0.7.3

### Updated
- Update default bootstrap icons CDN to version 1.7.1

## 0.7.2

### Updated
- Update default bootstrap icons CDN to version 1.7.0, update default Material Icons CDN to 6.4.95

## 0.7.1

### Updated
- Update default bootstrap icons CDN to bugfix version 1.6.1

## 0.7.0

### Updated
- Update default bootstrap icons CDN to version 1.6.0

## 0.6.4 

### Changed
- Improve error handling for custom icons

## 0.6.3

### Changed
- Add a configuration option what to display if icons are not found.

## 0.6.2

### Changed
- Add icon cache to avoid multiple redering of same icon ([#5](https://github.com/christianwgd/django-bootstrap-icons/issues/5))

## 0.6.1

### Fixed
- Fix path building on windows ([#3](https://github.com/christianwgd/django-bootstrap-icons/issues/3))

## 0.6.0

### Updated
- Update default bootstrap icons CDN to version 1.5.0

## 0.5.5

### Changed
- Add support for Material Design Icons, no need to install as long as you don't want to use MDI.

## 0.5.4

### Fixed
- Fix some documentation issues, no need to install since it affects only documentation

## 0.5.3

### Changed
- Add css to specify vertical alignment of sgv icons

## 0.5.2

### Fixed
- Handle error if custom icon svg does not exist


## 0.5.1

### Fixed
- Fix incorrect template tag names in documentation ([#3494](https://github.com/cookiecutter/cookiecutter-django/pull/3494))

## 0.5.0

### Changed
- Refactor to use bootstrap svg icons from CDN
