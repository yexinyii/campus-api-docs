Campus API Lab 校园教务模拟靶场

## 项目介绍

本靶场基于仓库脱敏校园业务接口开发，完整复刻高校统一认证、课表查询、空闲教室、学工请假、奖助申请等真实业务逻辑。

靶场内置多类接口安全漏洞：未授权访问、水平 / 垂直越权、参数篡改、敏感信息泄露等，专门用于 Web 安全、接口安全实训练习。

提供两种运行方案：

1. Python 本地直接运行（Kali 虚拟机自用，无 Docker 依赖，推荐新手）
2. Docker 容器一键部署（标准化环境，统一运行环境）

> 声明：项目所有账号、教室、课程数据均为模拟脱敏数据，不含任何学校真实信息，仅用于网络安全学习研究。

##

## 环境前置准备（Kali Linux 通用）

### 方案一：Python 本地运行前置依赖

bash

运行

```
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

### 方案二：Docker 容器部署前置依赖

bash

运行

```
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl start docker
sudo systemctl enable docker
```

## 方式一：Python 本地启动靶场（虚拟机直跑，无容器）

1. 进入靶场 lab 目录

bash

运行

```
cd ~/use_api_project/campus-api-docs/lab
```

1. 创建并激活虚拟环境

bash

运行

```
python3 -m venv venv
source venv/bin/activate
```

激活成功后终端前缀会出现 `(venv)`。

1. 安装项目全部依赖

bash

运行

```
pip3 install -r requirements.txt
```

1. 初始化数据库（首次运行必须执行）

bash

运行

```
python3 init_db.py
```

1. 启动靶场服务

bash

运行

```
python3 app.py
```

1. 访问靶场
  
  浏览器访问：`http://127.0.0.1:5000`
  

### 日常启停操作

- 关闭服务：`Ctrl + C`
- 退出虚拟环境：`deactivate`
- 快速启动命令：

bash

运行

```
cd ~/use_api_project/campus-api-docs/lab
source venv/bin/activate
python3 app.py
```

## 方式二：Docker 一键容器部署

1. 进入 lab 目录

bash

运行

```
cd ~/use_api_project/campus-api-docs/lab
```

1. 清理旧容器（更新代码后执行，首次部署可跳过）

bash

运行

```
sudo docker-compose down
```

1. 构建镜像（修改 Dockerfile / 代码 / 依赖后必执行）

bash

运行

```
sudo docker-compose build --no-cache
```

1. 后台启动靶场容器

bash

运行

```
sudo docker-compose up -d
```

1. 查看运行状态与日志

bash

运行

```
sudo docker-compose ps
sudo docker-compose logs campus-lab
```

1. 访问靶场
  
  浏览器访问：`http://127.0.0.1:5000`
  

### Docker 常用管理命令

bash

运行

```
# 仅停止容器，保留数据
sudo docker-compose stop

# 销毁容器，宿主机data目录数据库文件不会删除
sudo docker-compose down

# 重启靶场服务
sudo docker-compose restart campus-lab
```

## 常见报错问题排查

### 1. docker-compose 提示 no configuration file provided

原因：终端当前路径不是 lab 文件夹

解决：执行 `cd ~/use_api_project/campus-api-docs/lab` 切换目录后重试

### 2. 浏览器访问页面连接拒绝

1. Python 本地运行：确认 `app.py` 启动代码为 `app.run(host="0.0.0.0", port=5000)`
2. Docker 部署：执行 `sudo docker-compose logs campus-lab` 查看启动报错

### 3. 登录页面无用户、查询空白无数据

原因：未执行数据库初始化

- Python 本地：重新运行 `python3 init_db.py`
- Docker 部署：重新构建镜像 `sudo docker-compose build --no-cache`

### 4. 5000 端口被占用

修改 `docker-compose.yml` 端口映射为 `5001:5000`，访问地址改为 `http://127.0.0.1:5001`

## 靶场实训说明

1. 所有页面接口与仓库 `api/` 文件夹内接口文档一一对应，可对照文档复现漏洞；
2. 推荐使用 Burp Suite 抓包拦截请求，修改参数练习各类接口漏洞；
3. 可自主拓展：优化前端 UI、新增图书馆 / 一卡通业务、增加 SQL 注入等高阶漏洞场景。

## 重要注意事项

