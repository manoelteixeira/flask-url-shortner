from os import makedirs, environ, path, listdir
from random import choice, seed

class KeyList:
    def __init__(self) -> None:
        self._used_keys = []
        
    
    def _generate_key(self, size:int) -> str:
        seed() # 
        characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = [choice(characters) for _ in range(size)]
        return ''.join(key)
    
    def get_key(self, size:int=7):
        while True:
            key = self._generate_key(size)
            if key not in self._used_keys:
                self._used_keys.append(key)
                return key