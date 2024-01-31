#!/usr/bin/python3
import os

# Set Flask app and debug mode
os.environ['FLASK_APP'] = 'api.app'
os.environ['FLASK_DEBUG'] = '1'

# Run the Flask app
os.system('flask run')

#from main.app import create_app

# Create the Flask app
#app = create_app()

#if __name__ == "__main__":
    # Run the app
 #   app.run()

