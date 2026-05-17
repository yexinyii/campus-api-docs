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
  
  ## 快速启动
  
  pip install -r requirements.txt
  python app.py
  访问：http://127.0.0.1:5000

- ## 🐳 一键 Docker 启动
  
  如果你本地安装了 Docker 和 Docker Compose，只需两条命令启动靶场：
  
  ```bash
  docker-compose build
  docker-compose up -d
  
  
访问靶场：

[http://127.0.0.1:5000](http://127.0.0.1:5000)

停止靶场：

bash

运行

```
docker-compose down
```

## 具体接口文档目录

/api/01-统一认证.md
/api/02-教务系统认证.md
/api/03-学工系统认证.md

## 声明

本项目仅用于学习与教学，禁止用于非法渗透，使用后果自负。
