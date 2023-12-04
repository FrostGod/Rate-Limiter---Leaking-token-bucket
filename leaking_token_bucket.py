
# limiter
# whenever component recieves requests, it should count the number of requests
# sent from any ip/userID and block them to filter

import http
import socketserver
from cache import LocalCache

import json
import time

import threading


# limiting 5 requests per UserID and IP


class RateLimiter:
    
    def __init__(self):
        self.cache = LocalCache()
        self.buckets = set()
        periodic_thread = threading.Thread(target=self.Refiller)
        periodic_thread.daemon = True
        periodic_thread.start()
        
    def Refiller(self):
        print("entered refiller")
        while True:
            for bucket in self.buckets:
                self.cache.set_cache(bucket)
            time.sleep(60)

    def check_rate_limit(self, UserID):
        under_limit = True
        print(UserID)
        print(self.cache.exists_cache(UserID))
        if self.cache.exists_cache(UserID):
            val = self.cache.get_cache(UserID)
            print("current tokens available for this user are " + str(val))
            if val > 0:
                self.cache.use_token(UserID)
            else:
                under_limit = False 
        else:
            self.cache.set_cache(UserID)
            self.cache.use_token(UserID)
            print(self.cache.get_cache(UserID))

        self.buckets.add(UserID)
        return under_limit
    
    def flush_cache(self):
        self.cache.flush_all()

# if __name__ == "__main__":
#     cache = LocalCache()
#     main()
