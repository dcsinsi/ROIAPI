#! python3

from xmlrpc.client import ServerProxy

proxy = ServerProxy("https://secure2.roisolutions.net/enterprise/xmlrpc")

id = 'dcsinsi'
pwd = '*******'
client = 'oa'

proxy.Init.logon(id, pwd, client)
