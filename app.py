import redis
import random
import string

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Function to generate a random value
def generate_random_value():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# Function to add multiple key-value pairs with random values to Redis
def add_multiple_random_to_redis(keys):
    data = {key: generate_random_value() for key in keys}
    for key, value in data.items():
        r.set(key, value)

# Function to print all keys in Redis
def print_all_keys():
    keys = r.keys('*')
    if keys:
        print("Keys in Redis:")
        for key in keys:
            print(f"- {key.decode()} -> {r.get(key).decode()}")
    else:
        print("Redis is empty.")

# Keys to add to Redis
keys = ['key1', 'key2', 'key3']

# Add multiple key-value pairs with random values to Redis
add_multiple_random_to_redis(keys)

# Print all keys in Redis
print_all_keys()
