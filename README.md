## CIS322 - Project 5
Simple implementation of a map web application using LeafletJS and Flask.

## Run/Install
Using your own custom credentials.ini file, create one with the following format:
```ini
[DEFAULT]
PORT = <info here>
DEBUG = <info here>
TOKEN = <info here>
SECRET_KEY = <info here>
```
Graders will be provided with my own credentials file through Canvas.

To run, navigate to clone location. To install for the first time, run 
```bash
make install
```
and then 
''' bash
make start
'''
to start Flask server. Use `make stop` to stop the server after pressing ``CNTRL + C`` to exit.

To run without make, navigate to ../mapping and 
```bash
python3 map_server.py
```
However, this requires that you have all necessary modules installed.

## Author Information
Michael Hagel
Email: mhagel@uoregon.edu