"""Register tools."""

import json
import time

from mcp.server.fastmcp import Context, FastMCP

from libraries.filesystem import FileSystem


def register_tools(mcp: FastMCP) -> None:
    """Register tools."""

    @mcp.tool()
    def show_file_list() -> str:
        """Show file list."""
        files_list = FileSystem().show_file_list()
        return json.dumps(files_list)

    @mcp.tool()
    def show_filepath(filename: str) -> str:
        """Show file path."""
        filepath = FileSystem().show_filepath(filename)
        return json.dumps(filepath)

    @mcp.tool()
    def load_file_content(filename: str) -> str:
        """Load file content."""
        content = FileSystem().load_file_content(filename)
        return json.dumps(content)

    @mcp.tool()
    async def long_running_task(task_name: str, ctx: Context, steps: int = 5) -> str:
        """Execute a task with progress updates."""
        await ctx.info(f"Starting: {task_name}")

        for i in range(steps):
            progress = (i + 1) / steps
            await ctx.report_progress(
                progress=progress,
                total=1.0,
                message=f"Step {i + 1}/{steps}",
            )
            await ctx.info(f"Completed step {i + 1}")
            time.sleep(1)

        return f"Task '{task_name}' completed"
