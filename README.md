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

    > env.py shoud include:     
        import os
        
        os.environ.setdefault("IP", "VALUE")    
        os.environ.setdefault("PORT", "VALUE")  
        os.environ.setdefault("SECRET_KEY", "VALUE")    
        os.environ.setdefault("DEBUG", "VALUE") 
        os.environ.setdefault("DEVELOPMENT", "VALUE")   
        os.environ.setdefault("DB_URL", "VALUE")       

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

## To Deploy Project to Heroku
1. To check all installed packages in the terminal:
    > `pip3 list`
2. Creates requirements.txt with all installed packages
    > `pip3 freeze --local > requirements`
3. Create a Procfile --> what Heroku looks for to know which file runs the app, and how to run it   
    > `echo web: python run.py > Procfile`      

   (Make sure that the file starts with a capital 'P', and has no file extension. You should see the Heroku logo icon once that's created.)     
   (Using the echo command can sometimes add a blank line at the bottom of the file, and this can cause problems when running our app on Heroku, **so just delete that line and save the file.**)

4. In Heroku, add your app as New App.
5. Create a new database that Heroku can host:      
    A. Go to 'Resources' tab    
    B. Under the "Add-ons" section, search for "Heroku Postgres"
    C. Choose a Plan (eg, Hobby Dev)

6. Click on "Settings", and scroll to "Config Vars"     
    (**Config Vars** are the same as Environment Variables, which contain confidential key-value pairs)
7. Click on "**Reveal Config Vars**"    
    * Our new Postgres database URL will be automatically applied (and is being hosted on Amazon AWS)
    * When we created our environment variables, we assigned a variable of "DB_URL". (Please note, if you are using our recommended workspace environment, it actually comes with
a variable of "DATABASE_URL" behind the scenes, which we cannot override.) This is how you can easily distinguish between the two databases.    
    "DB_URL" is for our local database when working in the IDE workspace, whereas "DATABASE_URL" is the assigned Postgres database on our deployed app within Heroku. They are two completely separate databases.       

    Add the following in the HEROKU **CONFIG VARS**:    
    a. IP - <VALUE>     
    b. PORT - <VALUE>     
    c. SECRET_KEY - <VALUE>     
    d. DEBUG - <VALUE> (Should be 'False' when in production mode)

8. Deploy the app using either Heroku CLI or GitHub.    

9. Create the database in Heroku:   
    A. Go to 'MORE' tab.
    B. Click on 'Run Console'.
    C. In the console, type the following:      
    > python3   
    > from taskmanager import db    
    > db.create_all()       
    > exit()    

    (Remember, if you make any changes to your models anytime during development once deployed to Heroku, you will need to make these migrations once again in this Heroku console.)

### Resources:
* [Python strftime cheatsheet](https://strftime.org/)
* [Built-in Jinja Filters](https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters)

### Notes:  
* Convert database queries into Python lists.   
> Whenever you query the database, you get a **Cursor Object** (aka 'QuerySet').
In some cases, you can't use a Cursor Object on the front-end, or with some of the Jinja template filters.
Oftentimes, it's actually better to convert your queries into Python lists.     
> Example: `list(Task.query.order_by(Task.id).all())`   

* If you recall, we created a relationship between our Category and Task models, using a `'backref'` and the `'ondelete' cascade`.
Once the `backref` and `ondelete cascade` are added, it will perform a cascade effect and delete any task utilizing the category.