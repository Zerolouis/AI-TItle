# AI-Title

AI-Title 项目后端

## 项目部署

建议配置虚拟Python环境运行

### 不使用虚拟环境

#### 安装依赖

```shell
pip3 install -r requirements.txt
```

#### 启动

```shell
python3 app.py
```

### 使用虚拟环境

```shell
# 确保安装了python虚拟环境
pip3 install virtualenv
# 在文件夹下创建虚拟环境
virtualenv venv
```

### 安装依赖

#### Windows

```shell
.\venv\Scripts\pip3.exe install -r requirements.txt
```

### Linux

```shell
./venv/bin/pip3 install -r requirements.txt
```

### 启动

#### Windows

```shell
.\venv\Scripts\python.exe .\app.py
```

#### Linux

```shell
./venv/bin/python3 ./app.py
```

### 启动完成

服务将运行于 http://localhost:5000

### 常见问题

由于使用了HuggingFace，您可能需要在Python中使用HuggingFace-CLI登录您的账户后才能继续运行本项目

使用方法请查看https://huggingface.co/docs/huggingface_hub/quick-start