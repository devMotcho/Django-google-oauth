# Django-google-oauth

This project shows a simple way to add google authentication to your django app, for this you will need a Google Project and the OAuth client credentials to proceed with the authentication and of course python on your machine.

#### Creating a Google Project
---
1. Navigate to https://console.cloud.google.com/
2. Create a Project and Select it
3. Navigate to APIs and Services OAuth consent screen
4. Create a User Type and follow the App registration.
5. Add at least the first 2 Scope Options
6. After that, go to credentials in the APIs & Services menu section and Create Credentials
7. Create OAuth client ID set the Application type to Web application, create the credentials and download the JSON file - don't chare your credentials with anyone.
8. Open the Client ID for Web Application that was created
9. Add the following Authorized redirect URIs for local development:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/accounts/google/login/callback/ 

#### Running this Project
---
1. `pip install -r requirements.txt`
2. `python manage.py makemigrations` 
3. `python manage.py migrate` 
4. `python manage.py createsuperuser`
5. `python manage.py runserver`
6. Even if you get a error navigate to `127.0.0.1:8000/admin`
7. Login and change default instance of Site Model with `http://127.0.0.1:8000` as the domain name and display name
8. Create a social application instance setting the name to google, client id and secret key from the `json` file and adding the localhost sites to the chosen sites. 
