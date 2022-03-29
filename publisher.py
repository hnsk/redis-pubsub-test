import redis
from os import environ
from time import time, sleep

REDIS_HOST = environ.get('REDIS_HOST') or '127.0.0.1'
REDIS_PORT = int(environ.get('REDIS_PORT') or '6379')
REDIS_PASS = environ.get('REDIS_PASS') or None


rpool = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASS,
    decode_responses=True
)

def publish():
    rpool.publish('timestamp', str(time()))

def main():
    while True:
        publish()
        sleep(1)
    
if __name__ == "__main__":
    main()
