# python3 安装 Beautiful Soup 4
我本机安装python2和python3两个版本，默认的是python2   
那么如何在python3中安装BeautifulSoup4呢？   
首先下载https://pypi.python.org/pypi/beautifulsoup4/ 源码，解压并进入到目录，在终端运行   
`python3 setup.py install`  
记住，安装结束后退出当前目录!! cd切换到其他目录!!   
安装结果测试   
`python3`   
`from bs4 import BeautifulSoup`   
如果没错误就安装成功了。   
同样的，安装速度快的lxml解析库https://pypi.python.org/pypi/lxml/3.4.4   
如果出现

>fatal error: 'libxml/xmlversion.h' file not found  
\#include "libxml/xmlversion.h" 
 1 error generated.
error: command 'clang' failed with exit status 1 
  
```
brew install libxml2
brew link libxml2 --force
export C_INCLUDE_PATH=/usr/local/Cellar/libxml2/2.9.2/include/libxml2:$C_INCLUDE_PATH
```
然后再次安装`python setup.py install `
