# -*- coding: utf-8 -*-
import subprocess
import os
import sys



appids = ("111")
# 项目路径
PROJ_DIR = "/Users/zl/develop/project/taptap_client_build"
# 渠道
CHANNEL_CMD = "aBaiduR"
# 打包生成的文件名
APK_FILE_NAME = "taptap_1.5.1_20160622_16_03_baiduRelease.apk"
# 最终输出 apk 路径
APK_OUTPUT_DIR = "/Users/zl/tmp/apk"

# 原始生成的 apk 绝对路径
_APK_ABS_PATH = os.path.join(PROJ_DIR, "app", "build", "outputs", "apk", APK_FILE_NAME)

# 新 apk 文件名
_APK_NEW_FILE_NAME = os.path.join(APK_OUTPUT_DIR,
                                  os.path.splitext(APK_FILE_NAME)[0] + "_app_%s" + os.path.splitext(APK_FILE_NAME)[1])

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


def preSourceCode(appid):
    print(_CHANNEL_CONFIG_SOURCE_CODE % appid)
    with open(_CHANNEL_CONFIG_CLASS_JAVA_FILE) as f:
        print(f.read())
    pass


def assembleApp(appid):
    p = subprocess.Popen(["gradle", "-p", PROJ_DIR, CHANNEL_CMD], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    returncode = p.poll()
    while returncode is None:
        line = p.stdout.readline()
        returncode = p.poll()
        line = line.strip()
        print(line.decode())
    print(" returncode %s " % returncode)
    if returncode == 0:
        print("build %s success!" % appid)
        handleFile(appid)
    else:
        print("build %s error!" % appid)
        exit(0)
    pass


def handleFile(appid):
    if os.path.exists(_APK_ABS_PATH) and os.path.isfile(_APK_ABS_PATH):
        new_file = _APK_NEW_FILE_NAME % appid
        print("file: %s exists, rename to: %s " % (_APK_ABS_PATH, new_file))
        os.rename(_APK_ABS_PATH, new_file)
    else:
        print("error %s file not found !!!" % _APK_ABS_PATH)
        exit(0)
    pass

def pp():
    with open("/Users/zl/other/docs/package.txt") as f:
        print(f.readline())
    pass

if __name__ == "__main__":
    print("hello")
    pp()
    # assembleApp()
    #preSourceCode("12122323")
    # for appid in appids:
    #     print("开始打包 %s  ------\n\n" % appid)
