from random import getrandbits
from rsa_crt import rabinMiller


def generate_prime_number():
    x = getrandbits(10)

    while( x % 4 != 3 or (not rabinMiller(x))):
        x = getrandbits(10)

    return x

def bbs(p , q , num_round = 15 , bit_size = 16):
    M = p * q
    output = []
    x = pow(getrandbits(10),2 , M)
    print("Choosen random seed ", x)
    for j in range(num_round):
        bit_str = ""
        for i in range( bit_size ):
            x =  x*x % M
            bit_str += str(x % 2 )
        output.append( bit_str )
    print("%d round output \n\n"% num_round , output)
    return x



if __name__ == "__main__":
    p , q = generate_prime_number() , generate_prime_number()
    print("Generate 10 bit p and q (%s , %s)" %(p , q))
    bbs(p, q)