import os 


secret_key = os.urandom(16).hex()
print(secret_key)