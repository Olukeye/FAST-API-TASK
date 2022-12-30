# FAST-API-TASK
Assessment task


# Technology Stack:

	  FastAPI
	  bcrypy
	  Uvicorn (server)
	  Sqlalchemy
	  Postgres
	  Alembic for migration

# How to start the app ?
* git clone https://github.com/nofoobar/JobBoard-Fastapi.git
* cd .\JobBoard-Fastapi\
* py -3 -m venv env   #create a virtual environment
*  activate your virtual environment ".\env\Scripts\activate.bat"
* pip install -r .\requirements.txt
* uvicorn main:app --reload --port 4000    #start server
* visit  localhost://127.0.0.1:4000/ on your browser

# Features:
	✔️ Connecting to Database
	✔️ Schemas
	✔️ Dependency Injection
	✔️ Password Hashing
	✔️ Authentication login/create user/get token
	✔️ Authorization/Permissions
