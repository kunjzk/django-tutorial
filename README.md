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
