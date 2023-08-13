class CommandView:
    """
    Представление для команд.

    Методы:
        all_commands(command_list) -> None:
            Выводит информацию о доступных командах.

        error_command(incorrect_command) -> None:
            Выводит сообщение об ошибке при неверной команде.
    """
    @staticmethod
    def all_commands(command_list) -> None:
        for index, command in enumerate(command_list, start=1):
            print(f'{index}. {command.name} - {command.description}')

    @staticmethod
    def error_command(incorrect_command) -> None:
        print(f'Command {incorrect_command} is not found.')
