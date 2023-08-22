# djangoProject

## 目录结构

## 目录结构
![image](https://github.com/Yuan1z0825/djangoProject/assets/140061814/d1ad5609-e4b9-4157-86b2-a5c3dfe4fa23)

### 1.一级目录下的static不用动
其可以在完成修改后通过 python manage.py collectstatic命令生成，本地可以不生成，但是linux服务器需要nginx启动web 服务加载静态文件。



## 修改页面内容

### 调整HTML文件

要调整页面内容，您可以编辑 `app01/templates` 目录中的HTML文件。您可以根据需要更改文本、添加新元素或调整布局。

### 更新图片和文字

如果想更改页面上的图片或文字，您可以在 `static/img` 目录中替换或添加新的图片文件。确保在HTML文件中正确引用这些图片的路径。

## 添加新页面

要在Django项目中添加新页面，您需要执行以下步骤：

### 1. 在视图（views）中添加处理URL的函数

打开 `app01/views.py` 文件，并添加一个新的视图函数。以下是一个示例函数，用于渲染名为 `new_page.html` 的新页面：

```python
from django.shortcuts import render

def new_page(request):
    return render(request, 'app01/new_page.html')
```
### 2. 在URLs文件中找到对应页面的路径
打开 djangoProject/urls.py 文件，并导入您在上一步中创建的视图函数。然后，在 urlpatterns 列表中添加一个新的URL模式，以便将URL映射到新的视图函数。以下是一个示例(也可以根据已有代码学习)：

```python
from django.urls import path
from app01.views import new_page

urlpatterns = [
    # 其他URL模式
    path('new-page/', new_page, name='new_page'),
]
```

### 3. 创建HTML模板
在 app01/templates 目录中创建一个名为 new_page.html 的新HTML文件，并添加您想在新页面上显示的内容。


## 如何开始

1. 确保已安装所有必需的依赖项，可以通过运行 `pip install -r requirements.txt` 来安装。
2. 运行 `python manage.py runserver` 以启动开发服务器。
3. 打开浏览器并导航到 `http://localhost:8000` 以查看您的更改。

## 联系

如果遇到任何问题或需要进一步的帮助，请随时联系。

---

感谢您对本项目的兴趣！
