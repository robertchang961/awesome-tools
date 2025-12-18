# VS Code

撰寫時 Visual Studio Code 的版本為 1.107.1 (November 2025)。

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
# GitHub
code --install-extension GitHub.copilot
code --install-extension GitHub.vscode-pull-request-github
```

## 常用設定

以下列出一些常用的設定：

```sh
# editor
@id:editor.fontSize
@id:editor.tabSize
@id:editor.scrollOnMiddleClick
@id:editor.aiStats.enabled
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
@id:chat.checkpoints.enabled
@id:chat.checkpoints.showFileChanges
@id:chat.editRequests
@id:chat.mcp.discovery.enabled
@id:chat.mcp.gallery.enabled
@id:chat.instructionsFilesLocations
@id:chat.promptFilesLocations
@id:chat.tools.terminal.enableAutoApprove
@id:chat.tools.terminal.autoApprove
@id:chat.useAgentsMdFile
@id:chat.useNestedAgentsMdFiles
@id:chat.agentSessionsViewLocation
# Source Control
@id:scm.repositories.selectionMode
@id:scm.repositories.explorer
# GitHub Copilot
@id:github.copilot.chat.agent.currentEditorContext.enabled
@id:github.copilot.chat.localeOverride
@id:github.copilot.nextEditSuggestions.enabled
@id:github.copilot.enable
```

以下是已被棄用的設定：

```sh
# Retired
@id:chat.modeFilesLocations                                            # 版本 1.106 October 2025 棄用，資料夾從 .github/chatmodes 修改為 .github/agents
@id:chat.tools.autoApprove                                             # 版本 1.104 August 2025 棄用，請改用 @id:chat.tools.global.autoApprove
@id:github.copilot.chat.agent.terminal.allowList                       # 版本 1.104 August 2025 棄用，請改用 @id:chat.tools.terminal.autoApprove
@id:github.copilot.chat.agent.terminal.denyList                        # 版本 1.104 August 2025 棄用，請改用 @id:chat.tools.terminal.autoApprove
```

```json5
{
    // editor
    "editor.fontSize": 14,                                             // 文字大小
    "editor.tabSize": 4,                                               // 一個 Tab 為多少個空白
    "editor.scrollOnMiddleClick": true,                                // 是否啟用使用滑鼠中鍵來滑動檔案
    "editor.aiStats.enabled": true,                                    // 是否啟用 AI 使用統計 (版本 1.103 July 2025 加入)
    "[python]": {                                                      // Python 檔案的設定
        "editor.tabSize": 4,
    },
    "[html]": {                                                        // HTML 檔案的設定
        "editor.tabSize": 2,
    },
    "[css]": {                                                         // CSS 檔案的設定
        "editor.tabSize": 2,
    },
    "[javascript]": {                                                  // JavaScript 檔案的設定
        "editor.tabSize": 2,
    },
    "[vue]": {                                                         // Vue 檔案的設定
        "editor.tabSize": 2,
    },
    "[json]": {                                                        // JSON 檔案的設定
        "editor.tabSize": 2,
    },
    // files
    "files.autoSave": "onFocusChange",                                 // 自動儲存檔案
    "files.encoding": "utf8",                                          // Encoding 設定
    "files.insertFinalNewline": true,                                  // 是否啟用儲存時自動新增檔案最後一個空白行
    "files.trimFinalNewlines": true,                                   // 是否啟用儲存時自動刪除檔案最後多餘的空白行 (只會剩下最後一個空白行)
    "files.trimTrailingWhitespace": true,                              // 是否啟用儲存時自動刪除每行最後所有的空白
    // workbench
    "workbench.settings.showAISearchToggle": true,                     // 是否啟用在 Settings 啟用 AI Search 的 icon (快捷鍵 Ctrl + i)
    // terminal
    "terminal.integrated.defaultProfile.windows": "Command Prompt",    // 預設開啟哪種 Terminal
    "terminal.integrated.suggest.enabled": true,                       // 是否啟用 PowerShell 擴充的提示
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
    "chat.checkpoints.enabled": true,                                  // 是否啟用 Checkpoints 功能 (版本 1.103 July 2025 加入)
    "chat.checkpoints.showFileChanges": true,                          // 是否啟用在 Checkpoints 中顯示檔案變更 (版本 1.103 July 2025 加入)
    "chat.editRequests":"input",                                       // 編輯請求的模式 (版本 1.103 July 2025 加入)
    "chat.mcp.discovery.enabled": {                                    // 是否自動尋找 MCP 設定檔案
        "claude-desktop": true,
        "windsurf": true,
        "cursor-global": true,
        "cursor-workspace": true
    },
    "chat.mcp.gallery.enabled": true,                                  // 是否啟用 MCP Gallery，在 Extensions 輸入 @mcp 可搜尋商店的 MCP (版本 1.105 September 2025 加入)
    "chat.instructionsFilesLocations": {                               // 客製化 instructions 檔案放置路徑
        ".github/instructions": true
    },
    "chat.promptFilesLocations": {                                     // 客製化 prompts 檔案放置路徑
        ".github/prompts": true
    },
    "chat.tools.terminal.enableAutoApprove": true,                     // 是否啟用 Terminal 指令自動同意功能 (版本 1.104 August 2025 加入)
    "chat.tools.terminal.autoApprove": {                               // 自動同意 Terminal 指令 (版本 1.104 August 2025 加入)
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
        // custom tools
        "git": true
    },
    "chat.useAgentsMdFile": true,                                      // 是否啟用讀取 AGENTS.md 檔案 (版本 1.104 August 2025 加入)
    "chat.useNestedAgentsMdFiles": true,                               // 是否啟用讀取資料夾中的 AGENTS.md 檔案 (版本 1.105 September 2025 加入)
    "chat.agentSessionsViewLocation": "view",                          // Agent Sessions 視圖顯示位置 (版本 1.106 October 2025 加入)
    // Source Control
    "scm.repositories.selectionMode": "single",                        // Source Control 選擇模式，預設為 multiple (版本 1.106 October 2025 加入)
    "scm.repositories.explorer": true,                                 // 是否在 Source Control Explorer 顯示 Repositories View (版本 1.106 October 2025 加入)
    // GitHub Copilot
    "github.copilot.chat.agent.currentEditorContext.enabled": true,    // 是否啟用 Chat View 預設加入當前檔案到 Context 中
    "github.copilot.chat.localeOverride": "zh-TW",                     // Chat View 的回應語言
    "github.copilot.nextEditSuggestions.enabled": true,                // 是否啟用 Next Edit Suggestions (版本 1.104.2 August 2025 開始預設為啟用)
    "github.copilot.enable": {                                         // 是否啟用指定的檔案類型
        "*": true,
        "plaintext": true,
        "markdown": true,
        "scminput": false
    },
}
```

## GitHub Copilot

### 允許 MCP Tools

- 按下 `F1` 開啟命令選單, 搜尋 `Chat: Manage Tool Approval`，可以管理 MCP Tools 的允許清單。

### Custom Agents

- 以下是一個 `.agent.md` 的範例，會忽略未安裝的 tools：
```markdown
---
target: vscode
name: agent_name
description: description when mouse hover over the agent_name
argument-hint: hint to help user know what to input
model: model_name
tools: ['tool1', 'tool2', ... ]
handoffs:
  - label: Start Implementation
    agent: agent
    prompt: Start implementation
  - label: Open in Editor
    agent: agent
    prompt: '#createFile the plan as is into an untitled file (`untitled:plan-${camelCaseName}.prompt.md` without frontmatter) for further refinement.'
    send: true
---

Prompts ...
```
