## Prerequisites:
Need Web browser on the machine (Chrome, FireFox, Safari)
Python library needed to run python code. (IDLE, Anaconda)
Steps to install important packages-
$ sudo apt-get update
$ sudo apt-get -y upgrade
$ sudo apt-get install -y python3-pip
$ sudo easy_install sqlalchemy

## Technologies used :
Python 3.5.2
Flask 1.0.2
SQLite 3.0 database
Flask-Sqlalchemy 2.3.2
JSON
HTML
CSS

## Running the Meters Data App
Now type **python database_setup.py** to initialize the database.

Type **python meterdata.py** to populate the database with meters. (Optional)

Type **python meter.py** to run the Flask web server. In your browser visit **http://localhost:5000** to view the Meters Data app.  You should be able to view, all meters on first page.

## Author
Ajinkya Kishor Shinde
