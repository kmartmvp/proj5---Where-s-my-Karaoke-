import configparser


config = configparser.ConfigParser()                # Create configparser object
config.read('credentials.ini')                      # Open credentials.ini for reading

# Simple dictionary to implement key-value reading of configuration information for app.py
cfg_dict = {
    "PORT": config['DEFAULT']["PORT"],
    "DEBUG": config['DEFAULT']['DEBUG'],
    "SECRET_KEY": config['DEFAULT']['SECRET_KEY'],
    "TOKEN": config['DEFAULT']['TOKEN']
}