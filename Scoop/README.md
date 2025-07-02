# Scoop

## Reference
- [GitHub Scoop](https://github.com/ScoopInstaller/Scoop)
- [Scoop Website](https://scoop.sh/)

## Installation

Run the following commands from a regular (non-admin) PowerShell terminal to install Scoop:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

**Note**: The first command makes your device allow running the installation and management scripts. This is necessary because Windows 10 client devices restrict execution of any PowerShell scripts by default.

It will install Scoop to its default location:

`C:\Users\<YOUR USERNAME>\scoop`

You can find the complete documentation about the installer, including advanced installation configurations, in [ScoopInstaller/Install](https://github.com/ScoopInstaller/Install). Please create new issues there if you have questions about the installation.

## Command Execution
```
scoop update             # Update Scoop and its bucket
scoop list               # List installed apps
scoop status             # Show status and check for new app versions
scoop search <APP>       # Search an app
scoop install <APP>      # Install an app
scoop update <APP>       # Update an app
scoop uninstall <APP>    # Uninstall an app
```

## Awesome Apps
```
main/7zip        # A multi-format file archiver with high compression ratios
main/allure      # A flexible lightweight multi-language test report tool
main/git         # Distributed version control system
main/jq          # Lightweight and flexible command-line JSON processor
main/nodejs      # An asynchronous event driven JavaScript runtime designed to build scalable network applications
main/openssh     # The premier connectivity tool for remote login with the SSH protocol
main/python      # A programming language that lets you work quickly and integrate systems more effectively
main/uv          # An extremely fast Python package installer and resolver, written in Rust

extras/putty     # A free implementation of SSH and Telnet, along with an xterm terminal emulator
extras/vscode    # Lightweight but powerful source code editor

java/openjdk     # Official General-Availability Release of OpenJDK
```

## Bucket
- Extra manifests for Scoop, the Windows command-line installer. For manifests that don't fit the Main criteria.
```
scoop bucket add extras
```
- A bucket for Scoop, for Oracle Java, OpenJDK, Eclipse Temurin, IBM Semeru, Zulu, ojdkbuild, Amazon Corretto, BellSoft Liberica, SapMachine and Microsoft JDK.
```
scoop bucket add java
```
