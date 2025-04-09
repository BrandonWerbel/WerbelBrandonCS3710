from sympy import randprime

message = input("Enter message: ")

# get primes
p = randprime(100_000, 1_000_000)
q = randprime(100_000, 1_000_000)

# calculate variables
n = p*q
e = 65537
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
keysize = n.bit_length()

print(f"p: {p}")
print(f"q: {q}")
print(f"e: {e}")
print(f"d: {d}")

# Encode message into utf-8
message_bytes = message.encode()
# break message in chunks by keysize (divided by 8 for bits to bytes conversion), then convert to integers
M = [int.from_bytes(message_bytes[i : keysize // 8 + i]) for i in range(0, len(message_bytes), keysize // 8)]

# encode message
C = list(map(lambda m:  pow(m, e, n), M))
print("Ciphertext:")
print(":".join(map(lambda c: str(hex(c)), C)))

# decrypt message and concatenate chunks back together
P = list(map(lambda c: pow(c, d, n), C))
plaintext = "".join(list(map(lambda p: p.to_bytes((p.bit_length() + 7) // 8).decode(), P)))
print(f"Decrypted Message: {plaintext}")