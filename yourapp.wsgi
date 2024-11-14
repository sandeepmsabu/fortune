#!/usr/bin/python3

import sys
import os

# Add the Flask application directory to the sys.path
sys.path.insert(0, '/home/sandeepms/pythonProject')

# Activate the virtual environment (optional but recommended if you're using one)
activate_this = '/home/sandeepms/pythonProject/venv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

# Import the Flask application from app.py (assuming your Flask app is called "app")
from app import app as application

