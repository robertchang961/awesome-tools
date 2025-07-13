# VS Code

## 常用擴充

以下列出一些常用的擴充：

```sh
# Git
code --install-extension eamodio.gitlens
# Terminal
code --install-extension ms-vscode.powershell
# Python
code --install-extension ms-python.python
code --install-extension ms-python.vscode-python-envs
code --install-extension charliermarsh.ruff
code --install-extension ms-toolsai.jupyter
# AI
code --install-extension GitHub.copilot
code --install-extension ms-windows-ai-studio.windows-ai-studio
# Others
code --install-extension ms-vscode.live-server
```

## 常用設定

以下列出一些常用的設定：

```sh
# editor
@id:editor.fontSize
@id:editor.tabSize
# files
@id:files.autoSave
@id:files.encoding
@id:files.insertFinalNewline
@id:files.trimFinalNewlines
@id:files.trimTrailingWhitespace
# terminal
@id:terminal.integrated.defaultProfile.windows
# python
@id:python.defaultInterpreterPath
# ruff
@id:ruff.configuration
```

```json5
{
    // editor
    "editor.fontSize": 14,                                             // 文字大小
    "editor.tabSize": 4,                                               // 一個 Tab 為多少個空白
    // files
    "files.autoSave": "onFocusChange",                                 // 自動儲存檔案
    "files.encoding": "utf8",                                          // Encoding 設定
    "files.insertFinalNewline": true,                                  // 儲存時自動新增檔案最後一個空白行
    "files.trimFinalNewlines": true,                                   // 儲存時自動刪除檔案最後多餘的空白行 (只會剩下最後一個空白行)
    "files.trimTrailingWhitespace": true,                              // 儲存時自動刪除每行最後所有的空白
    // terminal
    "terminal.integrated.defaultProfile.windows": "Command Prompt",    // 預設開啟哪種 Terminal
    // python
    "python.defaultInterpreterPath": "\\path\\to\\python.exe",         // 預設的 Python Interpreter
    // ruff
    "ruff.configuration": {                                            // Python Ruff 的設定檔
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
