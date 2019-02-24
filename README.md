# Image_Annotator


## About
A simple application to demo an image annotator. [https://image-annotator.herokuapp.com/](https://image-annotator.herokuapp.com/) 
  * For the admin route;
       Username: Tbena   
       Password: 0987654zxas 

## Goal
The goal of this project is to create an app for annotating or drawing bounding boxes on an image.

## Features
  * Create annotation.
  * Edit/Update annotation.
  * Cancel/Delete anotation.
  * Zoom the images.

## Technology stack
Tools used during the development of this API are;

1. Django - a python web framework
2. Django REST Framework - a flexible toolkit to build web APIs
3. SQLite - this is a database server
##### Requirements
          Use Python 3.x.x+  and Django 2.x.x+

## Running the application
To run this application, clone the repository on your local machine and execute the following command.

    $ cd music_service
    $ virtualenv env
    $ source env/bin/activate or env\Scripts\activate -for windows
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
