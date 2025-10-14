# Django

## 參考資源
- [GitHub Django](https://github.com/django/django)
- [Django Website](https://www.djangoproject.com/)

## 什麼是 Django?

- Django 是一個免費開源的 Python Web 開發框架，能快速開發安全且易於維護的網站，它提供了物件關聯對映器 (ORM)、URL 分發、視圖處理、模板系統等核心組件，能應對網站開發中常見的認證、快取、表單處理等功能，讓開發者專注於應用程式本身，而無需重複建構基礎設施。
- Django 採用 MTV (Model-Template-View) 架構，與傳統的 MVC (Model-View-Controller) 架構相似，但名稱不同。
    - Model： 負責資料庫結構和資料操作，使用 Django 的 ORM (Object-Relational Mapping) 來定義資料模型並與資料庫互動。
    - Template： 負責呈現資料的 HTML 模板，使用 Django 的模板語言來動態生成 HTML 頁面。
    - View： 負責處理使用者請求和回應，從 Model 獲取資料並將其傳遞給 Template 進行渲染，然後返回給使用者。

## 安裝方式

- 確認 Python 版本支援 Django。
    - [Django 各版本支援的 Python 版本說明](https://docs.djangoproject.com/en/dev/faq/install/#faq-python-version-support)。
- 透過 uv 安裝。
    ```bash
    uv add django
    uv add djangorestframework
    ```
- 檢查安裝版本。
    ```bash
    uv run -m django --version
    ```

## 建立第一個 Django 專案

- 建立 Django 專案。
    - 建立 `django_example` 資料夾，並在其中建立名為 `mysite` 的 Django 專案。
        ```bash
        mkdir django_example
        django-admin startproject mysite django_example
        cd django_example
        ```
    - 專案結構如下：
        ```bash
        django_example/
            manage.py
            mysite/
                __init__.py
                settings.py
                urls.py
                asgi.py
                wsgi.py
        ```
- 啟動開發伺服器。
    - `runserver` 會自動重載程式碼變更，但某些動作不會觸發重載，例如：新增檔案。
    ```bash
    python manage.py runserver <port>    # 預設在 http://127.0.0.1:8000/
    ```
- 建立 Django App。
    - 建立名為 `example_app` 的 App。
    ```bash
    python manage.py startapp example_app
    ```
    - 專案結構如下：
        ```bash
        django_example/
            manage.py
            mysite/
                __init__.py
                settings.py
                urls.py
                asgi.py
                wsgi.py
            example_app/
                __init__.py
                admin.py
                apps.py
                models.py
                tests.py
                views.py
                migrations/
                    __init__.py
        ```
- 設定檔 `mysite/settings.py` 說明。
    - 在 `INSTALLED_APPS` 中加入剛建立的 App `example_app.apps.ExampleAppConfig`。
    ```python
    # mysite/settings.py
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent.parent    # 專案根目錄

    DEBUG = True    # 開發模式，Production 環境請設定為 False
    ALLOWED_HOSTS = []    # 允許的主機清單，Production 環境請設定為你的網域名稱或 IP 位址

    INSTALLED_APPS = [    # 已安裝的 App 清單
        'example_app.apps.ExampleAppConfig',    # 新增自訂的 App
        'django.contrib.admin',    # 管理後台
        'django.contrib.auth',    # 認證系統
        'django.contrib.contenttypes',    # 內容類型系統
        'django.contrib.sessions',    # Session 支援
        'django.contrib.messages',    # 訊息框架
        'django.contrib.staticfiles',    # 靜態檔案管理
    ]

    ROOT_URLCONF = 'mysite.urls'    # 專案的 URL 設定檔

    DATABASES = {    # 資料庫設定，預設使用 SQLite
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',    # 使用 SQLite 資料庫
            'NAME': BASE_DIR / 'db.sqlite3',    # 資料庫檔案位置
        }
    }

    TIME_ZONE = 'Asia/Taipei'    # 設定時區，預設為 UTC
    ```
- 建立資料庫的表，會根據 `mysite/settings.py` 中的 `INSTALLED_APPS` 來建立資料表。
    - 若 `example_app/models.py` 有變更，都需要先執行 Migration 來同步資料庫。
    ```bash
    python manage.py makemigrations    # 產生遷移檔
    python manage.py migrate    # 執行遷移

    python manage.py showmigrations    # 顯示遷移狀態
    ```
- 查看特定遷移檔的 SQL 語句。
    - `ForeignKey` 會在欄位名稱的後綴自動加上 `_id`。
    ```bash
    python manage.py sqlmigrate example_app 0001    # 查看 example_app 的 0001_initial 遷移檔的 SQL 語句
    ```
- 建立 Admin 使用者，建立完成後，可以透過 `http://127.0.0.1:8000/admin/` 登入後台管理介面。
    ```bash
    python manage.py createsuperuser
    ```
    - 註冊模型到 Admin 後台，可透過 Admin 後台進行資料表的管理。
        ```python
        # example_app/admin.py
        from django.contrib import admin
        from . import models

        admin.site.register(models.YourModel)
        ```
- 建立 `example_app/templates` 資料夾，並在 `mysite/settings.py` 中設定 Template 路徑。
    - `APP_DIRS` 設定為 `True`，表示會自動尋找已安裝 App 中的 `templates` 資料夾。
    - 在 `example_app/templates` 資料夾中，再建立 `example_app` 資料夾，避免 Template 名稱衝突。
        - 例如：`example_app/templates/example_app/index.html`
    ```python
    # mysite/settings.py
    from pathlib import Path

    ...

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```
- 開始撰寫 Model、Template 和 View。
    - 可參考 Django 官方文件的 [Writing your first Django app](https://docs.djangoproject.com/en/dev/intro/tutorial01/) 教學。
    - 在 `example_app/models.py` 中撰寫資料模型。
    - 在 `example_app/templates/example_app/` 中撰寫 HTML Template。
    - 在 `example_app/views.py` 中撰寫 View 函式，並在 `example_app/urls.py` 中設定 URL 路由。
    - 在 `mysite/urls.py` 中包含 `example_app/urls.py` 的路由設定。
- 使用 Django Shell 進行資料操作。
    ```bash
    python manage.py shell
    ```
    - 新增 Question 資料。
        ```python
        Question.objects.all()
        #> <QuerySet []>
        from django.utils import timezone
        q = Question(question_text="What's new?", pub_date=timezone.now())
        #> <Question: Question object (None)>
        q
        #> <Question: What's new?>
        q.id
        q.save()
        q.id
        #> 1
        q.question_text
        #> "What's new?"
        q.pub_date
        #> datetime.datetime(2025, 10, 14, 6, 34, 29, 482639, tzinfo=datetime.timezone.utc)
        Question.objects.all()
        #> <QuerySet [<Question: What's new?>]>
        ```
    - 查詢 Question 資料。
        ```python
        Question.objects.filter(id=1)
        #> <QuerySet [<Question: What's new?>]>
        Question.objects.filter(question_text__startswith="What")
        #> <QuerySet [<Question: What's new?>]>
        Question.objects.get(id=1)
        #> <Question: What's new?>
        Question.objects.get(pk=1)
        #> <Question: What's new?>
        Question.objects.count()
        #> 1
        ```
    - 新增 Choice 資料。
        ```python
        Choice.objects.all()
        #> <QuerySet []>
        q.choice_set.all()
        #> <QuerySet []>

        q.choice_set.create(choice_text="Not much", votes=0)
        #> <Choice: Not much>
        q.choice_set.create(choice_text="The sky", votes=0)
        #> <Choice: The sky>
        q.choice_set.create(choice_text="Just hacking again", votes=0)
        #> <Choice: Just hacking again>

        Choice.objects.all()
        #> <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
        q.choice_set.all()
        #> <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
        q.choice_set.count()
        #> 3
        Choice.objects.count()
        #> 3
        ```

## MTV 和其他常用功能介紹

以下假設專案名稱為 `mysite`，App 名稱為 `example_app`。

### Admin

- 使用 `admin.site.register()` 來註冊 Models 到 Admin 後台。
    ```python
    # example_app/admin.py
    from django.contrib import admin
    from example_app import models

    admin.site.register(models.Question)
    admin.site.register(models.Choice)
    ```

### Urls

- 使用 `path()` 來定義 URL 路徑，支援動態參數。
    - 使用 `include()` 來包含其他 URL 配置，方便管理大型專案的路由。
    - 使用 `app_name` 來設定應用程式命名空間，避免不同 App 的 URL 名稱衝突。
    ```python
    # mysite/urls.py
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("poll/", include("example_app.urls")),
    ]
    ```
    ```python
    # example_app/urls.py
    from django.urls import path

    from example_app import views

    app_name = "example_app"
    urlpatterns = [
        path("index/", views.index, name="index"),
        path("index2/", views.index2, name="index2"),
        path("<int:question_id>/detail/", views.detail, name="detail"),
        path("<int:question_id>/detail2/", views.detail2, name="detail2"),
        path("<int:question_id>/results/", views.results, name="results"),
        path("<int:question_id>/vote/", views.vote, name="vote"),
        path("<int:question_id>/vote2/", views.vote2, name="vote2"),
    ]
    ```


### Models

- 常用的模型欄位與方法：
    ```python
    from django.db import models

    models.Model  # 所有模型都繼承自這個類別

    models.ForeignKey  # 外鍵欄位
    models.CharField  # 字串欄位
    models.TextField  # 文字欄位

    models.DateTimeField  # 日期時間欄位
    models.DateField  # 日期欄位

    models.IntegerField  # 整數欄位



    models.OneToOneField  # 一對一欄位
    models.ManyToManyField  # 多對多欄位
    models.CASCADE  # 外鍵刪除時的行為
    models.PROTECT  # 外鍵刪除時的行為
    models.SET_NULL  # 外鍵刪除時的行為
    models.SET_DEFAULT  # 外鍵刪除時的行為
    models.SET()  # 外鍵刪除時的行為
    models.DO_NOTHING  # 外鍵刪除時的行為
    models.Manager  # 自訂模型管理器
    models.QuerySet  # 查詢集
    models.F  # 用於查詢和更新的欄位參考
    models.Q  # 用於複雜查詢的條件組合
    models.Avg  # 聚合函式
    models.Count  # 聚合函式
    models.Max  # 聚合函式
    models.Min  # 聚合函式
    models.Sum  # 聚合函式

    models.EmailField  # 電子郵件欄位
    models.URLField  # URL 欄位
    models.FloatField  # 浮點數欄位
    models.BooleanField  # 布林欄位
    models.DecimalField  # 十進位欄位
    models.FileField  # 檔案欄位
    models.ImageField  # 圖片欄位
    models.SlugField  # 簡短標識符欄位
    models.TimeField  # 時間欄位
    models.UUIDField  # UUID 欄位
    models.BinaryField  # 二進位欄位
    models.JSONField  # JSON 欄位
    models.AutoField  # 自動增量欄位
    models.BigAutoField  # 大型自動增量欄位
    models.SmallAutoField  # 小型自動增量欄位
    models.PositiveIntegerField  # 正整數欄位
    models.PositiveSmallIntegerField  # 小型正整數欄位
    models.SlugField  # 簡短標識符欄位
    models.TextChoices  # 用於定義選項的類別
    models.IntegerChoices  # 用於定義選項的類別
    models.UUIDChoices  # 用於定義選項的類別
    ```
- 常用的模型操作：
    ```python
    # example_app/models.py
    from django.db import models


    class Question(models.Model):
        question_text = models.CharField(max_length=200)

        def __str__(self):
            return self.question_text


    p = Question(question_text="Sample Question")

    p.save()    # 將物件儲存到資料庫
    p.delete()    # 刪除物件
    Question.objects.all()    # 查詢所有問題
    Question.objects.get(id=1)    # 根據 ID 查詢單一問題
    Question.objects.get(pk=1)    # 根據主鍵查詢單一問題
    Question.objects.filter(question_text__startswith="Sample")    # 查詢名稱以 "Sample" 開頭的問題
    Question.objects.filter(question_text__contains="Product")    # 查詢名稱包含 "Product" 的問題
    Question.objects.order_by("question_text")    # 根據名稱排序
    Question.objects.count()    # 計算問題數量

    Question.choice_set.all()    # 查詢所有相關的選項 (假設有一對多關聯)
    Question.choice_set.count()    # 計算相關選項的數量
    Question.choice_set.create(choice_text="Choice1")    # 建立新的相關選項
    ```

### Templates

- 變數使用雙大括號 `{{ variable }}` 來插入資料。
- 控制流程使用 `{% %}` 來包裹指令，如條件判斷和迴圈。
    - 使用 `{% if condition %}...{% elseif condition %}...{% else %}...{% endif %}` 來進行條
    件判斷。
    - 使用 `{% for item in list %}...{% endfor %}` 來進行迴圈。
        - 使用 `forloop.counter` 來取得目前迴圈的次數 (從 1 開始)。
- 支援模板繼承，使用 `{% extends "base.html" %}` 來繼承基礎模板
    - 使用 `{% block content %}...{% endblock content %}` 來定義可覆寫的區塊。
- 支援過濾器 (Filters) 來格式化輸出。
    - `{{ variable|lower }}` 將變數轉為小寫。
    - `{{ variable|date:"Y-m-d" }}` 將日期格式化為 "年-月-日"。
- 支援靜態檔案 (Static Files) 的載入。
    - `{% load static %}` 載入靜態檔案標籤庫。
    - `<img src="{% static 'images/logo.png' %}" alt="Logo">` 使用靜態檔案。
- 支援 URL 反轉 (URL Reversing)。
    - `{% url 'view_name' arg1 arg2 %}` 生成 URL。
    - 在 `urls.py` 使用 `app_name` 來設定應用程式命名空間，避免不同 App 的 URL 名稱衝突。
       - 例如在 `example_app/urls.py` 設定 `app_name = "example_app"`，即可在 Template 使用 `{% url 'example_app:view_name' arg1 arg2 %}`。
- 支援 CSRF 保護。
    - `{% csrf_token %}` 用於防止跨站請求偽造 (CSRF) 攻擊，通常在表單中使用。

### Views

- Views 負責處理使用者請求和回應，從 Model 獲取資料並將其傳遞給 Template 進行渲染，然後返回給使用者。
    - 使用 `loader.get_template` 來載入 Template，並使用 `template.render(context, request)` 來渲染 Template，並返回 HTTP 回應。
    - 使用 `render` 和 `get_object_or_404` 來簡化載入和渲染 Template 的過程。
    ```python
    # example_app/views.py
    from django.http import Http404, HttpResponse, HttpResponseRedirect
    from django.shortcuts import get_object_or_404, render
    from django.template import loader
    from django.urls import reverse

    from example_app import models


    def index(request):
        latest_question_list = models.Question.objects.order_by("-pub_date")[:5]
        template = loader.get_template("example_app/index.html")
        context = {
            "latest_question_list": latest_question_list,
        }
        return HttpResponse(template.render(context, request))

    def index2(request):
        latest_question_list = models.Question.objects.order_by("-pub_date")[:5]
        context = {
            "latest_question_list": latest_question_list,
        }
        return render(request, "example_app/index.html", context)

    def detail(request, question_id):
        try:
            question = models.Question.objects.get(pk=question_id)
            context = {
                "question": question,
            }
        except models.Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, "example_app/detail.html", context)

    def detail2(request, question_id):
        question = get_object_or_404(models.Question, pk=question_id)
        context = {
            "question": question,
        }
        return render(request, "example_app/detail.html", context)

    def results(request, question_id):
        question = get_object_or_404(models.Question, pk=question_id)
        context = {
            "question": question,
        }
        return render(request, "example_app/results.html", context)

    def vote(request, question_id):
        question = get_object_or_404(models.Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, models.Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, "example_app/detail.html", {
                "question": question,
                "error_message": "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse("example_app:results", args=(question.id,)))

    def vote2(request, question_id):
        question = get_object_or_404(models.Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, models.Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, "example_app/detail.html", {
                "question": question,
                "error_message": "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            context = {
                "question_id": question.id,
            }
            return redirect("example_app:results", **context)
    ```

### Database Engine

- Django 支援多種資料庫引擎。
    - SQLite
        ```python
        # mysite/settings.py
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        ```
    - PostgreSQL (支援 14 或更高版本)
        - psycopg 3.1.8 或更高版本是必須的。
        - psycopg2 2.8.4 或更高版本是必須的。
        ```python
        # mysite/settings.py
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'mydatabase',
                'USER': 'myuser',
                'PASSWORD': 'mypassword',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
        ```
    - MySQL (支援 8.0.11 或更高版本) / MariaDB (支援 10.5 或更高版本)
        ```python
        # mysite/settings.py
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'mydatabase',
                'USER': 'myuser',
                'PASSWORD': 'mypassword',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
        ```
    - Oracle (支援 19c 或更高版本)
        - oracledb 2.3.0 或更高版本是必須的。
        ```python
        # mysite/settings.py
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.oracle',
                'NAME': 'mydatabase',
                'USER': 'myuser',
                'PASSWORD': 'mypassword',
                'HOST': 'localhost',
                'PORT': '1521',
            }
        }
        ```

### Command-line

- 建立 Django 專案。
    ```bash
    django-admin startproject <project_name>    # 建立資料夾 project_name，並在其中建立 Django 專案
    django-admin startproject <project_name> <directory_name>    # 在 directory_name 資料夾 (需先建立 directory_name 資料夾) 中建立 Django 專案
    ```
- 啟動開發伺服器。
    - `runserver` 會自動重載程式碼變更，但某些動作不會觸發重載，例如：新增檔案。
    ```bash
    python manage.py runserver <port>    # 預設在 http://127.0.0.1:8000/
    ```
- 建立 Django App。
    - Django 專案可以包含多個 App，App 是專案中的功能模組。
    ```bash
    python manage.py startapp <app_name>    # 在專案目錄中建立 app_name 資料夾
    ```
- 建立資料庫的表，會根據 `settings.py` 中的 `INSTALLED_APPS` 來建立資料表。
    - 若 `models.py` 有變更，都需要先執行 Migration 來同步資料庫。
    ```bash
    python manage.py makemigrations    # 產生遷移檔
    python manage.py migrate    # 執行遷移

    python manage.py showmigrations    # 顯示遷移狀態
    ```
- 查看特定遷移檔的 SQL 語句。
    - `ForeignKey` 會在欄位名稱的後綴自動加上 `_id`。
    ```bash
    python manage.py sqlmigrate <app_name> <migration_number>    # 查看 app_name 的 migration_number 遷移檔的 SQL 語句
    ```
- 建立 Admin 使用者，建立完成後，可以透過 `http://127.0.0.1:8000/admin/` 登入後台管理介面。
    ```bash
    python manage.py createsuperuser
    ```
- 檢查專案設定是否有誤。
    ```bash
    python manage.py check
    ```
- 開啟 Django shell。
    ```bash
    python manage.py shell
    ```