1. 本项目仅用于网络安全学习实训，禁止用于非法测试真实校园系统；
2. Docker 部署模式下，`lab/data` 目录持久化存储数据库，删除容器数据不会丢失；
3. 仅本地虚拟机访问使用，切勿将靶场服务暴露至公网；
4. 普通使用者仅允许本地运行练习，禁止修改源码并提交至仓库。

---

#

### 方案二：Docker 容器部署前置依赖

bash

运行

```
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl start docker
sudo systemctl enable docker
```

## 方式一：Python 本地启动靶场（虚拟机直跑，无容器）

1. 进入靶场 lab 目录

bash

运行

```
cd ~/use_api_project/campus-api-docs/lab
```

1. 创建并激活虚拟环境

bash

运行

```
python3 -m venv venv
source venv/bin/activate
```

激活成功后终端前缀会出现 `(venv)`。

1. 安装项目全部依赖

bash

运行

```
pip3 install -r requirements.txt
```

1. 初始化数据库（首次运行必须执行）

bash

运行

```
python3 init_db.py
```

1. 启动靶场服务

bash

运行

```
python3 app.py
```

1. 访问靶场
  
  浏览器访问：`http://127.0.0.1:5000`
  

### 日常启停操作

- 关闭服务：`Ctrl + C`
- 退出虚拟环境：`deactivate`
- 快速启动命令：

bash

运行

```
cd ~/use_api_project/campus-api-docs/lab
source venv/bin/activate
python3 app.py
```

## 方式二：Docker 一键容器部署

1. 进入 lab 目录

bash

运行

```
cd ~/use_api_project/campus-api-docs/lab
```

1. 清理旧容器（更新代码后执行，首次部署可跳过）

bash

运行

```
sudo docker-compose down
```

1. 构建镜像

bash

运行

```
sudo docker-compose build --no-cache
```

1. 后台启动靶场容器

bash

运行

```
sudo docker-compose up -d
```

1. 查看运行状态与日志

bash

运行

```
sudo docker-compose ps
sudo docker-compose logs campus-lab
```

1. 访问靶场
  
  浏览器访问：`http://127.0.0.1:5000`
  

### Docker 常用管理命令

bash

运行

```
# 仅停止容器，保留数据
sudo docker-compose stop

# 销毁容器，宿主机data目录数据库文件不会删除
sudo docker-compose down

# 重启靶场服务
sudo docker-compose restart campus-lab
```

##

## 常见报错问题排查

### 1. docker-compose 提示 no configuration file provided

原因：终端当前路径不是 lab 文件夹

解决：执行 `cd ~/use_api_project/campus-api-docs/lab` 切换目录后重试

### 2. 浏览器访问页面连接拒绝

1. Python 本地运行：确认 `app.py` 启动代码为 `app.run(host="0.0.0.0", port=5000)`
2. Docker 部署：执行 `sudo docker-compose logs campus-lab` 查看启动报错

### 3. 登录页面无用户、查询空白无数据

原因：未执行数据库初始化

- Python 本地：重新运行 `python3 init_db.py`
- Docker 部署：重新构建镜像 `sudo docker-compose build --no-cache`

### 4. 5000 端口被占用

修改 `docker-compose.yml` 端口映射为 `5001:5000`，访问地址改为 `http://127.0.0.1:5001`

## 靶场实训说明

1. 所有页面接口与仓库 `api/` 文件夹内接口文档一一对应，可对照文档复现漏洞；
2. 推荐使用 Burp Suite 抓包拦截请求，修改参数练习各类接口漏洞；
3. 可自主拓展：优化前端 UI、新增图书馆 / 一卡通业务、增加 SQL 注入等高阶漏洞场景。

## 重要注意事项

1. 本项目仅用于网络安全学习实训，禁止用于非法测试真实校园系统；
2. Docker 部署模式下，`lab/data` 目录持久化存储数据库，删除容器数据不会丢失；
3. 仅本地虚拟机访问使用，切勿将靶场服务暴露至公网；
4. 普通使用者仅允许本地运行练习，禁止修改源码并提交至仓库。

---

### 基础信息

- 靶场地址：`http://127.0.0.1:5000`
- 技术栈：Python + Flask
- 内置模块：统一认证、教务系统、学工系统
- 核心漏洞类型：未授权访问、水平 / 垂直越权、参数篡改、弱校验
