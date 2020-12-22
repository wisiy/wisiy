import uuid

# print(uuid.uuid1())
# print(type(uuid.uuid1()), str(uuid.uuid1()).replace('-', ''))

uid = uuid.uuid1()

print(uid, type(uid), '\n'+str(uid).replace('-', ''))
