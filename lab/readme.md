# 校园教务/学工系统安全靶场

基于真实脱敏接口 1:1 复刻，包含统一认证、教务、学工三大模块，用于接口渗透、越权、未授权访问等漏洞练习。

## 包含接口（来自脱敏文档）

- 统一认证：/login、/getLoginUser、/getUserPermissionRouters

- 教务系统：成绩、课表、空闲教室、学术成果等

- 学工系统：离校、奖学金、违纪、请假、第二课堂等
  
  ## 内置漏洞

- 未授权访问

- 水平越权

- 垂直越权

- 弱权限校验

- 无 Cookie 身份校验

- 参数篡改
  

提供两种运行方案：
1. Python 本地直接运行（Kali虚拟机自用，无Docker依赖，推荐新手）
2. Docker 容器一键部署（标准化环境，统一运行环境）


## 环境前置准备（Kali Linux 通用）
### 方案一：Python本地运行前置依赖
```bash
# 更新软件源
sudo apt update
# 安装Python运行组件
sudo apt install python3 python3-pip python3-venv -y

方案二：Docker 容器部署前置依赖bash运行# 更新源并安装docker、docker-compose
sudo apt update
sudo apt install docker.io docker-compose -y
# 启动Docker并设置开机自启
sudo systemctl start docker
sudo systemctl enable docker
方式一：Python 本地启动靶场（虚拟机直跑，无容器）
进入靶场 lab 目录（路径不可出错）
bash
运行
cd ~/use_api_project/campus-api-docs/lab
创建并激活虚拟环境
bash
运行
python3 -m venv venv
source venv/bin/activate
激活成功后终端前缀会出现 (venv)。
安装项目全部依赖
bash
运行
pip3 install -r requirements.txt
初始化数据库（首次运行必须执行，生成账号与业务数据）
bash
运行
python3 init_db.py
启动靶场服务
bash
运行
python3 app.py
访问靶场
打开虚拟机浏览器访问：
plaintext
http://127.0.0.1:5000
日常启停操作
关闭服务：终端按下 Ctrl + C
退出虚拟环境：deactivate
下次快速启动：
bash
运行
cd ~/use_api_project/campus-api-docs/lab
source venv/bin/activate
python3 app.py
方式二：Docker 一键容器部署
进入 lab 目录（必须在此目录执行 docker-compose 命令，否则报配置文件不存在）
bash
运行
cd ~/use_api_project/campus-api-docs/lab
清理旧容器（更新代码后建议执行，首次部署可跳过）
bash
运行
sudo docker-compose down
构建镜像（修改 Dockerfile、代码、依赖后必须执行）
bash
运行
sudo docker-compose build --no-cache
后台启动靶场容器
bash
运行
sudo docker-compose up -d
查看运行状态与日志（排查报错专用）
bash
运行
# 查看容器是否正常运行
sudo docker-compose ps
# 查看实时运行日志
sudo docker-compose logs campus-lab
访问靶场
plaintext
http://127.0.0.1:5000
Docker 常用管理命令
bash
运行
# 仅停止容器，保留数据
sudo docker-compose stop

# 销毁容器，宿主机data目录数据库文件不会删除（数据持久化）
sudo docker-compose down

# 重启靶场服务
sudo docker-compose restart campus-lab
