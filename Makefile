ifeq ($(findstring Survey,$(shell hostname -f)), Survey)
	ENV = production
endif
all:
	@echo 'run make prod to deploy'

prod:
ifeq ($(ENV), production)
	git fetch && git reset --hard origin/master
	cd masterproject && venv/bin/python manage.py migrate
	cd masterproject && venv/bin/python manage.py collectstatic
	sudo supervisorctl restart survey
	@cd $(shell pwd)
else
	@echo 'Not on server'
endif