#Prova de trabalho
#Gabriel Rocha

import hashlib
import time

def ProofOfWork(S,msg,K):
   target = 2**(512-K)
   while(True):
      hash_msg = hashlib.sha256((str(S)+msg).encode()).hexdigest()
      S += 1
      if(int(hash_msg,16) < target):
         print('Numero de tentativas: %d'%S)
         break;
   return S

K = 279 

msg = 'Informação importante'

controle = 0

start = time.time()

while(controle == 0):
   controle = ProofOfWork(0,msg,K)

end = time.time()

running = end - start

print('Tempo decorrido: %.2f segundos'%running)
print('Hashes por segundo: %.0f'%(controle/running))
