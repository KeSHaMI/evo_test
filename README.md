# evo_test
File storage with limited time on server.

# Backend
I used DjangoRestFramework to make API for the app and render some pages. 
For delayed tasks(deletion from the server) i used Celery + Redis.

# Frontend
I used css and js from an AJAX tutorial(fetch API) and spend a lot of time formating dates(haven't work with js previously) and sending file via request.

# Deploy
App deployed on heroku using it's Redis server and PostgreSQL database
