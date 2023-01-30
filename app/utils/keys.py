import pickle
from os import path
from random import seed, choice

used_keys_file = path.join(path.abspath(path.curdir), 'instance/used_keys.pickle')

def _load_keys():
    if not path.isfile(used_keys_file):
        return []
    with open(used_keys_file, 'rb') as file:
        keys =  pickle.load(file)
        return keys

def _save_keys(keys):
    with open(used_keys_file, 'wb') as file:
        pickle.dump(keys, file)

def _generate_key(size:int) -> str:
    seed() # 
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = [choice(characters) for _ in range(size)]
    return ''.join(key)

def get_key(size:int) -> str:
    keys = _load_keys()
    key = None
    while True:
        key = _generate_key(size=size)
        if key not in keys:
            break
    keys.append(key)
    _save_keys(keys)
    return key