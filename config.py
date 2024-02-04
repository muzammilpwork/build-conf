import configparser
import os


serive_name = os.environ['DB_SERVICE_NAME']

# odoo_app_config_path = './debian/odoo.conf'
# config = configparser.ConfigParser()
# config.read(odoo_app_config_path)

# admin_passwd = config.get('options', 'admin_passwd')
config = configparser.ConfigParser()


config['options'] = {
    'without_demo': 'True',
    'admin_passwd': 'abctest123',
    'db_host': str(serive_name),
    'db_port': '5432',
    'db_user': 'odoo',
    'db_password': 'odoo',
    'db_name': 'noman123',
    'addons_path': '/mnt/extra-addons/custom-addons',
    'data_dir': '/opt/odoo',
}


with open("./config/odoo.conf", 'w') as configfile:
    config.write(configfile)

