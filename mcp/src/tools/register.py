"""Register tools."""

from mcp.server.fastmcp import FastMCP


def register_tools(mcp: FastMCP) -> None:
    """Register tools."""

    @mcp.tool()
    def add(a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

    @mcp.tool()
    def get_greeting(name: str) -> str:
        """Get a personalized greeting."""
        return f"Hello, {name}!"
