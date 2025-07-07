# Scoop

## Reference
- [GitHub Scoop](https://github.com/ScoopInstaller/Scoop)
- [Scoop Website](https://scoop.sh/)

## What is Scoop?

- Scoop 是 Windows 的命令列應用程式管理工具
- Scoop 讓你可以像在 Linux/macOS 使用 apt/brew 一樣，透過命令列安裝、更新、移除軟體
- 經過 Scoop 安裝後的應用程式會自動加入 PATH

## Installation

- 開啟 PowerShell (non-admin) 來安裝 Scoop
    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser    # 允許你的裝置執行安裝和管理腳本
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
    ```
- Scoop 安裝後的預設路徑會在 `C:\Users\<YOUR USERNAME>\scoop`
- 更多有關進階安裝配置 [ScoopInstaller/Install](https://github.com/ScoopInstaller/Install)

## Command Execution
- 以下列出一些常用的 Scoop 指令
    ```
    scoop update             # Update Scoop and its bucket
    scoop update -a          # Update Scoop, its bucket and all the apps
    scoop list               # List installed apps
    scoop status             # Show status and check for new app versions
    scoop search <APP>       # Search an app
    scoop install <APP>      # Install an app
    scoop update <APP>       # Update an app
    scoop uninstall <APP>    # Uninstall an app
    ```

## Awesome Apps
- 以下列出一些常用的應用程式
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

## Bucket
- Bucket 是應用程式清單的集合，Scoop 會從這些 bucket 中抓取應用程式的 manifest (一個 JSON 檔案，告訴 Scoop 該怎麼安裝應用程式)
- main 以外的 buckets
    ```
    scoop bucket add extras
    scoop bucket add java
    ```
