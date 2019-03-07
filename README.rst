
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
+ Collect static assets to improve stiles a bit:

  ``docker-compose exec web python manage.py collectstatic --noinput``

Run the tests
-------------
Fur running the tests (Note.- Containers must be running):

``docker-compose exec web pytest``

Tear down the project
---------------------
When you are finished run the following command to destroy all docker containers,
networks and volumes:

  ``docker-compose down -v``

