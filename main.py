#!/usr/bin/env python3

import sys
from common import log_util, redis_client, config
from entrance import controller

if __name__ == '__main__':
    log_util.logger.info(f'main startup:{sys.argv}')
    log_util.logger.info(f'home path:{sys.path[0]}')

    log_util.logger.info(f'ready init base config')
    config.init_base_config()

    log_util.logger.info(f'ready init redis cluster client')
    redis_client.init_redis_cluster_client()

    # last
    controller.init_flask()



