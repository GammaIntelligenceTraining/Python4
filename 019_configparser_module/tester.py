from configparser import ConfigParser

config = ConfigParser()
config.read('new_config.ini')
#
# config.add_section('NEWLOGIN')
# config.set('NEWLOGIN', 'login', 'my_new_login')
# config.set('NEWLOGIN', 'pass', 'my_new_pass')
#
# print(config['NEWLOGIN']['login'])
#
# with open('new_config.ini', 'w', encoding='utf8') as new_config_file:
#     config.write(new_config_file)

