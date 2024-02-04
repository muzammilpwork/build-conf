import configparser
import os


serive_name = os.environ['DB_SERVICE_NAME']

config = configparser.ConfigParser()


config['options'] = {
    'admin_passwd': 'abctest123',
    'db_host': str(serive_name),
    'db_port': '5432',
    'db_user': 'odoo',
    'db_password': 'odoo',
    'addons_path': '/mnt/extra-addons/custom-addons',
    'data_dir': '/opt/odoo',
}


with open("./config/odoo.conf", 'w') as configfile:
    config.write(configfile)
