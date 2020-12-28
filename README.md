# Data-Representation-Project
## Maura Hurley

Lecturer:  Andrew Beatty

This repository contains my project submission for Data Representation 2020

### About the Database
The shares database provides up to date prices for individuals 

The 'Shares' table contains the following fields:

- id (Primary key)
- symbol
- name
- price
    
### The Database contains the following files:

- SharesyDao.py enables CRUD operations to be performed on the SQL Database.
- Basic login screen
- login configuration - 'dbconfig.py'
- Flask Server - server.py


### Create a virtual environment as follow:

On the CLI open the directory where the files are saved.  Run the following:

-  .\venv\Scripts\activate.bat
- set FLASK_APP=server
- set FLASK_ENV=development
- flask run


Open browser and paste the following:

http://127.0.0.1:5000/login.html.

This directs you to a login page.  The login credentials are as follows:

Username: root
Password: root.

Once logged in you will be directed to the latest share prices in your portfolio.