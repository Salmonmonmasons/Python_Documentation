__author__ = 'Masonsalmon'

from TwitterAPI import TwitterAPI
import random
import time
ckey = ''
csecret = ''
atoken = ''
asecret = ''

api = TwitterAPI(ckey,csecret,atoken,asecret)
a = 0
b = 0

start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))

while a < 2:
    b = random.randrange(1,1000000000000000000000)

    status = str(b) + ' @FriendsName'

    a = a+1

    r = api.request('statuses/update', {'status': status})
print('SUCCESS' if r.status_code == 200 else 'FAILURE')
