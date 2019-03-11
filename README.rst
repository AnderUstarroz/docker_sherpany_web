
Build the project
-----------------

+ Checkout the project:

  ``git clone git@github.com:AnderUstarroz/docker_sherpany_web.git docker_sherpany_web``
+ Go to the Root folder:

  ``cd docker_sherpany_web``
+ Build Docker containers (I assume you have docker installed):

  ``docker-compose up -d``
+ Run database migrations:

  ``docker-compose exec web python manage.py migrate``
+ Collect static assets to improve styles a bit:

  ``docker-compose exec web python manage.py collectstatic --noinput``

The port 8000 will be exposed for testing the application.
By now you should by able to access the app in any of the following addresses:

- http://localhost:8000/
- http://127.0.0.1:8000/

Run the tests
-------------
For running the tests (Note.- Containers must be running):

``docker-compose exec web pytest``

Tear down the project
---------------------
When you are finished run the following command to clean up your machine, destroying all docker containers,
networks and volumes:

  ``docker-compose down -v``

