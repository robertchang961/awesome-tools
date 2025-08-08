"""File system."""

import logging
import pathlib


class FileSystem:
    """File system."""

    def __init__(self) -> None:
        """Initialize FileSystem."""
        self.basedir = pathlib.Path(__file__).resolve().parent.parent.parent

    def show_file_list(self) -> list[str] | bool:
        """Show file list."""
        try:
            files_list = [str(f) for f in self.basedir.glob("*") if f.is_file()]
            return files_list
        except Exception as e:
            logging.error(f"Error with list files: {e}")
            return False

    def show_filepath(self, filename: str) -> str | bool:
        """Show filepath."""
        try:
            logging.info(filename)
            filepath = pathlib.Path.joinpath(self.basedir, pathlib.Path(filename))
            return str(filepath)
        except Exception as e:
            logging.error(f"Error with show filepath: {e}")
            return False

    def load_file_content(self, filename: str) -> str | bool:
        """Load file content."""
        try:
            logging.info(filename)
            filepath = pathlib.Path(filename)

            if not filepath.is_file():
                logging.error(f"Error with load file content: file not found {filepath}")
                return False

            with open(filepath, mode="r", encoding="utf-8") as fp:
                contents = ""
                while True:
                    content = fp.read(4096)
                    if content:
                        contents += content
                    else:
                        break

            return contents
        except Exception as e:
            logging.error(f"Error with load file content: {e}")
            return False
