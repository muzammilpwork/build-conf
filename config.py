import configparser



odoo_app_config_path = './debian/odoo.conf'
config = configparser.ConfigParser()
config.read(odoo_app_config_path)

admin_passwd = config.get('options', 'admin_passwd')
config = configparser.ConfigParser()


# config['options'] = {
#     'db_host': '18.130.231.81',
#     'db_port': '31000',
#     'db_user': 'odoo',
#     'db_password': 'odoo',
#     'addons_path': '/opt/odoo/addons',
#     'admin_passwd': str(admin_passwd)
# }
config['options'] = {
    'db_host': 'postgres-service',
    'db_port': '5432',
    'db_user': 'odoo',
    'db_password': 'odoo',
    'addons_path': '/opt/odoo/addons',
    'admin_passwd': str(admin_passwd),
    'xmlrpc_port': '8070'
}


with open("./config/odoo.conf", 'w') as configfile:
    config.write(configfile)

