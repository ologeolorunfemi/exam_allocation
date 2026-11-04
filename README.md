# exam_allocation
A web app to allocate exam halls to students automatically based on hall capacity.
## Features
- add halls and courses
- add students
- auto-allocate halls by capacity
- view allocation by hall/course
- Admin panel to manage everything

## Tech used
- python/django
- html, css
- SQLite
- gunicorn + whitenoise

## Live demo
https://exam-allocation.onrender.com/exam/

## Run locally
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Admin
/admin/
