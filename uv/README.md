# uv

## 參考資源
- [GitHub uv](https://github.com/astral-sh/uv)
- [uv Website](https://docs.astral.sh/uv/)

## 什麼是 uv?

- uv 是一個 Python 套件管理工具。
- 速度更快、效能更好。

## 安裝方式

透過 Scoop 安裝：

```
scoop install uv
uv --version
```

透過 Docker 安裝：

```
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
```

## 常用指令

以下列出一些常用的 uv 指令：

```
uv init         # 建立新專案
uv python       # 管理 Python 版本
uv venv         # 建立虛擬環境

uv tree         # 顯示專案依賴樹
uv add          # 新增 Python 套件
uv remove       # 移除 Python 套件
uv pip          # 以 pip 介面管理 Python 套件

uv lock         # 根據 pyproject.toml 更新 lockfile
uv sync         # 根據 lockfile 同步環境，不會安裝 optional 的 Python 套件
uv export       # 匯出 lockfile

uv run          # 在 .venv 執行指令或腳本，也可執行 .ps1、.cmd 和 .bat 腳本
uv tool         # 在 tool 環境或臨時環境執行指令或腳本
uv cache        # 管理快取

uv build        # 打包為套件，路徑為 <SRC>/dist/
uv publish      # 上傳套件
```

## 初始化環境

- 初始化專案 (會建立 `main.py`, `pyproject.toml`, `README.md`)。
    ```
    uv init                                         # 初始化專案
    ```
- 安裝 Python。
    ```
    uv python install 3.10                          # 安裝指定 Python 版本
    uv python install 3.10 3.11 3.12 3.13           # 安裝多個 Python 版本
    ```
- 指定目錄使用特定 Python 版本。
    ```
    uv python pin 3.13                              # 會建立 .python-version 檔案
    ```
- 建立虛擬環境。
    ```
    uv venv                                         # 依 .python-version 建立虛擬環境
    uv venv --python 3.13.0                         # 依指定版本建立虛擬環境
    ```

## 管理套件

- 安裝 Python 套件。
    ```
    uv add <PACKAGE>                                # 安裝指定的 Python 套件
    uv add -r requirements.txt                      # 安裝 requirements.txt 中的 Python 套件

    uv add --dev <PACKAGE>                          # 在 group dev 安裝 Python 套件
    ```
- 移除 Python 套件。
    ```
    uv remove <PACKAGE>                             # 移除指定的 Python 套件

    uv remove --dev <PACKAGE>                       # 在 group dev 移除 Python 套件
    ```
- 更新 Python 套件。
    ```
    uv lock -U                                      # 更新所有的 Python 套件
    uv lock --upgrade

    uv lock -P <PACKAGE>                            # 更新指定的 Python 套件
    uv lock --upgrade-package <PACKAGE>
    ```
- 顯示已安裝的 Python 套件。
    ```
    uv tree                                         # 顯示已安裝的 Python 套件
    uv tree -d 1                                    # 依指定深度顯示已安裝的 Python 套件

    uv tree --package <PACKAGE>                     # 僅顯示指定的 Python 套件
    uv tree --invert                                # 顯示反向的樹
    uv tree --outdated                              # 顯示可更新的 Python 套件
    uv tree --only-dev                              # 僅包含 group dev 的樹
    uv tree --no-dev                                # 不包含 group dev 的樹
    ```

## 管理環境

- 依 `pyproject.toml` 安裝 Python 套件至 `.venv`。
    ```
    uv sync
    ```
- 匯出 `requirements.txt`。
    ```
    uv export --no-hashes                           # 匯出 requirements.txt
    uv pip freeze > requirements.txt                # 匯出 requirements.txt
    ```
- 使用專案環境 (.venv) 執行指令或腳本。
    ```
    uv run <SCRIPT>                                 # 在 .venv 執行指令或腳本
    ```
- 使用臨時環境執行指令或腳本。
    ```
    uv tool run <SCRIPT>                            # 使用臨時環境執行指令或腳本
    uvx <SCRIPT>                                    # 使用臨時環境執行指令或腳本
    ```
- 在臨時環境管理 Python 套件。
    ```
    uv tool list                                    # 列出 tool 環境已安裝的 Python 套件
    uv tool install <PACKAGE>                       # 在 tool 環境安裝 Python 套件
    uv tool uninstall <PACKAGE>                     # 在 tool 環境移除 Python 套件
    uv tool upgrade                                 # 在 tool 環境更新 Python 套件
    ```
- 清除臨時環境。
    ```
    uv cache clean                                  # 清除全部的快取
    ```

## 進階應用

### 安裝套件和環境

- 安裝指定條件的 Python 套件。
    ```
    uv add "<PACKAGE> @ git+<URL>"                  # 依 GitHub url 安裝 Python 套件
    uv add "<PACKAGE>; sys_platform == 'linux'"     # 依指定平台安裝 Python 套件
    uv add "<PACKAGE>; python_version >= '3.10'"    # 依指定 Python 版本安裝 Python 套件
    ```
- 安裝 `project.optional-dependencies` 的 Python 套件。
    - 預設不會安裝 Optional 的套件。
    ```
    uv sync --extra <OPTIONAL>                      # 除了安裝 project.dependencies 以外，也要安裝指定的 project.optional-dependencies
    uv sync --all-extra                             # 除了安裝 project.dependencies 以外，也要安裝所有的 project.optional-dependencies
    ```

### uv run

- 在臨時環境安裝 `<PACKAGE>` 套件來執行命令或腳本，不會安裝 `<PACKAGE>` 在 `.venv` 中。
    ```
    uv run --with <PACKAGE> -- <SCRIPT>
    ```
- 使用 `--` 分隔 `uv run` 的參數和要執行的程式與其參數，避免執行的程式恰好是 `uv run` 的某個參數。
    ```
    uv run --with <PACKAGE> -- <SCRIPT>
    ```
- 直接呼叫套件中的指定函數，需要先新增設定檔，才能使用 uv 執行指定的函數。
    ```
    # pyproject.toml
    [project.scripts]
    hello = "example:hello"
    ```

    ```
    uv run hello
    ```

### 套件環境限制

- 將 lockfile 限制在特定環境下。
    - [Environment Markers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#environment-markers)
    ```
    # pyproject.toml
    [tool.uv]
    environments = [
        "sys_platform == 'darwin'",    # MacOS
        "sys_platform == 'linux'",     # Linux
    ]
    ```

### 套件索引

- uv 的套件索引預設使用 PyPI 來解析依賴和安裝 Python 套件，以下方式可使用其他套件索引。
    - 若同時被標記為 `default = true` 和 `explicit = true`，則會以 `explicit = true` 優先。
    ```
    # pyproject.toml
    [tool.uv.sources]
    torch = { index = "pytorch" }

    [[tool.uv.index]]
    name = "pytorch"                                # optional name for the index
    url = "https://download.pytorch.org/whl/cpu"    # required URL for the index
    default = true                                  # exclude PyPI from the list of indexes
    explicit = true                                 # prevent packages from being installed from that index unless explicitly pinned to it
    ```

    ```
    uv run --index <URL> -- <SCRIPT>
    uv run --index <URL> --default-index true -- <SCRIPT>
    ```

### 環境變數 .env

- 支援從 `.env` 檔案載入環境變數，需要設定 `UV_ENV_FILE` 或使用 `uv run --env-file <FILE>`。
    - 使用 `--env-file` 時，若檔案不存在，則會顯示錯誤。
    - 載入多個檔案時，需要以空格分隔路徑。
    - 停用載入環境變數，可使用 `UV_NO_ENV_FILE=1` 或 `uv run --no-env-file`。
    ```
    uv run --env-file .env -- <SCRIPT>
    uv run --env-file ".env1 .env2" -- <SCRIPT>
    ```
