import redis
#TODO: attach this to redis cloud
class LocalCache:
    """
    local cache implementation using redis
    """
    def __init__(self):
        self.redis_client = redis.Redis()
    
    def get_cache(self, key):
        val = int(self.redis_client.get(key).decode('utf-8'))
        return val

    def set_cache(self, key, value=0):
        if value == 0:
            if self.redis_client.exists(key):
                self.redis_client.incrby(key, 5)
            else:
                self.redis_client.set(key, 5)

    def use_token(self, key):
        self.redis_client.decr(key)

    def exists_cache(self, key):
        return self.redis_client.exists(key)

    def del_cache(self, key):
        self.redis_client.delete(key)

    def flush_all(self):
        self.redis_client.flushall()