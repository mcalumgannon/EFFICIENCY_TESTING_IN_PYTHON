import time
from apples import apples

start_time = time.time()

def validation_for_apple():
    for apple in apples:
        if apple.get('name') == 'Red Delicious':
            if apple.get('color') == 'Red':
                if apple.get('taste') == 'Sweet':
                    if apple.get('price') == '$1.29/lb':
                        if apple.get('texture') == 'Velvety':
                            return True
    return False

for i in range(3000):                  
    result = validation_for_apple()
print(result)

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time:.200} seconds")