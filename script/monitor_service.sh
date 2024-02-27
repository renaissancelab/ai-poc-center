#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#*/60 * * * * sh /root/common/monitor_service.sh test > /dev/null 2>&1 &

process_name="run.py"

process_home="/root/roop/"
cd ${process_home}
env=$1

options="--execution-provider cuda --execution-threads 7"

source /etc/profile

echo "Check startUp!"

count=`ps -ef | grep ${process_name} | grep -v grep | grep -v tail| wc -l`
echo "${count}"
if [ ${count} -lt 1 ]; then
    echo "${process_name} is not running, will startup"
    echo `ps -ef | grep ${process_name} | grep -v auto | awk '{print $2}' | xargs kill -9`
    sleep 1s
    echo "/App/python3/bin/python3 ${process_home}${process_name} -e ${env} ${options} >/dev/null 2>&1 &"
    echo `/App/python3/bin/python3 ${process_home}${process_name} -e ${env} ${options} >/dev/null 2>&1 &`
else
    echo "${process_name} is running, do nothing"
fi

echo "Check done success!"