# Django

## 參考資源

- [GitHub Django](https://github.com/django/django)
- [Django Website](https://www.djangoproject.com/)
- [MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django)

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

## 資料夾結構

```plaintext
<repository_name>/
├── manage.py                           # Django 專案管理指令工具
├── <project_name>/                     # 專案設定資料夾
│   ├── __init__.py
│   ├── settings.py                     # 專案全域設定檔 (資料庫、靜態檔案、App 清單等)
│   ├── urls.py                         # 專案主路由設定檔
│   ├── asgi.py                         # ASGI 伺服器進入點 (支援非同步和 WebSocket)
│   └── wsgi.py                         # WSGI 伺服器進入點 (傳統同步請求)
└── <app_name>/                         # 應用程式資料夾 (功能模組)
    ├── __init__.py
    ├── admin.py                        # Admin 後台管理設定
    ├── apps.py                         # App 設定類別
    ├── models.py                       # 資料模型定義 (ORM 對應資料庫表結構)
    ├── tests.py                        # 單元測試檔案
    ├── urls.py                         # App 路由設定檔
    ├── views.py                        # 視圖函式 (處理請求與回應邏輯)
    ├── media/                          # 使用者上傳的媒體檔案 (如圖片、影片)
    ├── migrations/                     # 資料庫遷移檔案資料夾
    │   └── __init__.py
    ├── static/                         # 靜態檔案根目錄
    │   └── <app_name>/
    │       ├── *.css
    │       └── images/
    │           └── *.png
    └── templates/                      # Template 模板根目錄
        └── <app_name>/
            └── *.html
```

## 請求回應結構

```plaintext
[Browser]
  │  HTTP/JSON
  │
  ▼
[Web Server 反向代理: Nginx/Apache]
  │  WSGI/ASGI    # 靜態檔案 (static/) 和 媒體檔案 (media/) 可直接服務
  │
  ▼
[WSGI/ASGI Server: gunicorn/uWSGI/uvicorn/daphne]
  │  匯入 <project_name>/wsgi.py 或 <project_name>/asgi.py
  │
  ▼
[Django 專案]
  ├─ settings.py    # 全域設定
  ├─ urls.py        # 路由總表
  ├─ middleware     # 請求回應的中間處理 (認證、權限、日誌、CSRF、Session 等)
  └─ <app_name>/    # 專案 App
        ├─ urls.py           # 路由設定 (URL ↔ Views)
        ├─ views.py          # 實作邏輯 (接收參數、查詢資料、回傳 JSON/HTML)
        └─ models.py         # 資料模型 (Django ORM ↔ 資料庫)
            │
            │
            ▼
        [Django ORM] ↔ [DATABASES]
```

## MTV 和其他常用功能介紹

以下假設專案名稱為 `mdn_example`，App 名稱為 `catalog`。

### Settings

- 使用 `django-environ` 套件來管理環境變數，並在 `mdn_example/settings.py` 中載入。
    ```python
    # mdn_example/settings.py
    import environ
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent.parent

    env = environ.Env(DEBUG=(bool, False))
    ENV_FILE = BASE_DIR / '.env'
    env.read_env(str(ENV_FILE))

    DEBUG = env('DEBUG')
    SECRET_KEY = env('SECRET_KEY')
    ```

### Admin

- 使用 `admin.site.register()` 來註冊 Models 到 Admin 後台。
    ```python
    # catalog/admin.py
    from django.contrib import admin
    from catalog.models import MyModelName

    admin.site.register(MyModelName)
    ```
- 使用 `ModelAdmin` 來自訂 Admin 顯示選項。
    ```python
    # catalog/admin.py
    from django.contrib import admin
    from catalog.models import MyModelName


    class MyModelNameAdmin(admin.ModelAdmin):
        pass


    admin.site.register(MyModelName, MyModelNameAdmin)
    ```
- 使用 `@admin.register()` 裝飾器來註冊 Models 到 Admin 後台，並自訂 Admin 顯示選項。
    - `list_display`： 設定列表頁顯示的欄位。無法顯示 ManyToManyField 欄位。
    - `list_filter`： 設定可篩選的欄位。
    - `search_fields`： 設定可搜尋的欄位。
    - `fields`： 設定表單顯示的欄位順序。不可與 `fieldsets` 同時使用。
    - `fieldsets`： 設定表單欄位分組與標題。不可與 `fields` 同時使用。
    - `inline`： 設定內嵌顯示相關模型資料。可使用 `TabularInline` 或 `StackedInline` 來設定內嵌樣式。
    ```python
    # catalog/admin.py
    from django.contrib import admin
    from catalog.models import MyModelName


    class MyModelNameInstanceInline(admin.TabularInline):
        """Inline admin configuration for MyModelName model with one instance limit."""

        model = MyModelNameInstance
        extra = 0             # 不顯示額外的空白表單
        max_num = 1           # 最多只能有一個 MyModelName
        can_delete = False    # 不允許在這裡刪除


    @admin.register(MyModelName)
    class MyModelNameAdmin(admin.ModelAdmin):
        list_display = ('field1', 'field2', 'field3')
        list_filter = ('field1', 'field2')
        search_fields = ('field1', 'field2')
        # fields = ['field1', ('field2', 'field3')]
        fieldsets = (
            ('Section 1', {
                'fields': ('field1', 'field2')
            }),
            ('Section 2', {
                'fields': ('field3', 'field4')
            }),
        )
        inlines = [MyModelNameInstanceInline]
    ```

### Urls

- 使用 `path()` 來定義 URL 路徑，支援動態參數。
    - 使用 `include()` 來包含其他 URL 配置，方便管理大型專案的路由。
    - 使用 `app_name` 來設定應用程式命名空間，避免不同 App 的 URL 名稱衝突。
    ```python
    # mdn_example/urls.py
    from django.contrib import admin
    from django.urls import include, path
    from django.views.generic import RedirectView

    urlpatterns = [
        path("admin/", admin.site.urls),
    ]

    urlpatterns += [
        path("catalog/", include("catalog.urls")),
        path("", RedirectView.as_view(url="catalog/", permanent=True)),
    ]
    ```
    ```python
    # catalog/urls.py
    from django.urls import path, re_path

    from catalog import views

    app_name = "catalog"
    urlpatterns = [
        path("index/", views.index, name="index"),
        path("<int:question_id>/detail/", views.detail, name="detail"),
        path("<int:question_id>/results/", views.results, name="results"),
        path("<int:question_id>/vote/", views.vote, name="vote"),
    ]
    ```
- 使用 `re_path()` 來定義使用正則表達式的 URL 路徑。
    ```python
    # catalog/urls.py
    from django.urls import re_path

    from catalog import views

    urlpatterns = [
        re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive, name="year_archive"),
    ]
    ```
- 靜態檔案 URL 設定。
    ```python
    # mdn_example/urls.py
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ```

### Models

- 常用的模型欄位與方法：
    ```python
    from django.db import models

    models.Model    # 所有模型都繼承自這個類別

    models.CASCADE        # 外鍵刪除時，會連帶刪除相關物件
    models.PROTECT        # 外鍵刪除時，會阻止刪除相關物件
    models.RESTRICT       # 外鍵刪除時，會阻止刪除相關物件
    models.SET_NULL       # 外鍵刪除時，會將相關物件的外鍵設為 NULL
    models.SET_DEFAULT    # 外鍵刪除時，會將相關物件的外鍵設為預設值
    models.DO_NOTHING     # 外鍵刪除時，不執行任何操作
    models.SET()          # 外鍵刪除時，會將相關物件的外鍵設為指定值

    models.ForeignKey         # 外鍵欄位
    models.OneToOneField      # 一對一欄位
    models.ManyToManyField    # 多對多欄位

    models.CharField          # 字串欄位
    models.TextField          # 文字欄位
    models.EmailField         # 電子郵件欄位
    models.FileField          # 檔案欄位
    models.ImageField         # 圖片欄位

    models.DateTimeField      # 日期時間欄位
    models.DateField          # 日期欄位

    models.AutoField               # 自動增量欄位
    models.BigAutoField            # 大型自動增量欄位
    models.SmallAutoField          # 小型自動增量欄位
    models.IntegerField            # 整數欄位
    models.PositiveIntegerField    # 正整數欄位
    models.UUIDField               # UUID 欄位

    models.Manager            # 自訂模型管理器
    models.QuerySet           # 查詢集
    models.F                  # 用於查詢和更新的欄位參考
    models.Q                  # 用於複雜查詢的條件組合
    models.Avg                # 聚合函式
    models.Count              # 聚合函式
    models.Max                # 聚合函式
    models.Min                # 聚合函式
    models.Sum                # 聚合函式

    models.URLField           # URL 欄位
    models.FloatField         # 浮點數欄位
    models.BooleanField       # 布林欄位
    models.DecimalField       # 十進位欄位
    models.SlugField          # 簡短標識符欄位
    models.TimeField          # 時間欄位
    models.BinaryField        # 二進位欄位
    models.JSONField          # JSON 欄位
    models.PositiveSmallIntegerField    # 小型正整數欄位
    models.SlugField          # 簡短標識符欄位
    models.TextChoices        # 用於定義選項的類別
    models.IntegerChoices     # 用於定義選項的類別
    models.UUIDChoices        # 用於定義選項的類別
    ```
- 模型欄位常用參數：
    - `verbose_name`：欄位的顯示名稱。
    - `help_text`：欄位的說明文字。
    - `default`：設定欄位的預設值。
    - `null`：是否允許欄位為 NULL。
    - `blank`：是否允許欄位為空白。
    - `unique`：是否設定欄位值唯一。
    - `primary_key`：是否設定欄位為主鍵。

    - `max_length`：設定字串欄位的最大長度。
    - `choices`：設定欄位的選項。

    - `auto_now`：設定日期時間欄位在每次儲存時自動更新為當前時間。
    - `auto_now_add`：設定日期時間欄位在建立時自動設定為當前時間。

    - `on_delete`：外鍵刪除時的行為設定。
    - `db_index`：是否為欄位建立索引。
    - `related_name`：設定反向關聯的名稱。
- 常用的模型操作：
    ```python
    # example_app/models.py
    from django.db import models
    from django.urls import reverse

    class Question(models.Model):
        question_text = models.CharField(max_length=200)

        class Meta:
            ordering = ["question_text"]    # 預設排序方式，使用 - 則表示降冪 Descending

        def get_absolute_url(self):
            return reverse("example_app:question_detail", args=[str(self.id)])

        def __str__(self):
            return self.question_text


    p = Question(question_text="Sample Question")

    p.save()    # 將物件儲存到資料庫
    p.delete()    # 刪除物件

    Question.objects.all()    # 查詢所有問題
    # https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups
    Question.objects.get(id=1)    # 根據 ID 查詢單一問題
    Question.objects.get(pk=1)    # 根據主鍵查詢單一問題
    Question.objects.filter(question_text__in=["Sample", "Test"])    # 查詢名稱在指定清單中的問題
    Question.objects.filter(question_text__exact="Sample")    # 查詢名稱完全等於 "Sample" 的問題
    Question.objects.filter(question_text__contains="Product")    # 查詢名稱包含 "Product" 的問題
    Question.objects.filter(question_text__startswith="Sample")    # 查詢名稱以 "Sample" 開頭的問題
    Question.objects.filter(question_text__endswith="Sample")    # 查詢名稱以 "Sample" 結尾的問題
    Question.objects.exclude(id=1)    # 排除 ID 為 1 的問題

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
- 支援 Template 繼承，使用 `{% extends "base.html" %}` 來繼承基礎 Template。
    - 使用 `{% block content %}...{% endblock content %}` 來定義可覆寫的區塊。
- 支援過濾器 (Filters) 來格式化輸出。
    - `{{ variable|lower }}` 將變數轉為小寫。
    - `{{ variable|date:"Y-m-d" }}` 將日期格式化為 "年-月-日"。
- 支援靜態檔案 (Static Files) 的載入。
    - 使用 `{% load static %}` 來載入靜態檔案標籤庫。
    - 使用 `{% static '<app_name>/<filename>' %}` 來取得靜態檔案的絕對 URL。
        - 例如：`<link rel="stylesheet" href="{% static 'example_app/style.css' %}">`
- 支援 URL 反轉 (URL Reversing)。
    - `{% url 'view_name' arg1 arg2 %}` 生成 URL。
    - 在 `urls.py` 使用 `app_name` 來設定應用程式命名空間，避免不同 App 的 URL 名稱衝突。
       - 例如在 `example_app/urls.py` 設定 `app_name = "example_app"`，即可在 Template 使用 `{% url 'example_app:view_name' arg1 arg2 %}`。
- 支援 CSRF 保護。
    - `{% csrf_token %}` 用於防止跨站請求偽造 (CSRF) 攻擊，通常在表單中使用。

#### Static Files

- 在 `mysite/settings.py` 中設定靜態檔案路徑。
    ```python
    # mysite/settings.py
    STATIC_URL = 'static/'    # 設定靜態檔案的 URL 前綴
    ```
- `django.contrib.staticfiles` App 會自動尋找已安裝 App 中的 `static` 資料夾。
    - 例如：`example_app/static/example_app/style.css`


### Views

- Views 負責處理使用者請求和回應，從 Model 獲取資料並將其傳遞給 Template 進行渲染，然後返回給使用者。
    - 使用 `loader.get_template` 來載入 Template，並使用 `template.render(context, request)` 來渲染 Template，並返回 HTTP 回應。
    - 使用 `render` 和 `get_object_or_404` 來簡化載入和渲染 Template 的過程。
    ```python
    # example_app/views.py
    from django.http import Http404, HttpResponse, HttpResponseRedirect
    from django.shortcuts import get_object_or_404, redirect, render
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
    python manage.py runserver [<port>|<ip_addr:port>]    # 預設為 http://127.0.0.1:8000/
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
