from zabbix_api import ZabbixAPI
import configparser

#Get server/login
config = configparser.RawConfigParser()
config.readfp(open("zabbixinfo.conf"))
server = config.get('credentials','server')
login = config.get('credentials','login')
password = config.get('credentials','password')

zapi = ZabbixAPI(server=server)
zapi.login(login, password)

# get the hostId from hostName
def getID(host): 
    hostId = zapi.host.get({"filter": {"host": host}})[0]["hostid"]
    return zapi.item.getObjects({'hostid': hostId})

#Delete !
idtodelete = getID(hostname)
zapi.delete.host( [{"hostid" : int([idtodelete]) }] )
