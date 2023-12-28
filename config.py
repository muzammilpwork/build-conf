import configparser
import os


serive_name = os.environ['DB_SERVICE_NAME']

odoo_app_config_path = './debian/odoo.conf'
config = configparser.ConfigParser()
config.read(odoo_app_config_path)

admin_passwd = config.get('options', 'admin_passwd')
config = configparser.ConfigParser()


config['options'] = {
    'db_host': str(serive_name),
    'db_port': '5432',
    'db_user': 'odoo',
    'db_password': 'odoo',
    'addons_path': '/opt/odoo/addons',
    'admin_passwd': str(admin_passwd)
}


with open("./config/odoo.conf", 'w') as configfile:
    config.write(configfile)

