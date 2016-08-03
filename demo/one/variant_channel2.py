#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import hashlib
import logging
import logging.handlers
import datetime

#variant.baseName

# 要打的appids
appids = ("2520", "5724","5813","5566","6437","6099","3344","4010","72")
# 项目路径
PROJ_DIR = "/Users/zl/develop/project/taptap_client_build"
# 渠道,gradle 参数
CHANNEL_CMD = "aBaiduR"
# 打包生成的文件名,固定的
APK_FILE_NAME = "taptap_1.5.3_baidu-release.apk"
# 最终输出 apk 路径
APK_OUTPUT_DIR = "/Users/zl/tmp/apk"

APPIDS_CONFIG="/Users/zl/package.txt"

# 原始生成的 apk 绝对路径
_APK_ABS_PATH = os.path.join(PROJ_DIR, "app", "build", "outputs", "apk", APK_FILE_NAME)

# 新 apk 文件名
_APK_NEW_FILE_NAME = os.path.join(APK_OUTPUT_DIR,
                                  os.path.splitext(APK_FILE_NAME)[0] + "_app_%s" + os.path.splitext(APK_FILE_NAME)[1])
# 要修改的java文件
_CHANNEL_CONFIG_CLASS_JAVA_FILE = os.path.join(PROJ_DIR, "app", "src", "main", "java", "com", "play", "taptap",
                                               "ChannelConfig.java")

### 动态生成代码
_CHANNEL_CONFIG_SOURCE_CODE = '''
package com.play.taptap;

public class ChannelConfig {

    public static final String getChannelAppId(){
        return "%s";
    }
}

'''

# 日志
LOG_FILE = ('assemble_apk_%s.log' % datetime.datetime.now().strftime("%Y%m%d_%H"))
handler = logging.handlers.RotatingFileHandler(LOG_FILE, encoding="utf-8", maxBytes=1024 * 1024 , backupCount=5)
# fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger('app')
logger.addHandler(handler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

logger.setLevel(logging.DEBUG)

#------

def preSourceCode(appid):
    """
    处理代码
    :param appid:
    :return:
    """
    code = (_CHANNEL_CONFIG_SOURCE_CODE % appid)
    with open(_CHANNEL_CONFIG_CLASS_JAVA_FILE, mode="w", encoding="utf-8") as f:
        f.write(code)

    logger.debug("生成的代码 :")
    with open(_CHANNEL_CONFIG_CLASS_JAVA_FILE, mode="r", encoding="utf-8") as f:
        logger.debug(f.read())
    pass


def assembleApp(appid):
    """
    打包apk
    :param appid:
    :return:
    """
    #gradle 路径
    p = subprocess.Popen([os.environ.get("GRADLE_HOME") + "/bin/gradle", "-p", PROJ_DIR, CHANNEL_CMD],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    logger.debug("gradle assemble apk ...")
    returncode = p.poll()
    while returncode is None:
        line = p.stdout.readline()
        returncode = p.poll()
        line = line.strip()
        # print(line.decode())
    logger.debug("return code %s " % returncode)
    if returncode == 0:
        logger.debug("build %s success!" % appid)
        handleFile(appid)
    else:
        logger.debug("build %s error!" % appid)
        exit(0)
    pass


def handleFile(appid):
    """
    处理生成的apk文件
    :param appid:
    :return:
    """
    if os.path.exists(_APK_ABS_PATH) and os.path.isfile(_APK_ABS_PATH):
        new_file = _APK_NEW_FILE_NAME % appid
        logger.debug("file: %s exists! " % (_APK_ABS_PATH))
        logger.debug("rename to: %s " % (new_file))
        os.rename(_APK_ABS_PATH, new_file)
    else:
        logger.debug("error %s file not found !!!" % _APK_ABS_PATH)
        exit(0)
    pass


def processAppId(appid):
    logger.debug("开始打包 ---- %s -----" % appid)
    preSourceCode(appid)
    assembleApp(appid)
    new_file = _APK_NEW_FILE_NAME % appid
    logger.debug("保存在  %s " % (new_file))
    logger.debug("md5: %s " % md5sum(new_file))
    logger.debug("打包 ---- %s ----- 成功!\n\n" % appid)
    pass


def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(128 * md5.block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()

def readAppIds():
    apps=[]
    with open(APPIDS_CONFIG,mode="r", encoding="utf-8") as f:
        line = f.readline()

        while line:
            if len(line.split("\t")) > 1:
                id = line.split("\t")[0].split("_")[1]
                #print(" %s |||  %s " % (line.split("\t")[0], line.split("\t")[0].split("_")[1]))
                apps.append(id)
            line = f.readline()

    return apps


if __name__ == "__main__":
    appids=readAppIds()
    logger.debug("------------开始打包------------")
    logger.debug("-----总个数 %s-----" % len(appids))
    logger.debug(str(appids))
    for appid in appids:
        processAppId(appid)
