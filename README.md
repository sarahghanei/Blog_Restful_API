**Blog API Backend
**

A REST API for blog built using Django Rest Framework
Installation
Requirements

    Python

    Django

    Complete list available in requirements.txt file

**Quickstart**

    Clone the repo.

    git clone https://github.com/ExpressHermes/Blog-API.git

    Inside the backend folder, make a virtual environment and activate it

    cd Blog-API/backend
    python -m venv env 
    source env/bin/activate

    Install requirements from requirements.txt

    pip install -r requirements.txt

    Makemigrations and migrate the project

    python manage.py makemigrations && python manage.py migrate

    Create a superuser

    python manage.py createsuperuser

    Runserver

    python manage.py runserver

Note: After running the server, you can use the api inside browser or you can use Postman to make api calls. Make sure in each api call, you provide username, password by creating a user.
