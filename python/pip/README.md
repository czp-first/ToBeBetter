## pip package conflict
```shell
pip install -r requirements.txt --no-deps
```

## 配置pip源
### 临时
```shell
pip install 包名 -i 源地址
```

### 永久
```shell
pip config set global.index-url 源地址
```

### 国内源
```shell
https://mirrors.aliyun.com/pypi/simple/  # ali

```