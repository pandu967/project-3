# project-3
This project is all about log analysis from the given sql file.
various things inculcated: vahrant,virtual box,psql
Working:
	By using the terminal we execute the python file which we write. 
	With this whatever the data we need will be displayed in the terminal.
	To display those data,we write various queries.
Process:
	Download newsdata.sql file.
	It is a zip file.
	Extract it and place it in the current working directory. 
	First we install vagrant and virtual box with following commands.
		i) sudo apt-get install virtualbox
		ii) sudo apt-get install vagrant
	Setting up the environment required.
		iii) vagrant up - Launching the virtual machine
		iv) vagrant ssh 
		Change directory to /vagrant and look around with ls.
		Load the data in local database using the command:
		psql -d news -f newsdata.sql
This newsdata.sql file consists of
	The authors table includes information about the authors of articles.
	The articles table includes the articles themselves.
	The log table includes one entry for each time a user has accessed the site.
Use \c news to connect to database.
running python file:
	python log.py



		 
