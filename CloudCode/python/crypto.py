from cryptography.fernet import Fernet
import json, const

def read_write_json(data: dict = None, filename="credentials.json") -> dict:
    if data is None:
        with open(filename, 'r') as f:
            data = json.load(f)
    else:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    return data


def create_or_login(login, password):
  data = read_write_json()
  if login in data:
    return user_login(login, password)
  else:
    data[login] = password
    read_write_json(data)
  print("User created successfully.")
  return True

def user_login(login, password):
  data = read_write_json()
  if not login in data:
    print("User does not exists.")
    return False
  if data[login] != password:
    print ("Wrong password.")
    return False
  return True

# --

def generate_key():
  return Fernet.generate_key()

def encrypt(message: bytes, key: bytes = const.FERNET_KEY) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes = const.FERNET_KEY) -> bytes:
    return Fernet(key).decrypt(token)

