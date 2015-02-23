This is a simple python script to delete a zabbix host when an sns nothing is
received.

This is mostly meant for autoregister autoscaling host. (When a instance is
terminated, a SNS have to be send in order to deregister.)

EDIT zabbixinfo.conf 
