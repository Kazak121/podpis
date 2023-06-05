import hashlib
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def read_file_in_chunks(filename, chunk_size):
    chunks = []
    prime1 = 0
    prime2 = 0
    with open(filename, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            chunk = int(chunk, 2)
            if is_prime(chunk):
                if chunk > prime1:
                    prime2 = prime1
                    prime1 = chunk
                elif chunk > prime2 and chunk!=prime1:
                    prime2 = chunk
    return prime1, prime2
def signature(data, priv, n):
    mess = data.encode('utf-8')
    hasz = hashlib.sha1(mess).hexdigest()
    sign = ''
    for i in range(0, len(hasz)):
        r1 = pow(int(hasz[i], 16), priv, n)
        r2 = hex(r1)
        sign += r2
    return sign

def check_it_out (data, signa, publ, n):
    mess = data.encode('utf-8')
    hasz = hashlib.sha1(mess).hexdigest()
    signa2 = signa.split('0x')
    signa3 = ''
    for i in range(1, len(signa2)):
        r1 = pow(int(signa2[i], 16), publ, n)
        if r1 == 0:
            r2 = '0'
        else:
            r2 = hex(r1).lstrip('0x')
        signa3 += str(r2)
    if signa3 == hasz:
        return True
    else:
        return False

    
        
print ("\n Czekaj")
filename = 'losowe.txt'
chunk_size = 32

p, q = read_file_in_chunks(filename, chunk_size)
e = 7
phi = (p-1)*(q-1)
n = p*q
priv = pow(e, -1, phi)
publ = e

data = 'test.txt'
data2 = 'test.txt'
signa = signature(data2, priv, n)
print("\n\n\n\n podpis: \n")
print(signa)
print("\n\n")
if check_it_out (data, signa, publ, n):
    print (" Podpis jest poprawny")
else:
    print (" Zly podpis")






