# Сериализация. Помогает сохранять состояния игры к примеру. Таблица рекордов.
import pickle

a = {}
a[1] = a

pickle.dump()
pickle.load()

import marshal
#import msgpack
import json
import shelve
#sqlite
# Можно восстанавливаться после сбоев используя запись состояния во время работы программы.


