# Django Auth

Make sure you
  1. Have run `python manage.py migrate`
  2. Also run `python manage.py createsuperuser` to create a user with the username & password both set to "admin".

Run `http-server` (or whatever) inside of the `static/` folder. Click the three buttons in order to access the protected route.

Your front-end server should be running at `localhost` and not `127.0.0.1` or else you will get cross-origin errors!


