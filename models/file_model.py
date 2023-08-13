import os
from dataclasses import dataclass

from controllers.config import FILE_PATH


@dataclass
class FileModel:
    """
    Модель файла.

    Атрибуты:
        filename (str): Имя файла.
        path (str): Путь к директории файла.
        full_path (str): Полный путь к файлу.

    Методы:
        __post_init__() -> None:
            Выполняет дополнительную инициализацию объекта.

    """
    filename: str
    path: str = FILE_PATH

    def __post_init__(self) -> None:
        self.full_path = os.path.join(self.path, self.filename)
