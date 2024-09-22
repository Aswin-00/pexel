
Installation
------------

Follow these steps to get the project up and running.

Step 1: Create a Virtual Environment
------------------------------------
First, create a virtual environment to isolate the project dependencies:

    python -m venv venv

Activate the virtual environment:

- On Windows:
  
    venv\Scripts\activate
  
- On macOS/Linux:
  
    source venv/bin/activate


Step 2: Install Required Modules
--------------------------------
Install the required dependencies using the `requirements.txt` file:

    pip install -r requirements.txt


Step 3: Run Migrations
----------------------
Apply the database migrations by running the following commands:

    python manage.py makemigrations
    python manage.py migrate


Step 4: Start the Development Server
------------------------------------
Run the Django development server:

    python manage.py runserver


Step 5: Create a Superuser
--------------------------
To access the admin panel, create a superuser:

    python manage.py createsuperuser

You can then log in using either your email or username.



**ありがとうございます 😊🎉✨
**
