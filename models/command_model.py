from dataclasses import dataclass


@dataclass
class CommandModel:
    """
    Модель команды.

    Атрибуты:
        name (str): Имя команды.
        description (str): Описание команды.

    Методы:
        from_dict(command_dict) -> CommandModel:
            Создает объект CommandModel из словаря.

            Параметры:
                command_dict (dict): Словарь с информацией о команде.

            Возвращает:
                CommandModel: Созданный объект CommandModel.
    """
    name: str
    description: str

    @classmethod
    def from_dict(cls, command_dict) -> 'CommandModel':
        return cls(name=command_dict['name'],
                   description=command_dict['description'])
