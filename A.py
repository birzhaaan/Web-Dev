import os
import struct
import time

# Генерация случайного ключа
def generate_key(key_size=16):
    return os.urandom(key_size)

# Функция для чтения файла
def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

# Функция для записи файла
def write_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

# Функция для простого блочного XOR-шифрования (не AES, но принцип похож)
def xor_encrypt(data, key):
    key_len = len(key)
    return bytes(data[i] ^ key[i % key_len] for i in range(len(data)))

# Функция для шифрования (с простым XOR вместо AES)
def encrypt_file(input_file, key_file, output_file):
    key = read_file(key_file)  # Читаем ключ
    data = read_file(input_file)  # Читаем открытый текст

    encrypted_data = xor_encrypt(data, key)  # XOR-шифрование
    write_file(output_file, encrypted_data)

    return encrypted_data

# Функция для дешифрования (тот же XOR, так как XOR-операция обратима)
def decrypt_file(encrypted_file, key_file, output_file):
    key = read_file(key_file)  # Читаем ключ
    encrypted_data = read_file(encrypted_file)  # Читаем зашифрованные данные

    decrypted_data = xor_encrypt(encrypted_data, key)  # XOR-расшифрование
    write_file(output_file, decrypted_data)

    return decrypted_data

# Генерация ключа
key_size = 16  # 16 байт (128 бит)
key = generate_key(key_size)
write_file("aes_key.bin", key)

# Создание тестового файла с открытым текстом
write_file("plaintext.txt", b"Hello, this is a test message for encryption!")

# Шифрование
encrypted = encrypt_file("plaintext.txt", "aes_key.bin", "encrypted.bin")

# Дешифрование
decrypted = decrypt_file("encrypted.bin", "aes_key.bin", "decrypted.txt")

# Проверка результата
print(f"Исходный текст: {read_file('plaintext.txt')}")
print(f"Расшифрованный текст: {read_file('decrypted.txt')}")
