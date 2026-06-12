from db import plsql
from models import User, Message


plsql.connect()

# plsql.create_tables([User])
plsql.create_tables([Message])

plsql.close()

