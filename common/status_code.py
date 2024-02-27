#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Desc: { 项目枚举类模块 }
from enum import Enum


class StatusCodeEnum(Enum):
    # base
    RAW = (0, 'raw')
    QUEUE = (1, 'queue')
    PROGRESS = (2, 'progress')
    FINISH = (3, 'success')
    Failed = (4, 'failed')
    REJECT_FULL = (5, 'reject_full')
    REJECT_SELF = (6, 'reject_self')

    # biz
    IMAGE_HAVE_NO_FACE_ERROR = (100, 'image_have_no_face_error')
    VIDEO_HAVE_NO_FACE_ERROR = (101, 'video_have_no_face_error')
    VIDEO_TOO_LONG_ERROR = (102, 'video_too_long_error')
    VIDEO_NO_FACE_ERROR = (103, 'video_no_face_error')
    UPLOAD_TO_S3_FAILED = (104, 'upload_to_s3_failed')
    PROCESSING_TO_VIDEO_FAILED = (105, 'processing_to_video_failed')
    UNKNOWN_EXCEPTION = (199, 'unknown_exception')


    SERVER_SYSTEM_ERROR = (500, 'server_system_error')
    SERVER_FRAME_PROCESSOR_ERROR = (501, 'server_frame_processor_error')

    @property
    def code(self):
        return self.value[0]

    @property
    def msg(self):
        return self.value[1]
