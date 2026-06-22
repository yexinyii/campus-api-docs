FROM python:3.9-slim

# 安装基础工具，用于健康检查、时区
RUN apt-get update && apt-get install -y --no-install-recommends curl tzdata && rm -rf /var/lib/apt/lists/*
ENV TZ=Asia/Shanghai

WORKDIR /app

# 复制依赖安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制全部项目代码
COPY . .

# 提前初始化数据库（构建镜像时生成基础数据）
RUN python3 init_db.py

EXPOSE 5000

# 强制监听0.0.0.0，外部可访问
CMD ["python", "app.py", "--host=0.0.0.0"]
 
