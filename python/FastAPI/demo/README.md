# DEMO

# 1 启动
## 1.1 配置环境变量
修改envs中的文件

## 1.2 创建表
执行db/sqls/schema.sql

## 1.3 配置环境
```
pip install -r requirements.txt
```

## 1.4 启动
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 1.5 docs
```
http://127.0.0.1:8000/docs
```