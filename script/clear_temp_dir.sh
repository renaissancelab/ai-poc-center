#!/bin/bash

function clear(){
  if [ -d $1 ];then
    for f in ` ls $1 `
      do
         file=$1$f
         a=`stat -c %Y $file`
         b=`date +%s`
         if [ $[ $b - $a ] -gt 3600 ];then
			  rm -rf $file
         fi
      done
  else
     echo "目录不存在"
  fi
}

dirPath1="/root/roop/resource/src/temp/"
clear $dirPath1