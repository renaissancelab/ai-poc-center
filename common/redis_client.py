from rediscluster import RedisCluster
import redis
import common.globals
from common import log_util, config

redis_client = None


def init_redis_cluster_client():
    global redis_client
    if common.globals.env == "prod":
        if config.redis_config[common.globals.env]['password']:
            redis_client = RedisCluster(host=config.redis_config[common.globals.env]['host'], port=6379,
                                        max_connections=20480, skip_full_coverage_check=True,
                                        password=config.redis_config[common.globals.env]['password'])
        else:
            redis_client = RedisCluster(host=config.redis_config[common.globals.env]['host'], port=6379,
                                        max_connections=20480, skip_full_coverage_check=True)
    else:
        redis_client = redis.Redis(host=config.redis_config[common.globals.env]['host'], port=6379, db=0)
    redis_client.set('foo', 'bar')
    test_value = redis_client.get('foo')
    log_util.logger.info(f"success redis_client:{redis_client} test_value:{test_value}")
