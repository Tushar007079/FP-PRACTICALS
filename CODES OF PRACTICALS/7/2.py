def encrypt_file(input_filename, output_filename):
    with open(input_filename, 'rb') as input_file:
        with open(output_filename, 'wb')as output_file:
            while True:
                byte = input_file.read(1)
                if not byte:
                    break
                encrypted_byte = bytes([byte[0]+5])
                output_file.write(encrypted_byte)


def decrypt_file(input_filename, output_filename):
    with open(input_filename, 'rb')as input_file:
        with open(output_filename, 'wb')as ouptut_file:
            while True:
                byte = input_file.read(1)
                if not byte:
                    break
                decrypted_file = bytes([byte[0]-5])
                ouptut_file.write(decrypted_file)


encrypt_file('villain.txt', 'encrypted.txt')
print("File is Encrypted Sucessfully.")
decrypt_file('encrypted.txt', 'decrypted.txt')
print("File is Decrypted Sucessfully.")
