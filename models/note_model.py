from dataclasses import field, dataclass
from datetime import datetime


@dataclass
class NoteModel:
    """
    Модель заметки.

    Атрибуты:
        title (str): Заголовок заметки.
        body (str): Содержание заметки.
        created (datetime): Дата и время создания заметки.
        updated (datetime): Дата и время последнего обновления заметки.
        __note_id (str): Уникальный идентификатор заметки.
        __next_id (int): Счетчик для создания следующего идентификатора.

    Методы:
        __post_init__() -> None:
            Выполняет дополнительную инициализацию объекта.

        from_dict(data_dict) -> NoteModel:
            Создает объект NoteModel из словаря.

            Параметры:
                data_dict (dict): Словарь с информацией о заметке.

            Возвращает:
                NoteModel: Созданный объект NoteModel.

        to_dict() -> dict:
            Преобразует объект NoteModel в словарь.

        @property
        next_id() -> int:
            Возвращает следующий доступный идентификатор.

        @property
        note_id() -> str:
            Возвращает уникальный идентификатор заметки.
    """
    title: str = None
    body: str = None

    created: datetime = field(default_factory=datetime.now)
    updated: datetime = field(default_factory=datetime.now)

    __note_id: str = field(init=False)
    __next_id: int = 1

    def __post_init__(self) -> None:
        self.__note_id = str(NoteModel.__next_id).zfill(5)
        NoteModel.__next_id += 1

    @classmethod
    def from_dict(cls, data_dict: dict[str, str]) -> 'NoteModel':
        note = cls(
            title=data_dict['title'],
            body=data_dict['body'],
            created=datetime.fromisoformat(data_dict['created']),
            updated=datetime.fromisoformat(data_dict['updated'])
        )
        note.__note_id = data_dict['__note_id']
        return note

    def to_dict(self) -> dict:
        return {
            'title': self.title,
            'body': self.body,
            'created': self.created.isoformat(),
            'updated': self.updated.isoformat(),
            '__note_id': self.note_id
        }

    @property
    def next_id(self) -> int:
        return self.__next_id

    @property
    def note_id(self) -> str:
        return self.__note_id
