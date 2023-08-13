from models.command_model import CommandModel
from view.command_view import CommandView


class CommandController:
    """
    Управляет командами и представлением.

    Атрибуты:
        command_list (list[CommandModel]): Список объектов CommandModel,
        представляющих команды.
        view (CommandView): Объект для отображения информации о командах.

    Методы:
        __init__(commands: dict[CommandModel], view: CommandView):
            Инициализирует объект CommandController.

        show_all_commands() -> None:
            Отображает информацию о всех доступных командах с помощью
            представления.

        get_command() -> str:
            Получает команду от пользователя, возвращает её имя в нижнем
            регистре и без лишних пробелов.

        create_command_list(commands) -> list[CommandModel]:
            Создаёт список объектов CommandModel из переданного словаря команд.
    """

    def __init__(self, commands: dict[CommandModel], view: CommandView):
        self.command_list = self.create_command_list(commands)
        self.view = view

    def show_all_commands(self) -> None:
        self.view.all_commands(self.command_list)

    @staticmethod
    def get_command() -> str:
        user_input = input('Введите имя команды или номер: ')
        return user_input.lower().strip()

    @staticmethod
    def create_command_list(commands) -> list[CommandModel]:
        return [CommandModel.from_dict(command_dict)
                for command_dict in commands]

