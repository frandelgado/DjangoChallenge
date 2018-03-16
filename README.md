# Xivis Django Dev Challenge

[Django 2.0](https://www.djangoproject.com/) web application built to challenge new developers.

## Requirements

  * Python 3 or newer

## Getting Started

1. Clone the repo and install dependencies (you may want to create a virtualenv)

````bash
git clone git@github.com:Xivis/django-dev-challenge.git
cd django-dev-challenge
python3 -m venv envname
source envname/bin/activate
pip install -r requirements.txt
````

2. Run migrations, load fixtures, collectstatics & create a superuser
````bash
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata fixtures/tickets.json
python manage.py createsuperuser # then follow instructions
````

3. Run server (default: PORT 8000)

  ````bash
  python manage.py runserver
  ````

## Challenge
### Context
The web application is a simplified version of a ticketing system that handles requests of users.
Each requests has a Service Order Category, that has it's own SLA (Service Level Agreement) in working hours.
When a Service Order is created, the system should calculate the expiry date based on working hours, holidays and weekends.

### What are we waiting
We need you to:
  * Create a welcome page with a list of all the Service Orders that are in progress, showing it's expiry date.
  * Create a form for new Service Orders, calculating at the creation moment the expiry date (try making a reusable service for this)
  * Return to the user requesting the Service Order, the ID of the newly created order and the expiry date.

## Developers

  * [Ramiro Gonzalez](https://github.com/ragonzal)

---

[Xivis](https://www.xivis.com) Copyright © 2018.
