# Windows Command

## Abbreviations

WMIC (Windows Management Instrumentation Command-line)

## Basic

* 查詢電腦資訊
    * `Get-ComputerInfo`
* 查詢 Device Name
    * `hostname`
    * `wmic computersystem get name`
    * `Get-ComputerInfo | Select-Object -ExpandProperty CsDNSHostName`
* 查詢 User Name
    * `Get-ComputerInfo | Select-Object -ExpandProperty CsName`

## DNS

* 查詢 DNS Name
    * `wmic computersystem get domain`
    * `Get-ComputerInfo | Select-Object -ExpandProperty CsDomain`
* 顯示本機所有網路介面的狀態資訊，列出管理狀態 (已啟用/已停用)、連線狀態 (已連線/已斷線)、類型 (如乙太網路、無線、環回等)、介面名稱
    * `netsh interface show interface`
    * `netsh interface show interface | findstr /c:"Connected" /c:"已連線"`
* 設定 DNS
    * `netsh interface ip set dns name=<interface_name> static <dns_ip>`
* 查詢 DNS 資訊
    * `Get-DnsClientServerAddress`
    * `nslookup <domain_name | dns_ip>`

## Domain

* 加入 Domain
    * `powershell "$password = '<domain_password>' | ConvertTo-SecureString -AsPlainText -Force; $cred = New-Object System.Management.Automation.PSCredential ('<domain_name>\<domain_username>', $password); Add-Computer -DomainName '<domain_name>' -DomainCredential $cred -Force -Restart"`
* 退出 Domain
    * `powershell "$password = '<domain_password>' | ConvertTo-SecureString -AsPlainText -Force; $cred = New-Object System.Management.Automation.PSCredential ('<domain_name>\<domain_username>', $password); Remove-Computer -UnjoinDomainCredential $cred -Force -Restart"`
* 新增 AD 使用者
    * `net user <username> <password> /add /domain`
    * `dsadd user "CN=<username>,CN=Users,DC=<dns_name>"` (<dns_name> 不需要加上 `.com`)
* 刪除 AD 使用者
    * `net user <username> /delete /domain`
    * `dsrm "CN=<username>,CN=Users,DC=<dns_name>"` (<dns_name> 不需要加上 `.com`)
* 新增 AD 群組
    * `net group <groupname> /add /domain`
    * `dsadd group "CN=<groupname>,CN=Users,DC=<dns_name>"` (<dns_name> 不需要加上 `.com`)
* 刪除 AD 群組
    * `net group <groupname> /delete /domain`
    * `dsrm "CN=<groupname>,CN=Users,DC=<dns_name>"` (<dns_name> 不需要加上 `.com`)
* 新增 AD 電腦
    * `dsadd computer "CN=<computer_name>,CN=Computers,DC=<dns_name>"` (<dns_name> 不需要加上 `.com`)
* 刪除 AD 電腦
    * `dsrm "CN=<computer_name>,CN=Computers,DC=<dns_name>"` (<dns_name> 不需要加上 `.com`)
* 查詢使用者
    * `dsquery user -name <username>`
* 查詢群組
    * `dsquery group -name <groupname>`
* 查詢電腦
    * `dsquery computer -name <computer_name>`

## Share Folder

* 設定 Share Folder 權限
    * `net share <share_folder_name>=<folder_path> /GRANT:<username>,<permission>` (<permission> 可為 FULL、CHANGE 或 READ)
* 刪除 Share Folder
    * `net share <share_folder_name> /delete /y`
