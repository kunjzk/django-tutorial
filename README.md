## Django tutorial

Learning from scratch, following: https://docs.djangoproject.com/en/5.2/intro/tutorial01/

# Notes

## Creating a new endpoint

1. Create the view (business logic function. Input is request, returns a HttpResponse)
2. Add the view to app-level routing in urls.py
3. "Wire up" the app-level routes to the project level ones in project-level urls.py.

## Creating SQL tables

1. Create your model in the app. Table name -> class name. Column -> class variable.
2. Add app config to project level INSTALLED_APPS in settings.py
3. `python manage.py makemigrations <app_name>` -> generates a python migrations file
4. `python manage.py migrate`. There are commands to view the raw SQL too.
5. Locally your db is SQLite, (guessing) same API as postgres but all data is persisted to a local file, `db.sqlite3`.

Extra stuff

- Methods can be added to models. a particularly useful one is `__str__`, returning a string representation of each "object" or row of data. Methods can run any custom logic and return any data. We don't need to make migrations after adding methods, since we're not changing anything in the database.

## manage.py shell

1. Runs a python shell with django environment variables, and auto-imports models from INSTALLED_APPS.
2. Can be used to perform CRUD operations & complex filtering on DB objects via the ORM. This is the database API - really powerful, very complicated.

## Admin

1. For site managers to add/edit content that is viewed on the public site. Super useful!
