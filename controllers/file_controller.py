import json
import os

from controllers.config import FILE_PATH
from models.file_model import FileModel
from view.file_view import FileView


class FileController:
    """
    Управляет файлами и их представлением.

    Методы:
        __init__():
            Инициализирует объект FileController.

        get_file_name() -> str:
            Запрашивает у пользователя имя файла.

        file_manager() -> None:
            Отображает список файлов в указанной директории.

        create_file() -> None:
            Создаёт новый файл и записывает в него данные.

        read_data() -> list:
            Считывает данные из файла.

        update_data() -> None:
            Обновляет данные в файле.

        ask_save_changes() -> bool:
            Запрашивает у пользователя сохранить изменения.

        user_match_choice(action, function) -> bool:
            Запрашивает у пользователя подтверждение для выполнения
            определенного действия.
    """
    def __init__(self):
        self.view = FileView()
        self.file_manager()
        self.file_name = self.get_file_name()
        self.file = FileModel(self.file_name)
        self.data = []
        self.save_changes = True

    def get_file_name(self) -> str:
        while True:
            file_name = input('Enter the file name: ')
            if file_name.strip():
                break
            self.view.not_valid('file name.')
        return file_name

    def file_manager(self) -> None:
        file_list = os.listdir(FILE_PATH)
        self.view.print_files(file_list=file_list)

    def create_file(self) -> None:
        folder_path = os.path.dirname(self.file.full_path)

        if not os.path.exists(folder_path):
            self.view.new_folder(folder_path)
            os.makedirs(folder_path)

        with open(self.file.full_path, 'w') as f:
            self.view.status_info(action='create',
                                  file=self.file)
            self.update_data()

    def read_data(self) -> list:
        if not self.file.full_path.lower().endswith('.json'):
            self.file.full_path += '.json'
        try:
            with open(self.file.full_path, 'r') as f:
                data = json.load(f)
                self.view.status_info(action='read', file=self.file)
                return data
        except FileNotFoundError:
            self.view.bad_status_info(action='found', file=self.file)
            choice = self.user_match_choice(
                f'create a new file {self.file_name}',
                self.read_data)
            self.create_file() if choice else self.view.no_file_work()
            return []

    def update_data(self) -> None:
        with open(self.file.full_path, 'w') as f:
            self.view.status_info(action='save', file=self.file)
            json.dump(self.data, f, indent=4)
            self.save_changes = True

    def ask_save_changes(self) -> bool:
        self.view.bad_status_info(action='saved', file=self.file)
        choice = self.user_match_choice(f'save changes {self.file_name}',
                                        self.ask_save_changes)
        return choice

    def user_match_choice(self, action, function) -> bool:
        match input(f'Do you want to {action}? (y/n): ').lower().strip():
            case 'y' | 'yes':
                return True
            case 'n' | 'no':
                return False
            case _:
                self.view.not_valid('(yes/y) or (no/n)')
                return self.user_match_choice(action=action, function=function)
