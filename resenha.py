import redis
import time
r = redis.Redis(host='10.1.68.172', port=6379, db=0)
r.ping()
# True

# ### Inserindo Dados / CRIATE ###

r.set('win', 'sabe nada os cara')
# True

# ### Obtendo Dados / UPDATE ###

r.set('win', 'sabe nada os cara')
while(True):
   name = r.get('win')
   print(name.decode())
   time.sleep(1)