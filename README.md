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
