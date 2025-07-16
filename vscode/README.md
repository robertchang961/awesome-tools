# VS Code

## 常用擴充

以下列出一些常用的擴充：

```sh
# git
code --install-extension eamodio.gitlens
# terminal
code --install-extension ms-vscode.powershell
# Python
code --install-extension ms-python.python
code --install-extension ms-python.vscode-python-envs
code --install-extension charliermarsh.ruff
code --install-extension ms-toolsai.jupyter
# AI
code --install-extension GitHub.copilot
code --install-extension ms-windows-ai-studio.windows-ai-studio
# others
code --install-extension ms-vscode.live-server
```

## 常用設定

以下列出一些常用的設定：

```sh
# editor
@id:editor.fontSize
@id:editor.tabSize
@id:editor.scrollOnMiddleClick
# files
@id:files.autoSave
@id:files.encoding
@id:files.insertFinalNewline
@id:files.trimFinalNewlines
@id:files.trimTrailingWhitespace
# workbench
@id:workbench.settings.showAISearchToggle
# terminal
@id:terminal.integrated.defaultProfile.windows
@id:terminal.integrated.suggest.enabled
# Python
@id:python.defaultInterpreterPath
# ruff
@id:ruff.configuration
# chat
@id:chat.agent.maxRequests
@id:chat.tools.autoApprove
@id:chat.mcp.discovery.enabled
@id:chat.instructionsFilesLocations
@id:chat.promptFilesLocations
@id:chat.modeFilesLocations
# GitHub Copilot
@id:github.copilot.chat.localeOverride
# GitHub Copilot / experimental
@id:github.copilot.chat.agent.currentEditorContext.enabled
@id:github.copilot.chat.agent.terminal.allowList
@id:github.copilot.chat.agent.terminal.denyList
```

```json5
{
    // editor
    "editor.fontSize": 14,                                             // 文字大小
    "editor.tabSize": 4,                                               // 一個 Tab 為多少個空白
    "editor.scrollOnMiddleClick": true,                                // 使用滑鼠中鍵來滑動檔案
    // files
    "files.autoSave": "onFocusChange",                                 // 自動儲存檔案
    "files.encoding": "utf8",                                          // Encoding 設定
    "files.insertFinalNewline": true,                                  // 儲存時自動新增檔案最後一個空白行
    "files.trimFinalNewlines": true,                                   // 儲存時自動刪除檔案最後多餘的空白行 (只會剩下最後一個空白行)
    "files.trimTrailingWhitespace": true,                              // 儲存時自動刪除每行最後所有的空白
    // workbench
    "workbench.settings.showAISearchToggle": true,                     // 在 Settings 啟用 AI Search 的 icon (快捷鍵 Ctrl + i)
    // terminal
    "terminal.integrated.defaultProfile.windows": "Command Prompt",    // 預設開啟哪種 Terminal
    "terminal.integrated.suggest.enabled": true,                       // 開啟 PowerShell 擴充的提示
    // Python
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
            "ignore": ["E501", "D413"]
        },
        "format": {
            "quote-style": "double",
            "indent-style": "space",
            "docstring-code-format": true,
            "docstring-code-line-length": 60
        }
    },
    // chat
    "chat.agent.maxRequests": 100,                                     // Chat View Agent Mode 的最大 Requests
    "chat.tools.autoApprove": true,                                    // Chat View Agent Mode 自動同意
    "chat.mcp.discovery.enabled": true,                                // 是否自動尋找 MCP 設定檔案
    "chat.instructionsFilesLocations": {                               // 客製化 instructions 檔案放置路徑
        ".github/instructions": true
    },
    "chat.promptFilesLocations": {                                     // 客製化 prompts 檔案放置路徑
        ".github/prompts": true
    },
    "chat.modeFilesLocations": {                                       // 客製化 chatmodes 檔案放置路徑
        ".github/chatmodes": true
    },
    // GitHub Copilot
    "github.copilot.chat.localeOverride": "zh-TW",                     // Chat View 的回應語言
    // GitHub Copilot / experimental
    "github.copilot.chat.agent.currentEditorContext.enabled": true,    // Chat View 是否要預設加入當前檔案到 Context 中
    "github.copilot.chat.agent.terminal.allowList": {},                // Chat View Agent Mode 同意的命令表單
    "github.copilot.chat.agent.terminal.denyList": {},                 // Chat View Agent Mode 不同意的命令表單
}
```
