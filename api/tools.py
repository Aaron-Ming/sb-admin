#encoding=utf-8
#


# 切割路由路径，获取路由动作
def split_path(req):
    tmp = req.split('/')
    return tmp[-1]

