# import uuid
#
# # print(uuid.uuid1())
# # print(type(uuid.uuid1()), str(uuid.uuid1()).replace('-', ''))
#
# uid = uuid.uuid1()
#
# print(uid, type(uid), '\n'+str(uid).replace('-', ''))


import requests
from eliot import start_action, to_file

to_file(open("linkcheck.log", "w"))


def check_links(urls):
    with start_action(action_type="check_links", urls=urls):
        for url in urls:
            try:
                with start_action(action_type="download", url=url):
                    response = requests.get(url)
                    response.raise_for_status()
            except Exception as e:
                raise ValueError(str(e))


try:
    check_links(["http://eliot.readthedocs.io", "http://nosuchurl"])
except ValueError:
    print("Not all links were valid.")
