import random
from math import gcd
from time import time
from asni_random_generator import des

def rabinMiller(n, confidency_leve= 5):
    if n!=int(n):
        return False
    n=int(n)

    #base cases
    # avoid empty range for randrange() (%d,%d, %d)" % (istart, istop, width) in randint
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False

    if n==2 or n==3 or n==5 or n==7:
        return True

    k = 0
    q = n-1
    while q%2==0:
        q>>=1
        k+=1
    assert(2**k * q == n-1)

    def trial_composite(a):
        if pow(a, q, n) == 1:
            return False
        for i in range(k):
            if pow(a, 2**i * q, n) == n-1:
                return False
        return True

    for i in range(confidency_leve):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
    return True

def generate_prime_num(bit_size=512):
    rand_num = random.getrandbits(bit_size)
    while(not rabinMiller(rand_num)):
        del rand_num
        rand_num = random.getrandbits(bit_size)
    return rand_num

def generate_key_pair(bit_size, debug=False):
    p , q = generate_prime_num(bit_size) , generate_prime_num(bit_size)

    n, phi_n = p * q , (p-1)*(q-1)
    if debug:
        print("\nGenerating prime number pair p and q (%d , %d)\n"%(p , q))
        print("\nCompute p x q %d\n\nphi(n) is %d "% (n , phi_n))
    return n , phi_n , p , q

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def RSA(e, m , bit_size= 512 ,CRT=False, debug=False):
    n , phi_n , p , q  = generate_key_pair(bit_size , debug)
    # check for co-prime between e and phi_n
    while( gcd(phi_n,e) != 1):
        n , phi_n , p , q  = generate_key_pair(bit_size, debug)

    d = modinv(e,phi_n)
    if debug:
        print("\nCompute d %d" % d)

    # chinese reminder theorem for decryption
    dq = modinv(e, q - 1)
    dp = modinv(e, p -1)

    qinv = modinv(q, p)

    c = m**e % n

    if CRT:
        start_time = time()
        m1 = pow(c, dp , p)
        m2 = pow(c, dq , q)

        h = (qinv  *(m1 - m2)) % p
        m_ = m2 + h * q
        end_time = time()
        print("m_ and m should be equal ",(m_ == m) )
        print("The time taken is %.3f ms"% (1000 * ( end_time - start_time)))
        return

    start_time = time()
    dec = pow(c, d , n)
    end_time = time()
    print("m_ and m should be equal ", (dec == m) )
    print("Without CRT takes %3f ms" % (1000 * (end_time - start_time)))
    del n , phi_n , p , q


def rsa_generation( bit_size = 1024 , assigned_key = False , key=()):
    if assigned_key:
        n , phi_n , p , q = key
    else:
        n , phi_n , p , q = generate_key_pair(bit_size)

    e = random.getrandbits(1024)
    while( gcd(phi_n,e) != 1):
        e = random.getrandbits(1024)
    d = modinv(e,phi_n)
    return (n , e) ,( d , p , q)


class KeyHolder():
    def __init__(self , name="alice", bit_size = 1024, assigned_key=False, key = ()):
        self.name= name
        if ( not assigned_key ):
            self.public_key , self.private_key = rsa_generation(bit_size)
        else:
            self.public_key , self.private_key = rsa_generation(assigned_key= assigned_key, key = key)
        self.bit_size = bit_size
        self.n , self.e = self.public_key
        self.d , self.p , self.q = self.private_key

    def compute_dh_pub_secret(self , p, g):
        self.dh_public_key = random.getrandbits(15360)
        self.public = pow(g, self.dh_public_key, p)
        return self.public

    def compute_dh_shared_secret(self, receiver_public_key, prime):
        start_time = time()
        self.shared_secret = pow(receiver_public_key  , self.dh_public_key , prime)
        end_time = time()
        print("The time taken %s compute DH-shared key generate shared key is %.3f ms"% ( self.name  ,1000 * ( end_time - start_time)))
        return self.shared_secret

    def compute_ecdh_pub_secret(self, basePoint):
        self.ec_private_key = random.getrandbits(512)
        self.ec_public = basePoint * self.ec_private_key

    def compute_ecdh_shared_secret(self, receive_public_key):
        start_time = time()
        self.shared_secret = self.ec_private_key * receive_public_key
        end_time = time()
        print("The time taken %s compute ECDH-shared key generate shared key is %.3f ms"% ( self.name  ,1000 * ( end_time - start_time)))
        return self.shared_secret


if __name__ == "__main__":
    e , m  =65537 , 466921883457309

    RSA( e, m , CRT=False , debug=False)
    RSA( e, m , CRT=True , debug=False)
