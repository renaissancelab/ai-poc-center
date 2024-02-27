import json
from flask import Flask, request
import sys
import platform
import psutil
from common import log_util


app = Flask(__name__)


@app.route('/health_check')
def health_check():
    return 'success!'


@app.route('/system_info')
def system_info():
    info = {}

    info["args"] = sys.argv
    info["platform"] = platform.platform()
    info["uname"] = platform.uname()

    info["mem"] = psutil.virtual_memory()
    info["cpu"] = psutil.cpu_stats()
    info["uptime"] = psutil.boot_time()

    json_data = json.dumps(info)
    return json_data


@app.route('/call_message', methods=["POST"])
def call_message():
    data = request.get_json()
    #executor.submit(long_task, 'hello', 123)

    # 方法二
    # data = request.json        # 获取 JOSN 数据
    # data = data.get('obj')     #  以字典形式获取参数

    return ""


@app.route('/produce_message', methods=["POST"])
def produce_message():
    data = request.get_json()
    data_str = json.dumps(data).encode()
    return 'success'


@app.route('/consume_message', methods=["GET"])
def consume_message():
    data = request_parse(request)
    name = data.get("name")
    return name


def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data


def init_flask():
    app.run(debug=False, host='0.0.0.0', port=8089, use_reloader=False)
    log_util.logger.info("success")

