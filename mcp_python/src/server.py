"""Create a MCP server, register tools, and run MCP server."""

from mcp.server.fastmcp import FastMCP

from prompts.register_prompts import register_prompts
from tools.register_tools import register_tools


def main() -> None:
    """Create a MCP server, register tools, and run MCP server."""
    mcp = FastMCP(name="demo", port=8000)
    register_prompts(mcp)
    register_tools(mcp)
    mcp.run(transport="stdio")
    # mcp.run(transport="sse")
    # mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()
