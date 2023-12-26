import configparser

odoo_app_config_path = './debian/odoo.conf'
config = configparser.ConfigParser()
config.read(odoo_app_config_path)

admin_passwd = config.get('options', 'admin_passwd')
config = configparser.ConfigParser()


config['options'] = {
    'db_host': '18.133.120.91',
    'db_port': '31002',
    'db_user': 'odoo',
    'db_password': 'odoo',
    'addons_path': '/opt/odoo/addons',
    'admin_passwd': str(admin_passwd)
}


with open("./config/odoo.conf", 'w') as configfile:
    config.write(configfile)

