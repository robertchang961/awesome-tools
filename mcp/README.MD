# MCP

## 參考資源
- [GitHub MCP](https://github.com/modelcontextprotocol/python-sdk/)
- [GitHub FastMCP](https://github.com/jlowin/fastmcp)
- [FastMCP Documentation]()

## 什麼是 MCP?

MCP (Model Context Protocol) 是一種用於大型語言模型 (LLM) 與上下文服務之間溝通的協定，設計目的是讓 LLM 能夠透過標準化的方式取得上下文資訊。

MCP 讓你能夠建立伺服器，安全且標準化地向 LLM 應用程式提供資料與功能。

## 安裝方式

透過 uv 安裝：

```
uv add mcp[cli]
uv add fastmcp
```

透過 Scoop 安裝 node.js：

```
scoop install nodejs
```

透過 node.js 安裝 mcp-remote：

```
npm install mcp-remote
```

## 建立第一個 MCP Server

- 建立檔案 `mcp\src\server.py`，並輸入以下命令。
    - 建立一個 MCP Server 名為 `demo`，註冊 MCP Tools，在本機啟動 MCP Server。
    ```python
    """Create a MCP server, register tools, and run MCP server."""

    from tools.register import register_tools

    from mcp.server.fastmcp import FastMCP


    def main() -> None:
        """Create a MCP server, register tools, and run MCP server."""
        mcp = FastMCP(name="demo", port=8000)
        register_tools(mcp)
        mcp.run(transport="stdio")

    if __name__ == "__main__":
        main()
    ```
- 建立檔案 `mcp\src\tools\register.py`，並輸入以下命令。
    - 透過 `@mcp.tool()` 裝飾器定義 MCP Tools。
    ```python
    """Register tools."""

    from mcp.server.fastmcp import FastMCP


    def register_tools(mcp: FastMCP) -> None:
        """Register tools."""

        @mcp.tool()
        def add(a: int, b: int) -> int:
            """Add two numbers."""
            return a + b
    ```
- 開啟 VS Code，按下 `F1` 開啟命令選單, 搜尋 `MCP: Add Server`，選擇 `Command (stdio)`，可以新增設定於 User Settings 的 `settings.json` 或是 Workspace Settings 的 `.vscode/mcp.json`，輸入以下設定至設定檔中。
    - 注意在 Windows 上的路徑的反斜線 `\`，需要要轉換為雙反斜線 `\\`。
    ```json5
    {
        "mcp": {
            "servers": {
                "demo": {
                    "type": "stdio",
                    "command": "uv",
                    "args": [
                        "--directory",
                        "C:\\path\\mcp\\src",
                        "run",
                        "server.py"
                    ]
                }
            }
        }
    }
    ```
- 最後開啟 GitHub Copilot Chat View 的 Agent Mode，按下 New Tools Avaiable (Refresh Icon)，即可在 Configure Tools 看到新加入的工具。

## MCP 傳輸方式

- Stdio (Standard Input Output)
    - 透過標準輸入輸出，將 Request 送至 MCP Server。
- SSE (Server-Sent Events)
    - 僅能單向由 Server 向 Client 傳輸，但 SSE 額外提供 HTTP 的 POST 方法，允許 Client 向 Server 進行通訊，實現 Client 與 Server 雙向溝通的功能。
    ```python
    """Create a MCP server, register tools, and run MCP server."""

    from tools.register import register_tools

    from mcp.server.fastmcp import FastMCP


    def main() -> None:
        """Create a MCP server, register tools, and run MCP server."""
        mcp = FastMCP(name="demo", port=8000)
        register_tools(mcp)
        mcp.run(transport="sse")

    if __name__ == "__main__":
        main()
    ```
    ```json5
    {
        "mcp": {
            "servers": {
                "demo-sse": {
                    "type": "sse",
                    "args": [
                        "mcp-remote",
                        "http://localhost:8000/sse"
                    ]
                }
            }
        }
    }
    ```
- Streamable HTTP
    ```python
    """Create a MCP server, register tools, and run MCP server."""

    from tools.register import register_tools

    from mcp.server.fastmcp import FastMCP


    def main() -> None:
        """Create a MCP server, register tools, and run MCP server."""
        mcp = FastMCP(name="demo", port=8000)
        register_tools(mcp)
        mcp.run(transport="streamable-http")

    if __name__ == "__main__":
        main()
    ```
    ```json5
    {
        "mcp": {
            "servers": {
                "demo-http": {
                    "type": "http",
                    "args": [
                        "mcp-remote",
                        "http://localhost:8000/mcp"
                    ]
                }
            }
        }
    }
    ```
