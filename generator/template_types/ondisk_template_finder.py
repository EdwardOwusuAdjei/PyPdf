import logging
from pathlib import Path

from generator.template import Template


class OnDiskTemplate(Template):
    def get_template_file(self, path: str, cache=True) -> str:
        """
        Get file from on disk
        :param path: actually path with file
        :param cache: should use LRU cache
        :return: str
        """
        template_file = Path(path)
        if template_file.is_file():
            with open(path) as f:
                body = f.read()
                return body
        else:
            logging.error(f"path does not exist {path} on disk or not file")
