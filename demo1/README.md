# Getting Started

## Build and launch container

First build and launch the docker container:

```console
$ docker-compose build
...
$ docker-compose run web
demo@2d6ea8e808b0:/code$
```

## Bootstrapping

Bootstrap your new Invenio module:

```console
$ cookiecutter https://github.com/inveniosoftware/cookiecutter-invenio-module.git
...
$ ls -la
...
drwxr-xr-x  1 demo staff  884 Oct 14 09:31 invenio-fungenerator
...
```

Now, take a look at Invenio-Fungenerator:

```console
$ ls -la
...
drwxr-xr-x  1 demo staff  884 Oct 14 09:31 invenio-fungenerator
...
$ cd invenio-fungenerator/
$ find .
.
./.dockerignore
./.editorconfig
./.gitignore
./.travis.yml
./.tx
./.tx/config
./AUTHORS.rst
./babel.ini
./CHANGES.rst
./CONTRIBUTING.rst
./docs
./docs/api.rst
./docs/authors.rst
./docs/changes.rst
./docs/conf.py
./docs/contributing.rst
./docs/index.rst
./docs/installation.rst
./docs/license.rst
./docs/make.bat
./docs/Makefile
./docs/usage.rst
./examples
./examples/app.py
./INSTALL.rst
./invenio_fungenerator
./invenio_fungenerator/__init__.py
./invenio_fungenerator/ext.py
./invenio_fungenerator/templates
./invenio_fungenerator/templates/invenio_fungenerator
./invenio_fungenerator/templates/invenio_fungenerator/base.html
./invenio_fungenerator/templates/invenio_fungenerator/index.html
./invenio_fungenerator/version.py
./invenio_fungenerator/views.py
./LICENSE
./MANIFEST.in
./misc
./misc/header.py
./misc/header.rst
./pytest.ini
./README.rst
./RELEASE-NOTES.rst
./requirements-devel.txt
./run-tests.sh
./setup.cfg
./setup.py
./tests
./tests/conftest.py
./tests/test_invenio_fungenerator.py
```

What's in the box:

- Python package
- Tests
- Internationalization
- Documentation template
- Example code
    - Invenio module
    - Basic view
    - Templates
    - I18N

# Starting development

Initialize git, add files, install dependencies and update MANIFEST:

```console
$ git init
$ git add -A
$ pip install -e .[all]
$ check-manifest -u
```

Run all tests:

```console
$ ./run-tests.sh
...
```

Run Python only tests:

```console
$ python setup.py test
running test
running egg_info
writing requirements to invenio_fungenerator.egg-info/requires.txt
writing top-level names to invenio_fungenerator.egg-info/top_level.txt
writing dependency_links to invenio_fungenerator.egg-info/dependency_links.txt
writing invenio_fungenerator.egg-info/PKG-INFO
reading manifest file 'invenio_fungenerator.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'invenio_fungenerator.egg-info/SOURCES.txt'
running build_ext
========================================================= test session starts =========================================================
platform linux -- Python 3.5.0, pytest-2.8.2, py-1.4.30, pluggy-0.3.1
rootdir: /code/invenio-fungenerator, inifile: pytest.ini
plugins: pep8-1.0.6, cov-2.2.0
collected 12 items

setup.py .
examples/app.py .
invenio_fungenerator/__init__.py .
invenio_fungenerator/ext.py .
invenio_fungenerator/version.py .
invenio_fungenerator/views.py .
misc/header.py .
tests/conftest.py .
tests/test_invenio_fungenerator.py ....
------------------------------------------- coverage: platform linux, python 3.5.0-final-0 --------------------------------------------
Name                                                             Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------------------------
invenio_fungenerator/__init__.py                                     5      0   100%
invenio_fungenerator/ext.py                                         15      0   100%
invenio_fungenerator/version.py                                      3      0   100%
invenio_fungenerator/views.py                                        7      0   100%
----------------------------------------------------------------------------------------------
TOTAL                                                               30      0   100%

====================================================== 12 passed in 0.41 seconds ======================================================
```


Build and view the documentation:

```console
$ python setup.py build_sphinx
...
$ open docs/_build/html/index.html
```

Create message catalogs:

```console
$ mkdir invenio_fungenerator/translations
$ python setup.py extract_messages
$ python setup.py init_catalog -l da
$ python setup.py compile_catalog
```

Inspect and commit changes:

```console
$ git config --global user.email "lars.holm.nielsen@cern.ch"
$ git config --global user.name "Lars Holm Nielsen"
$ git status
$ git add MANIFEST.in
$ git add invenio_fungenerator/translations/
$ git commit
```

Push changes to GitHub:

```console
$ git remote add origin https://github.com/lnielsen/invenio-fungenerator.git
$ git push origin master
```

Make a small change and push to GitHub:

```console
$ git checkout -b smallchange
# Make change
$ git add -A
$ git commit
$ git push origin smallchange
```

Make a pull request:

- Go to https://github.com/lnielsen/invenio-fungenerator
- Click "Compare & pull request"
- Example: https://github.com/lnielsen/invenio-fungenerator/pull/1
- TravisCI: https://travis-ci.org/lnielsen/invenio-fungenerator/builds/85300610

Test Matrix:

- Python version: 2.7, 3.3, 3.4, 3.5
- Dependencies: Lowest, Release, Devel
- (Database: SQLite, MySQL, PostgreSQL)

Push translation catalogs to Transifex:

- Example: https://www.transifex.com/zenodo/invenio-fungenerator/translate/#da/messagespot/63792780


# Developing

Launch the included example application:

```console
$ cd examples/
$ flask -a app.py run -h 0.0.0.0
```
