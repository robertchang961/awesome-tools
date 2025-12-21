# Windows Command

## Windows SDK - Inspect

- 下載並安裝 [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)。
- [Inspect Tool](https://learn.microsoft.com/en-us/windows/win32/winauto/inspect-objects) 是一款基於 Windows 的工具，可選擇任何 UI 元素並查看 Microsoft UI 自動化屬性和控制模式以及 Microsoft Active Accessibility (MSAA) 屬性。
- 使用 CMD 開啟 Inspect Tool，Inspect Tool 會在此路徑下 `C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x86\Inspect.exe` (版本號可能會不同)。
- 接著可以使用 RPA Framework 的 [RPA.Windows](https://rpaframework.org/libraries/windows/python.html) 來操作 Windows GUI。

## Abbreviations

WMIC (Windows Management Instrumentation Command-line)

## Pause System Updates

- 暫停 Windows 系統更新。
    ```powershell
    irm bit.ly/SetWinUpd | iex; Set-WUPause 3650
    ```

## File Operations

- 顯示當前工作目錄。
    ```powershell
    Get-Location
    ```
    ```powershell
    pwd
    ```
- 列出檔案與目錄。
    ```powershell
    Get-ChildItem
    ```
    ```powershell
    ls
    ```
    ```powershell
    dir
    ```
- 切換目錄。
    ```powershell
    Set-Location <path>
    ```
    ```powershell
    cd <path>
    ```
- 建立目錄。
    ```powershell
    New-Item -ItemType Directory -Path <path>
    ```
    ```powershell
    mkdir <path>
    ```
- 建立檔案。
    ```powershell
    New-Item -ItemType File -Path <path>
    ```
- 刪除檔案或目錄。
    ```powershell
    Remove-Item <path>
    ```
    ```powershell
    rm -r <path>
    ```
- 複製檔案。
    ```powershell
    Copy-Item -Path <source> -Destination <destination>
    ```
    ```powershell
    cp <source> <destination>
    ```
- 進階檔案複製 (Robocopy)。
    - 鏡像複製 (同步來源與目的資料夾)。
        ```powershell
        robocopy <source> <destination> /MIR
        ```
    - 複製包含子目錄 (含空目錄)。
        ```powershell
        robocopy <source> <destination> /E
        ```
- 移動檔案。
    ```powershell
    Move-Item -Path <source> -Destination <destination>
    ```
    ```powershell
    mv <source> <destination>
    ```
- 讀取檔案內容。
    ```powershell
    Get-Content <path>
    ```
    ```powershell
    cat <path>
    ```

## Basic

- 查詢電腦資訊。
    ```powershell
    Get-ComputerInfo
    ```
- 查詢 Device Name。
    ```powershell
    hostname
    ```
    ```powershell
    wmic computersystem get name
    ```
    ```powershell
    Get-ComputerInfo | Select-Object -ExpandProperty CsDNSHostName
    ```
- 查詢 User Name。
    ```powershell
    Get-ComputerInfo | Select-Object -ExpandProperty CsName
    ```

## Credentials

- 列出儲存的認證。
    ```powershell
    cmdkey /list
    ```
- 新增認證。
    ```powershell
    cmdkey /add:<target_name> /user:<username> /pass:<password>
    ```
- 刪除認證。
    ```powershell
    cmdkey /delete:<target_name>
    ```

## Network Drive

- 連線網路磁碟機。
    ```powershell
    net use <drive_letter>: \\<server_name>\<share_name> /user:<username> <password> /persistent:yes
    ```
- 斷開網路磁碟機。
    ```powershell
    net use <drive_letter>: /delete
    ```
- 斷開所有網路磁碟機。
    ```powershell
    net use * /delete /y
    ```

## DNS

- 查詢 DNS Name。
    ```powershell
    wmic computersystem get domain
    ```
    ```powershell
    Get-ComputerInfo | Select-Object -ExpandProperty CsDomain
    ```
- 顯示本機所有網路介面的狀態資訊，列出管理狀態 (已啟用/已停用)、連線狀態 (已連線/已斷線)、類型 (如乙太網路、無線、環回等)、介面名稱。
    ```powershell
    netsh interface show interface
    ```
    ```powershell
    netsh interface show interface | findstr /c:"Connected" /c:"已連線"
    ```
- 設定 DNS。
    ```powershell
    netsh interface ip set dns name=<interface_name> static <dns_ip>
    ```
- 查詢 DNS 資訊。
    ```powershell
    Get-DnsClientServerAddress
    ```
    ```powershell
    nslookup <domain_name | dns_ip>
    ```

## Domain

- 加入 Domain。
    ```powershell
    $password = '<domain_password>' | ConvertTo-SecureString -AsPlainText -Force; $cred = New-Object System.Management.Automation.PSCredential ('<domain_name>\<domain_username>', $password); Add-Computer -DomainName '<domain_name>' -DomainCredential $cred -Force -Restart
    ```
- 退出 Domain。
    ```powershell
    $password = '<domain_password>' | ConvertTo-SecureString -AsPlainText -Force; $cred = New-Object System.Management.Automation.PSCredential ('<domain_name>\<domain_username>', $password); Remove-Computer -UnjoinDomainCredential $cred -Force -Restart
    ```
- 新增 AD 使用者。
    ```powershell
    net user <username> <password> /add /domain
    ```
    ```powershell
    dsadd user "CN=<username>,CN=Users,DC=<dns_name>"
    ```
    (<dns_name> 不需要加上 `.com`)
- 刪除 AD 使用者。
    ```powershell
    net user <username> /delete /domain
    ```
    ```powershell
    dsrm "CN=<username>,CN=Users,DC=<dns_name>"
    ```
    (<dns_name> 不需要加上 `.com`)
- 新增 AD 群組。
    ```powershell
    net group <groupname> /add /domain
    ```
    ```powershell
    dsadd group "CN=<groupname>,CN=Users,DC=<dns_name>"
    ```
    (<dns_name> 不需要加上 `.com`)
- 刪除 AD 群組。
    ```powershell
    net group <groupname> /delete /domain
    ```
    ```powershell
    dsrm "CN=<groupname>,CN=Users,DC=<dns_name>"
    ```
    (<dns_name> 不需要加上 `.com`)
- 新增 AD 電腦。
    ```powershell
    dsadd computer "CN=<computer_name>,CN=Computers,DC=<dns_name>"
    ```
    (<dns_name> 不需要加上 `.com`)
- 刪除 AD 電腦。
    ```powershell
    dsrm "CN=<computer_name>,CN=Computers,DC=<dns_name>"
    ```
    (<dns_name> 不需要加上 `.com`)
- 查詢使用者。
    ```powershell
    dsquery user -name <username>
    ```
- 查詢群組。
    ```powershell
    dsquery group -name <groupname>
    ```
- 查詢電腦。
    ```powershell
    dsquery computer -name <computer_name>
    ```

## Share Folder

- 設定 Share Folder 權限。
    ```powershell
    net share <share_folder_name>=<folder_path> /GRANT:<username>,<permission>
    ```
    (<permission> 可為 FULL、CHANGE 或 READ)
- 刪除 Share Folder。
    ```powershell
    net share <share_folder_name> /delete /y
    ```
