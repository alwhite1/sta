MANAGE=django-admin.py
SETTINGS=sta.settings

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE)  test  product
	flake8 --exclude '*migrations*' --ignore=E501 apps

loaddata:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) loaddata ./fixtures/data.json