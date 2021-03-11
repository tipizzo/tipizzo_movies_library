# tipizzo_movies_library
Tipizzo_movies_library is a simple web application built with Django Frmawork
How to setup this project:

First, Download the zip or clone it from your Desktop github
then,
cd movie_library
movie_library>env\Scripts\active
pip install Django
pip install psycopg2(This will allow you to use Postgresql database)
Create database named "django_db"
still in movie_library>py manage.py makemigrations
movie_library>py manage.py migrate

run: movie_library>py manage.py createsuperuser (Then follow steps)


Congratulations 🎉

Fatality: movie_library>py manage.py runserver
