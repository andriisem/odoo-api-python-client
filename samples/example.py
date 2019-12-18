from odooapiclient.client import Client


client = Client(host='andriisem.odoo.com', dbname='andriisem', saas=True)
client.authenticate(login='semko.andrey.i@gmail.com', pwd='audi100')
