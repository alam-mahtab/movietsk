This Task is 
""" 
Create Django Movie project which should be serve REST APIs as below with CRUD details,
Create Movie with Name, Description, Date of release
    Request Method : POST
    Request Body : JSON
    Response : return movie and its id in json format
Update Movie name/description/date
    URL Params id : required
    Request Method : PUT
    Request Body : JSON
    Response : return movie and its id in json format
Delete Movie using id of movie name
    URL Params id : required
    Request Method : DELETE
    Response : return movie and its id in json format
Get Movie details
    Request Method : GET
    URL Params id : optional
    With id return only a movie details
    If id is not available then return all movies with list in response
Note: 
Give exception if id is not passing in request in PUT/DELETE/GET request and id not found while id is given invalid
After creating this APIs Write some unit test cases for these APIs as many as possible """

My Approach for this task is:
1. Launch django Project using "django-admin startproject movietask"
2. Create an App inside project using "python manage.py startapp api"
3. Register app and rest_framework in installed_app's section in settings.py and also make some required changes there.
4. Create a model named MOvie in 'api/model.py'
5. Then Serialized the model created in 'api/serializers.py'
6. Create view function to serve RESTApi in 'api/views.py'
7. Configure urls in 'api/urls.py' and in 'movietask/urls.py'
8. Delete 'api/test.py' and Create a folder named test and inside it create [__init__.py,test_setup.py,test_views.py]
9. Write test cases

After Cloning it run the following commands:
1. python manage.py makemigrations
2. python manage.py migrate if  throwing no such table: api_movie error run ['python manage.py migrate --run-syncdb']
3. python manage.py createsuperuser [to create admin][Optional]
4. python manage.py runserver
5. python manage.py test  [for testing]

Question from my side:
As This line """If id is not available then return all movies with list in response """
is not very clear that which id you are talking about, 

if it is the id in query params:
    this work is done

elif it is the id in db:
    uncomment line 81-83 and comment line 84
