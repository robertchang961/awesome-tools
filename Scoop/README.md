# Scoop

## 參考來源
- [GitHub Scoop](https://github.com/ScoopInstaller/Scoop)
- [Scoop Website](https://scoop.sh/)

## 什麼是 Scoop?

- Scoop 是一款 Windows 平台的命令列應用程式管理工具。
- 你可以像在 Linux/macOS 使用 apt 或 brew 一樣，透過命令列安裝、更新、移除軟體。
- 透過 Scoop 安裝的應用程式會自動加入 PATH，方便直接在命令列執行。

## 安裝方式

- 開啟 PowerShell（非管理員模式）執行以下指令：
    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser    # 允許執行安裝與管理腳本
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
    ```
- Scoop 安裝後的預設路徑為：`C:\Users\<你的使用者名稱>\scoop`。
- 更多進階安裝設定請參考 [ScoopInstaller/Install](https://github.com/ScoopInstaller/Install)。

## 常用 Scoop 指令

以下列出一些常用的 Scoop 指令：

```
scoop update             # 更新 Scoop 及其 bucket
scoop update -a          # 更新 Scoop、所有 bucket 及所有已安裝的應用程式
scoop list               # 列出已安裝的應用程式
scoop status             # 顯示狀態並檢查有無新版本
scoop search <APP>       # 搜尋應用程式
scoop install <APP>      # 安裝應用程式
scoop update <APP>       # 更新指定應用程式
scoop uninstall <APP>    # 移除指定應用程式
```

## Awesome Apps

以下列出一些常用的應用程式：

```
main/7zip                 # A multi-format file archiver with high compression ratios
main/allure               # A flexible lightweight multi-language test report tool
main/git                  # Distributed version control system
main/jq                   # Lightweight and flexible command-line JSON processor
main/nodejs               # An asynchronous event driven JavaScript runtime designed to build scalable network applications
main/openssh              # The premier connectivity tool for remote login with the SSH protocol
main/python               # A programming language that lets you work quickly and integrate systems more effectively
main/uv                   # An extremely fast Python package installer and resolver, written in Rust

extras/putty              # A free implementation of SSH and Telnet, along with an xterm terminal emulator
extras/vscode             # Lightweight but powerful source code editor
extras/notepadplusplus    # A free source code editor and Notepad replacement that supports several languages

java/openjdk              # Official General-Availability Release of OpenJDK
```

## Bucket 介紹

- Bucket 是應用程式清單的集合，Scoop 會從這些 bucket 取得應用程式的 manifest (JSON 格式，描述如何安裝應用程式)。
- 除了預設的 main bucket，也可加入其他 bucket：
    ```
    scoop bucket add extras
    scoop bucket add java
    ```
