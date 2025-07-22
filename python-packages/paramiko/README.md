# Paramiko

## 參考資源
- [Paramiko Documentation](https://www.paramiko.org/)

## 什麼是 Paramiko?

Paramiko 是一個用 Python 編寫的套件，用來實作 SSH 通訊協定。

## 安裝方式

透過 uv 安裝：

```
uv add paramiko
```

## 常用指令

以下列出一些常用的 Paramiko 指令：

- 建立 sshclient 物件。
    ```python
    import paramiko

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ```
- 建立 SSH 連線。
    ```python
    host = ""
    port = ""
    username = ""
    password = ""
    client.connect(host, port=port, username=username, password=password, timeout=10)
    ```
- 在 SSH Server 上執行命令。
    ```python
    cmd = ""
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    ret = stdout.read().decode("utf-8", errors="ignore")
    ret_err = stderr.read().decode("utf-8", errors="ignore")
    exit_status = stdout.channel.recv_exit_status()
    ```
- 關閉 SSH 連線。
    ```python
    client.close()
    ```
