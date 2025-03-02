from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import time
import numpy as np
import matplotlib.pyplot as plt

def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

def write_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

def generate_key(key_size=16):
    return os.urandom(key_size)  

def encrypt_file(input_file, key_file, output_file):
    key = read_file(key_file)
    data = read_file(input_file)
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    write_file(output_file, cipher.iv + encrypted_data)

    return cipher.iv + encrypted_data

def decrypt_file(encrypted_file, key_file, output_file):
    key = read_file(key_file)
    encrypted_data = read_file(encrypted_file)

    iv = encrypted_data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[AES.block_size:]), AES.block_size)

    write_file(output_file, decrypted_data)
    return decrypted_data

def flip_bit(data, bit_position):
    byte_pos = bit_position // 8
    bit_pos = bit_position % 8
    modified_data = bytearray(data)
    modified_data[byte_pos] ^= (1 << bit_pos)
    return bytes(modified_data)

def count_changed_bits(original, modified):
    return sum(bin(o ^ m).count('1') for o, m in zip(original, modified))

def avalanche_test(input_file, key_file, bit_position, change_key=False):
    key = read_file(key_file)
    data = read_file(input_file)

    encrypted_original = encrypt_file(input_file, key_file, "original_encrypted.bin")

    if change_key:
        modified_key = flip_bit(key, bit_position)
        write_file("modified_key.bin", modified_key)
        encrypted_modified = encrypt_file(input_file, "modified_key.bin", "modified_encrypted.bin")
    else:
        modified_data = flip_bit(data, bit_position)
        write_file("modified_plaintext.txt", modified_data)
        encrypted_modified = encrypt_file("modified_plaintext.txt", key_file, "modified_encrypted.bin")

    changed_bits = count_changed_bits(encrypted_original, encrypted_modified)
    return changed_bits

key_size = 16
key = generate_key(key_size)
write_file("aes_key.bin", key)

plaintext = b"Hello, where are you from"
write_file("plaintext.txt", plaintext)

start_time = time.time()
encrypted = encrypt_file("plaintext.txt", "aes_key.bin", "encrypted.bin")
encryption_time = time.time() - start_time

decrypted = decrypt_file("encrypted.bin", "aes_key.bin", "decrypted.txt")

print(f"Ключ (hex): {key.hex()}")
print(f"Исходный текст: {plaintext.decode()}")
print(f"Зашифрованный текст (hex): {encrypted.hex()}")
print(f"Расшифрованный текст: {decrypted.decode()}")
print(f"Время шифрования: {encryption_time:.6f} секунд")

bit_positions = range(128)  
changed_bits_text = [avalanche_test("plaintext.txt", "aes_key.bin", pos, change_key=False) for pos in bit_positions]
changed_bits_key = [avalanche_test("plaintext.txt", "aes_key.bin", pos, change_key=True) for pos in bit_positions]

plt.figure(figsize=(10, 5))
plt.plot(bit_positions, changed_bits_text, label="Изменение 1 бита в тексте")
plt.plot(bit_positions, changed_bits_key, label="Изменение 1 бита в ключе", linestyle="dashed")
plt.xlabel("Изменённый бит")
plt.ylabel("Изменённые биты в шифротексте")
plt.title("Эффект лавины AES")
plt.legend()
plt.grid()
plt.show()