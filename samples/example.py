from odooapiclient.client import Client


client = Client(host='andriisem.odoo.com', dbname='andriisem', ssl=True)
client.authenticate(login=' ', pwd=' ')
print(client._uid)
