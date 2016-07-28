#encoding=utf-8
#

# 此模块做操作系统环境检查
# 
#
import platform,os
from config import app_config
class Env_check():

    def __init__(self):
        pass

    # 检查当前操作系统类型
    def os_check(self):
        os_type = platform.system()
        if os_type == "Windows":
            return "Windows"
        elif os_type == "Linux":
            return "Linux"
        else:
            return "Other"

    # 校验临时文件目录是否存在
    def dir_check(self):
        os_type = self.os_check()
        if os_type == "Windows":
            if (os.path.exists(app_config['windows_dir'])):
                print "%s 临时文件目录已经存在." % (app_config['windows_dir'])
            else:
                os.makedirs(app_config['windows_dir'])
                print "%s 临时文件目录创建成功." % (app_config['windows_dir'])

        elif os_type == "Linux":
            if (os.path.exists(app_config['linux_dir'])):
                print "%s 临时文件目录已经存在." % (app_config['linux_dir'])
            else:
                os.makedirs(app_config['linux_dir'])
                print "%s 临时文件目录创建成功." % (app_config['linux_dir'])
        else:
            print "暂不支持操作系统."

        return True
        
    def user_check(self):
        pass

    def cpu_check(self):
        pass

    def mem_check(self):
        pass