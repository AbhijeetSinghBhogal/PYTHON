from cryptography.fernet import Fernet

def main():
    
    ##### KEY GENERATION #####

    key = Fernet.generate_key()

    with open("/Users/abhijeetsingh/PYTHON/Encryption_Decryption/mykey.key", "wb") as mykey:
        mykey.write(key)
    # print(key)

    with open("/Users/abhijeetsingh/PYTHON/Encryption_Decryption/mykey.key", "rb") as mykey:
        key = mykey.read()
    # print(key)

    ##### ENCRYPTION #####

    f = Fernet(key)

    with open("/Users/abhijeetsingh/PYTHON/Encryption_Decryption/grades.csv", "rb") as  original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open("/Users/abhijeetsingh/PYTHON/Encryption_Decryption/enc_grades.csv", "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    
    ##### DECRYPTION #####

    f = Fernet(key)

    with open("/Users/abhijeetsingh/PYTHON/Encryption_Decryption/enc_grades.csv", "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open("/Users/abhijeetsingh/PYTHON/Encryption_Decryption/dec_grades.csv", "wb") as decrypted_file:
        decrypted_file.write(decrypted)

if __name__ == "__main__":
    main()