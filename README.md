# Task Manager

This walkthrough project is built with:     
* Flask
* SQLAlchemy ORM
* Materialize (frontend framework - www.materializecss.com)

## Requirements:
1. `pip3 install Flask-SQLAlchemy psycopg2`
    * Flask-SQLAlchemy comes with both Flask and SQLAlchemy requirements in one download
    * psycopg2 - inorder to work with Postgres databases
2. `touch env.py`
    * env.py - where we store sensitive data that needs to be hidden
    * Be sure to have **.gitignore** file that contains any file and folders that should be ignored by GitHub (eg, env.py)
3. `# noqa` - means 'No Quality Assurance' - to stop the linting warnings that are not technically accurate


## To Create Postgres Database:
1. In the terminal, type `psql`     
    * If error occurs, try `set_pg`
2. `CREATE DATABASE taskmanager;` --> taskmanager is the name of the database
3. Connect to the database created by typing: `\c taskmanager`  
4. Exit from the db CLI by typing: `\q`


## To Generate and Migrate the Models into the New Database
Important: If you were to modify your models later, then you'll need to migrate these changes each time the file is updated with new context.   
1. In the terminal, access the Python interpreter by typing: `python3`
2. Import the 'db' variable found within the taskmanager package: `from taskmanager import db`  
3. `db.create()`       
(Our Postgres database should be populated with these two tables and their respective columns and relationships.)
4. Now, exit the Python interpreter: `exit()`


## To RUN the Application
1. `python3 run.py`