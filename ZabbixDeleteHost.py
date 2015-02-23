from zabbix_api import ZabbixAPI
import ConfigParser

#Set server/login
config = ConfigParser.RawConfigParser()
config.readfp(open("zabbixinfo.conf"))

zapi = ZabbixAPI(server="server")
zapi.login("login", "password")
