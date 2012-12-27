import sys
sys.path.insert(0, '/var/www/weblog')
activate_this = '/var/www/weblog/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from hello import app as application
