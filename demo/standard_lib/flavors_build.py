#!/usr/bin/env python3
__author__ = 'zl'
import subprocess
import shutil
import os
import datetime

# 渠道列表
flavors = ["aaa", "bbb", "ccc"]
project_name = "android_market_2"
build_type = "Release"
_var_key = "${CHANNEL_NAME}"
_MANIFEST_FILE = "AndroidManifest.xml"         # 目标文件
_MANIFEST_FILE_COPY = _MANIFEST_FILE+"_bak"    # 复制的原始文件
_OUTPUT_BUILD_DIR = "build/outputs/apk/"

def init_build():
    """
    清理项目文件
    :return:
    """
    subprocess.call("gradle clean", shell=True)

def assemble(channel, type="Release"):
    """
    开始构建编译
    :param channel:
    :param type:
    :return:
    """
    write_channel(channel)
    cmd = "gradle assemble"+type
    subprocess.call(cmd, shell=True)
    save_apk(channel, type.lower())

def write_channel(channel):
    """
    写入渠道信息
    :param channel:
    :return:
    """
    lines = None
    with open(_MANIFEST_FILE_COPY, mode="r", encoding="utf-8") as fd:
        lines = fd.readlines()

    # lines
    if lines is not None:
        print("start write write channel ")
        with open(_MANIFEST_FILE, mode="w", encoding="utf-8") as fd:
            for line in lines:
                if line is None:
                    continue
                if _var_key in line:
                    line = line.replace(_var_key, channel)

                fd.write(line)
        print("write channel success !")
    else:
        print("lines is null !")

def save_apk(channel, type="release"):
    output_apk_src = _OUTPUT_BUILD_DIR+project_name+"-"+type+".apk"
    output_apk_dst = _OUTPUT_BUILD_DIR+project_name+"-"+channel+"-"+type+".apk"
    if os.path.exists(output_apk_src):
        os.rename(output_apk_src, output_apk_dst)
    pass

def init_file():
    """
    保存原始AndroidManifest.xml文件，方便每次修改
    :return:
    """
    if os.path.exists(_MANIFEST_FILE_COPY):
        os.remove(_MANIFEST_FILE_COPY)
    if os.path.exists(_MANIFEST_FILE):
        shutil.copyfile(_MANIFEST_FILE, _MANIFEST_FILE_COPY)

def finalize_file():
    """
    还原原始文件状态
    :return:
    """
    os.remove(_MANIFEST_FILE)
    os.rename(_MANIFEST_FILE_COPY, _MANIFEST_FILE)

def main():
    t1 = datetime.datetime.now()
    print("start build !")
    # 清理文件
    init_build()
    # 初始化文件
    init_file()
    # 多渠道开始
    for flv in flavors:
        print("start build channel --->> ", flv)
        assemble(flv, build_type)
    # 恢复文件
    finalize_file()

    t2 = datetime.datetime.now()

    print("---------    over !!  ---------- \n Total time ", t2-t1)
    pass

if __name__ == "__main__":
    main()
