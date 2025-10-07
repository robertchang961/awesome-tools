# VS Code

撰寫時 Visual Studio Code 的版本為 1.104.2。

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
@id:chat.mcp.discovery.enabled
@id:chat.instructionsFilesLocations
@id:chat.promptFilesLocations
@id:chat.modeFilesLocations
@id:chat.tools.terminal.autoApprove
# GitHub Copilot
@id:github.copilot.chat.localeOverride
@id:github.copilot.nextEditSuggestions.enabled
@id:github.copilot.enable
# GitHub Copilot / experimental
@id:github.copilot.chat.agent.currentEditorContext.enabled
```

以下是已被棄用的設定：

```sh
# Retired
@id:chat.tools.autoApprove                                             # retired after vscode version 1.104.0
@id:github.copilot.chat.agent.terminal.allowList                       # retired after vscode version 1.104.0
@id:github.copilot.chat.agent.terminal.denyList                        # retired after vscode version 1.104.0
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
    "python.analysis.typeCheckingMode": "basic",                       // Python 的型態檢查模式
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
    "chat.mcp.discovery.enabled": {                                    // 是否自動尋找 MCP 設定檔案
        "claude-desktop": true,
        "windsurf": true,
        "cursor-global": true,
        "cursor-workspace": true
    },
    "chat.instructionsFilesLocations": {                               // 客製化 instructions 檔案放置路徑
        ".github/instructions": true
    },
    "chat.promptFilesLocations": {                                     // 客製化 prompts 檔案放置路徑
        ".github/prompts": true
    },
    "chat.modeFilesLocations": {                                       // 客製化 chatmodes 檔案放置路徑
        ".github/chatmodes": true
    },
    "chat.tools.terminal.autoApprove": {                               // 自動同意 Terminal 指令
        "cd": true,
        "echo": true,
        "ls": true,
        "pwd": true,
        "cat": true,
        "head": true,
        "tail": true,
        "findstr": true,
        "wc": true,
        "tr": true,
        "cut": true,
        "cmp": true,
        "which": true,
        "basename": true,
        "dirname": true,
        "realpath": true,
        "readlink": true,
        "stat": true,
        "file": true,
        "du": true,
        "df": true,
        "sleep": true,
        "git status": true,
        "git log": true,
        "git show": true,
        "git diff": true,
        "Get-ChildItem": true,
        "Get-Content": true,
        "Get-Date": true,
        "Get-Random": true,
        "Get-Location": true,
        "Write-Host": true,
        "Write-Output": true,
        "Split-Path": true,
        "Join-Path": true,
        "Start-Sleep": true,
        "Where-Object": true,
        "/^Select-[a-z0-9]/i": true,
        "/^Measure-[a-z0-9]/i": true,
        "/^Compare-[a-z0-9]/i": true,
        "/^Format-[a-z0-9]/i": true,
        "/^Sort-[a-z0-9]/i": true,
        "column": true,
        "/^column\\b.*-c\\s+[0-9]{4,}/": false,
        "date": true,
        "/^date\\b.*(-s|--set)\\b/": false,
        "find": true,
        "/^find\\b.*-(delete|exec|execdir|fprint|fprintf|fls|ok|okdir)\\b/": false,
        "grep": true,
        "/^grep\\b.*-(f|P)\\b/": false,
        "sort": true,
        "/^sort\\b.*-(o|S)\\b/": false,
        "tree": true,
        "/^tree\\b.*-o\\b/": false,
        "/\\(.+\\)/": {
            "approve": false,
            "matchCommandLine": true
        },
        "/\\{.+\\}/": {
            "approve": false,
            "matchCommandLine": true
        },
        "/`.+`/": {
            "approve": false,
            "matchCommandLine": true
        },
        "rm": false,
        "rmdir": false,
        "del": false,
        "Remove-Item": false,
        "ri": false,
        "rd": false,
        "erase": false,
        "dd": false,
        "kill": false,
        "ps": false,
        "top": false,
        "Stop-Process": false,
        "spps": false,
        "taskkill": false,
        "taskkill.exe": false,
        "curl": false,
        "wget": false,
        "Invoke-RestMethod": false,
        "Invoke-WebRequest": false,
        "irm": false,
        "iwr": false,
        "chmod": false,
        "chown": false,
        "Set-ItemProperty": false,
        "sp": false,
        "Set-Acl": false,
        "jq": false,
        "xargs": false,
        "eval": false,
        "Invoke-Expression": false,
        "iex": false,
        "git": true
    },
    // GitHub Copilot
    "github.copilot.chat.localeOverride": "zh-TW",                     // Chat View 的回應語言
    "github.copilot.nextEditSuggestions.enabled": true,                // 啟用 Next Edit Suggestions，版本 1.104.2 開始預設為啟用
    "github.copilot.enable": {                                         // 啟用指定的檔案類型
        "*": true,
        "plaintext": false,
        "markdown": true,
        "scminput": false
    },
    // GitHub Copilot / experimental
    "github.copilot.chat.agent.currentEditorContext.enabled": true,    // Chat View 是否要預設加入當前檔案到 Context 中
}
```
