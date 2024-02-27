import os
import boto3
import datetime
import common
from common import config, log_util

session = boto3.Session(profile_name='cnc')


def upload_file_to_s3(file_path) -> (bool, str, str):
    s3_path = ""
    try:
        env = common.globals.env
        now = datetime.datetime.now()
        day = now.strftime("%Y%m%d")
        filename = os.path.basename(file_path)
        s3_path = 'cdn/aivideo/{}/{}/{}'.format(env, day, filename)
        cdn_path = '{}/{}/{}'.format(env, day, filename)
        log_util.logger.info(f"file_path:{file_path}")
        log_util.logger.info(f"s3_path:{s3_path}")
        log_util.logger.info(f"cdn_path:{cdn_path}")
        result = session.client('s3').put_object(
            Bucket=config.S3_BUCKET,
            Key=s3_path,
            Body=open(file_path, 'rb'),
            ContentType='video/mp4',
        )
        res = result.get('ResponseMetadata')
        if res.get('HTTPStatusCode') == 200:
            log_util.logger.info('upload s3 success response:{}'.format(str(res)))
            return True, s3_path, cdn_path
        else:
            log_util.logger.error('upload s3 failed response:{}'.format(str(res)))
            return False, s3_path, cdn_path
    except Exception as e:
        log_util.logger.error(f"upload s3 have exception:{e}")
        return False, s3_path, cdn_path
