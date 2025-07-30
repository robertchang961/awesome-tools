"""Create a MCP server, register tools, and run MCP server."""

from tools.register import register_tools

from mcp.server.fastmcp import FastMCP


def main() -> None:
    """Create a MCP server, register tools, and run MCP server."""
    mcp = FastMCP(name="demo", port=8000)
    register_tools(mcp)
    # mcp.run(transport="stdio")
    # mcp.run(transport="sse")
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()
