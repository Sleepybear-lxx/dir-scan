# dir-scan
基于字典的Web目录扫描工具，字典参考自[LoRexxar/BScanner](https://github.com/LoRexxar/BScanner#bscanner)

# 使用说明  
python2 dir-scan -f dir_type -t thread_count
## 必选参数
* -f DIR_TYPE, --file=DIR_TYPE Type of dictionary used 工具使用的字典类型，目前版本（v1.0）包含asp\aspx\jsp\php四种类型为后缀的字典
## 可选参数 
* -t THREAD_COUNT, --thread=THREAD_COUNT Number of threads 工具使用的线程数，默认为10

# 更新日志
* v1.0 2022/03/29 基本功能完成
