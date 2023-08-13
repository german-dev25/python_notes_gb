from models.file_model import FileModel


class FileView:
    """
    Представление для файлов.

    Методы:
        status_info(action: str, file: FileModel) -> None:
            Выводит информацию о статусе файла (создан, сохранен и т.д.).

        bad_status_info(action: str, file: FileModel) -> None:
            Выводит сообщение об ошибке в статусе файла.

        new_folder(folder) -> None:
            Выводит сообщение о создании новой папки.

        not_valid(error_name: str) -> None:
            Выводит сообщение об ошибке с неверным значением.

        no_file_work() -> None:
            Выводит сообщение о неработающем файле.

        print_files(file_list) -> None:
            Выводит список файлов.
    """

    @staticmethod
    def status_info(action: str, file: FileModel) -> None:
        print(f'{action.capitalize()} the file: {file.filename}')

    @staticmethod
    def bad_status_info(action: str, file: FileModel) -> None:
        print(f'File {file.filename} is not {action}.')

    @staticmethod
    def new_folder(folder) -> None:
        print(f'Make new folder: {folder}')

    @staticmethod
    def not_valid(error_name: str) -> None:
        print(f'Please enter a valid {error_name}.')

    @staticmethod
    def no_file_work() -> None:
        print(f'File is not created.'
              f'\nWe can work and make notes.'
              f'\nDon\'t forgive save file in the end')

    @staticmethod
    def print_files(file_list) -> None:
        print('Your notes files:')
        for file_name in file_list:
            print(file_name.split('.')[0])
