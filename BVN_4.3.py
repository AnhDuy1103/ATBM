
p = 17
q = 23
n = p * q             
phi = (p - 1) * (q - 1)
e = 5                  

P = "van cong anh duy"

def encrypt(P, e, n):
    ciphertext = []
    for ch in P:
        m = ord(ch)              
        c = pow(m, e, n)         
        ciphertext.append(c)
    return ciphertext


cipher = encrypt(P, e, n)
# TEST
print("ban goc:", P)
print("ban ma hoa RSA:", cipher)

