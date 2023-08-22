# djangoProject

## 目录结构

'''
├── app01
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── static
│   ├── templates
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── djangoProject
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Dockerfile
├── manage.py
├── nginx.conf
├── requirements.txt
└── static
    ├── admin
    ├── css
    ├── img
    └── js
'''


## 修改页面内容

### 调整HTML文件

要调整页面内容，您可以编辑 `app01/templates` 目录中的HTML文件。您可以根据需要更改文本、添加新元素或调整布局。

### 更新图片和文字

如果您想更改页面上的图片或文字，您可以在 `static/img` 目录中替换或添加新的图片文件。确保在HTML文件中正确引用这些图片的路径。

## 如何开始

1. 确保您已安装所有必需的依赖项，可以通过运行 `pip install -r requirements.txt` 来安装。
2. 运行 `python manage.py runserver` 以启动开发服务器。
3. 打开浏览器并导航到 `http://localhost:8000` 以查看您的更改。

## 联系

如果您遇到任何问题或需要进一步的帮助，请随时联系我们。

---

感谢您对本项目的兴趣！
