from zabbix_api import ZabbixAPI
import configparser

#Get server/login
config = configparser.RawConfigParser()
config.readfp(open("zabbixinfo.conf"))
server = config.get('credentials','server')
login = config.get('credentials','login')
password = config.get('credentials','password')

zapi = ZabbixAPI(server="server")
zapi.login("login", "password")
