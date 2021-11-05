# /manage.py
# date created : 28-10-2021
# by : Simran Beig
# Updated on: 02-11-2021

from config.instance import server
from services.book_service import nbook
from services.bookedByStudent_service import nstudent
from services.library import name_space
from namespaces.book_ns import name_space2

# adding namespace for swagger
server.api.add_namespace(name_space2)
server.api.add_namespace(name_space)
server.api.add_namespace(nbook) # created : 28-10-2021
server.api.add_namespace(nstudent) # updated on : 29-10-2021

if __name__ == '__main__':
    server.app.run()

