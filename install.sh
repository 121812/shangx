#!/bin/bash
# shangx 安装脚本

if ! wget -O /tmp/shangx  https://raw.githubusercontent.com/121812/shangx/main/shangx.py;
then
    printf '%-20s' | sed 's/\ /-/g' && printf '下载失败，请手动安装' && printf '%-20s\n' | sed 's/\ /-/g'
    exit
fi

chmod 744 /tmp/shangx
mv /tmp/shangx /sbin/shangx

printf '%-20s' | sed 's/\ /-/g' && printf '安装成功' && printf '%-20s\n' | sed 's/\ /-/g'
