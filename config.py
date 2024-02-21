import configparser
import os


serive_name = os.environ['DB_SERVICE_NAME']
# db_name = os.environ['DB_NAME']
# without_demo = os.environ['WITHOUT_DEMO']

# odoo_app_config_path = './debian/odoo.conf'
# config = configparser.ConfigParser()
# config.read(odoo_app_config_path)

# admin_passwd = config.get('options', 'admin_passwd')
config = configparser.ConfigParser()


config['options'] = {
    # 'without_demo': str(without_demo),
    'without_demo': 'True',
    'admin_passwd': 'abctest123',
    'db_host': str(serive_name),
    'db_port': '5432',
    'db_user': 'odoo',
    'db_password': 'odoo',
    # 'db_name': str(db_name),
    'db_name': 'noman123',
    'addons_path': '/mnt/extra-addons/custom-addons',
    'data_dir': '/var/lib/odoo',
    'list_db': 'True',
}


with open("./config/odoo.conf", 'w') as configfile:
    config.write(configfile)

