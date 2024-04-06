import redis

def init_redis_cache():
    return redis.Redis(host='redis', port=6379)