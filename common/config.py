import argparse
import common.globals
from common import log_util

kafka_config = {
    'dev': {
        'producer_bootstrap_servers_finish': '192.168.13.69:9092',
        'producer_topic_finish': 'aivideo_finish',

        'producer_bootstrap_servers_progress': '192.168.13.69:9092',
        'producer_topic_progress': 'aivideo_progress',

        'consumer_bootstrap_servers_queuing': '192.168.13.69:9092',
        'consumer_topic_queuing': 'aivideo_queuing',
        'group-id': 'aivideo_queuing_consumer_group',
    }
}

redis_config = {
    'dev': {
        'host': '127.0.0.1',
        'password': None
    }
}

S3_BUCKET = ''
CDN_DOMAIN = ''

# REDIS KEY
PRE = "cnc:magician:{}:"
QUEUE_TASK_WAIT = PRE + "queue:task:wait"

KAFKA_CONSUME_QUEUE_FAIL_LIST = "kafka_consume_queue_fail_list"
KAFKA_CONSUME_QUEUE_RECORD_STRING = "kafka_consume_record:{}"
TASK_TIMEOUT_CANCELED_STRING = PRE+"task:{}:{}"


def init_base_config() -> None:
    program = argparse.ArgumentParser()
    program.add_argument('-e', '--env', help='env', dest='env')
    args = program.parse_args()
    common.globals.env = args.env
    log_util.logger.info(f"success env:{common.globals.env}")

