# CSC4001 Backend

## 项目介绍：
该Django项目包括```CSC4001-Frontend```所需的API。

## 项目运行：
```shell
# （第一次下载）从gitlab上下载代码到本机
git clone git@github.com:118010362/CSC4001-backend.git

# （不是第一次下载）就直接更新本机代码
cd CSC4001-backend
git pull

# 在虚拟环境下安装相应的依赖包
pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r ./requirements/common.txt

# 运行项目
python3 manage.py runserver

#如果需要迁移 则运行
python3 manage.py makemigrations
python3 manage.py migrate

```
