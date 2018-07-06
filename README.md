## Log Analysis
This project is all about Log analysis which is apart of FULL STACK WEB DEVELOPMENT COURSE in UDACITY
## Project Requirements
	Python3
   Vagrant
   VirtualBox
   psycopg2
## Environment Setup
	Install vagrant and virtualBox with following command:
		sudo apt-get install vagrant
		sudo apt-get install virtualbox
	To install python:
		sudo apt-get install python
	Download or clone fullstack-nanodegree-vm repository.
	Download the data from the cloned one.
	Unzip / extract the file.
	This contains newsdata.sql file.

## Launching the Virtual Machine:
    Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
		$ vagrant up
	Log into this using the following command:
		$ vagrant ssh
	Change the directory to /vagrant with the below command and later check with 'ls' command
		$ cd /vagrant
## Setting up the database:
	Load the data using the command below:
		$ psql -d news  -f newsdata.sql
	The database includes three tables:

    authors table - information about the authors of articles.
    articles table - articles 
    log table - one entry for each time a user has accessed the site.

## Connecting to database
	After making sure that everything went in a correct way give the below comand to connect to database:
		$ \c news
	
## Running python file:
  python3 log1.py
	
