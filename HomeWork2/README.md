## To run:

Make sure to install all the dependencies (in this case, SQLAlchemy)
To do so (automatically) use the command `pip install -r requirements.txt`

Finally, when the dependencies are installed
Use the main.py file to view the results.

Inside main.py, the db.start(file_path) function initializes the database and returns a session object to perform queries.
You can provide a database file path, if the file doesn't exist it will be created (however the parent directory of the file should exist)

If no file path provided, it will create a (sqlite) file in the current working directory named `db.diners`

## Directory structure

The "test" file is main.py where all the queries are done to view the results

diner package contains 2 modules, namely db.py and models.py

* models.py contains all the models for sqlalchemy. There are 2 models, Provider and Canteen.
* db.py contains all the functions to initalize the database. use db.start() to initalize the database and get a session to perform queries into the database
