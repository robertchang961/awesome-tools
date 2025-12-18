# Ruff

## 參考資源
- [GitHub Ruff](https://github.com/astral-sh/ruff)
- [Ruff Website](https://docs.astral.sh/ruff/)

## 什麼是 Ruff?

- Ruff 是一個 Python 的 linter 及 formatter。
- 可用來取代 flake8, isort, black, pydocstyle, pyupgrade, autoflake 等 linter 及 formatter。

## 安裝方式

透過 uv 安裝：

```
uv add --dev ruff
```

## 常用指令

- Ruff 會尋找以下檔案 `*.py`、`*.pyi`、`*.ipynb` 及 `pyproject.toml` 來檢查。
- Ruff 預設會啟用 `F` (Pyflakes) 和部分的 `E` (pycodestyle) 規則。

以下列出一些常用的 Ruff 指令：

### Lint

```
uv run ruff check                 # 檢查所有檔案的 lint
uv run ruff check --fix           # 檢查所有檔案的 lint，並修正錯誤
uv run ruff check --diff          # 檢查所有檔案的 lint，並列出差異，不修改檔案
uv run ruff check --add-noqa      # 檢查所有檔案的 lint，並在錯誤的地方加上 noqa 的註解來忽略錯誤
```

### Format

```
uv run ruff format                # 檢查所有檔案的 format
uv run ruff format --check        # 檢查所有檔案的 format，不修改檔案
uv run ruff format --diff         # 檢查所有檔案的 format，並列出差異，不修改檔案
```

### 其他指令

```
uv run ruff linter                # 列出所有支援的 linter
uv run ruff config                # 列出所有支援的 config
uv run ruff rule <RULE>           # 描述規則
```

## 規則

| 套件 | 縮寫 |
| ---- | ---- |
| All Rules | ALL |
| pycodestyle (flake8) | E, W |
| Pyflakes (flake8) | F |
| isort | I |
| mccabe | C90 |
| pydocstyle | D |
| pep8-naming | N |
| pyupgrade | UP |
| flake8-builtins | A |
| flake8-annotations | ANN |
| flake8-unused-arguments | ARG |
| flake8-bugbear | B |
| flake8-commas | COM |
| flake8-comprehensions | C4 |
| flake8-pytest-style | PT |
| flake8-quotes | Q |
| flake8-simplify | SIM |

## 設定檔

- 可以使用 `pyproject.toml`、`ruff.toml` 及 `.ruff.toml` 作為設定檔案。
- 在 Command-Line Interface 輸入的設定優先度比設定檔的高。
    ```
    # 若設定檔 line-length = 100，以下的 CLI 會使 line-length = 90
    ruff format --line-length=90
    ```

### 通用

```
# pyproject.toml

[tool.ruff]
include = ["*.py"]                              # 包含的檔案 (lint) ["*.py", "*.pyi", "*.ipynb", "**/pyproject.toml"]
extend-include = []                             # 包含的 extend 檔案 (lint)
exclude = []                                    # 排除的檔案 (lint & format)
extend-exclude = []                             # 排除的 extend 檔案 (lint & format)

show-fixes = true                               # 是否顯示修正的內容 (lint)
line-length = 88                                # 最大長度 (format) [1~320]
indent-width = 4                                # 縮排長度 (format)
respect-gitignore = true                        # 是否自動忽略 .ignore、.gitignore 及 .git/info/exclude 裡的檔案
extend = "../pyproject.toml"                    # 繼承另一個設定檔
```

### Lint

```
# pyproject.toml

[tool.ruff.lint]
select = ["F", "E", "W", "I"]                   # 新增規則
ignore = ["E501"]                               # 忽略規則
extend-select = []                              # 新增規則

fixable = []                                    # 修正指定規則
unfixable = []                                  # 不修正指定規則

[tool.ruff.lint.per-file-ignores]
"*.ipynb" = ["E501"]                            # 忽略指定檔案的指定規則

[tool.ruff.lint.pydocstyle]
convention = "google"                           # docstyle 的風格

[tool.ruff.lint.flake8-quotes]
inline-quotes = "double"                        # 單個引號風格 ["double", "single"]
multiline-quotes = "double"                     # 多個引號風格 ["double", "single"]
docstring-quotes = "double"                     # docstring 引號風格 ["double", "single"]
avoid-escape = true                             # 是否避免轉義內部引號
```

### Format

```
# pyproject.toml

[tool.ruff.format]
quote-style = "double"                          # String 的引號風格，可能和 linter E501 (line-too-long) 產生衝突 ["double", "single"]
indent-style = "space"                          # 縮排風格 ["space", "tab"]

skip-magic-trailing-comma = false               # 是否忽略 magic trailing commas
line-ending = "auto"                            # 換行符號 ["auto", "lf", "cr-lf", "native"]
docstring-code-format = false                   # 是否開啟 docstring format
docstring-code-line-length = 60                 # ["dynamic", int]
```

## VS Code Extension

- 安裝 [Ruff Extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)。
- 需要 format Python 檔案時，可在檔案中右鍵選擇 `Format Document` 或是按下 `F1` 開啟命令選單，搜尋 `Ruff: Format Document`。

### settings.json

- 以 `@id:ruff.enable` 設定是否啟用 Ruff。
- 若沒有設定 user settings 的設定檔，則會自動讀取專案的 `pyproject.toml`，優先度以 `@id:ruff.configurationPreference` 設定。
- 以 `@id:ruff.exclude` 設定不檢查哪些檔案名稱。

```
{
    "ruff.configuration": "~/path/to/pyproject.toml"
}
```

```
{
    "ruff.configuration": {
        "include": ["*.py"],
        "show-fixes": true,
        "line-length": 88,
        "indent-width": 4,
        "lint": {
            "select": [
                "F", "E", "W", "I", 
                "C90", "D", "N", 
                "A", "ANN", "ARG", "B", "COM", "C4", "PT", "Q", "SIM"
            ],
            "ignore": ["E501"]
        },
        "format": {
            "quote-style": "double",
            "indent-style": "space",
            "docstring-code-format": true, 
            "docstring-code-line-length": 60
        }
    }
}
```