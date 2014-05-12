PurplePikachu.com
=================

PurplePikachu.com is a Django-powered web site for an upcoming Pokemon fan-game. It is currently being developed by Tanner Evins and Michael Todd.

Dependencies
------------
Since Django is a Python web framework, the deployed site uses [virtualenv](https://pypi.python.org/pypi/virtualenv) and [pip](https://pypi.python.org/pypi/pip) (installed automatically with virtualenv) to manage dependencies. The file `requirements.txt` is produced with the command `pip freeze` and contains all the dependencies of this project.

The important dependencies and their purposes are:
 - [Django](https://www.djangoproject.com/): The web framework that generates the site.
 - [South](http://south.aeracode.org/): Django module to ease data migration.
 - [Fabric](http://www.fabfile.org/): Python SSH application for networked deployment scripts.
