"""Register prompts."""

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

from prompts.template import template_prompts


def register_prompts(mcp: FastMCP) -> None:
    """Register prompts."""

    @mcp.prompt(title="Convert To Markdown")
    async def convert_to_markdown(filename: str) -> list[base.Message]:
        """Convert a file such as [PDF, PPTX, DOCX] to markdown format. Need to install MCP Server MarkItDown.

        Args:
            filename (str): The name of the file to be converted. Supported formats include PDF, PPTX, and DOCX.

        Returns:
            A list of user messages describing the conversion process and requirements.
        """
        prompt_msg = base.UserMessage(template_prompts.prompt_convert_to_markdown.format(filename=filename))
        return [prompt_msg]
