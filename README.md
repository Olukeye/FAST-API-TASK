# FAST-API-TASK
Assessment task


# Technology Stack:

	  FastAPI
	  bcrypt
	  Uvicorn (server)
	  psycopg2
	  Sqlalchemy
	  Postgres
	  Alembic for migration

# How to start the app ?
*  run py -3 -m venv env  ( to create a virtual environment)
* activate your virtual environment by ".\venv\Scripts\activate.bat"
* pip install -r .\requirements.txt to generate required install packages
* uvicorn main:app --reload --port 4000    #start server
* visit  localhost://127.0.0.1:4000/ on your browser

# Features:
	 Connecting to Database
	 Schemas
	 Dependency Injection such as (get_current_user)
	 Password Hashing
	 Authentication login/create user
	 Authorization and user Permissions
