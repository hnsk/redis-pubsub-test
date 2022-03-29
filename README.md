# Redis pub/sub latency test

## Installation

```
pip install -r requirements.txt
```

## Usage

By default connects to `localhost:6379` without password.

Reads environment variables `REDIS_HOST`, `REDIS_PORT`, `REDIS_PASS`.

### publisher.py
Sends timestamp once a second

### subscriber.py
Reads the timestamp and prints latency compared to local time.
