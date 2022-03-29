import redis
from os import environ
from time import time

REDIS_HOST = environ.get('REDIS_HOST') or '127.0.0.1'
REDIS_PORT = int(environ.get('REDIS_PORT') or '6379')
REDIS_PASS = environ.get('REDIS_PASS') or None

rpool = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASS,
    decode_responses=True
)

def receive():
    sub = rpool.pubsub()
    sub.subscribe('timestamp')
    for message in sub.listen():
        if message.get('type') == 'message':
            timedelta = time() - float(message.get('data'))
            print(f"Timedelta: {timedelta*1000:.3f}ms")

def main():
    receive()
    
if __name__ == "__main__":
    main()
