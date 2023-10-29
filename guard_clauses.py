import time
from apples import apples

start_time = time.time()

def validation_for_apple():
    if apple.get('name') != 'Red Delicious':
        return False
    if apple.get('color') != 'Red':
        return False
    if apple.get('taste') != 'Sweet':
        return False
    if apple.get('price') != '$1.29/lb':
        return False
    if apple.get('texture') != 'Velvety':
        return False
    return True

for i in range(3000):
    for apple in apples:
        result = validation_for_apple()

print(result)


end_time = time.time()

elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time:.200} seconds")
