import inspect
from datetime import datetime

from models.note_model import NoteModel


class NoteView:
    """
    Представление для заметок.

    Методы:
        show_note(note: NoteModel, action=None) -> None:
            Выводит информацию о заметке.

        show_notes(note_list: list[NoteModel]) -> None:
            Выводит информацию о списке заметок.

        get_user_input(note_list: list = None) -> None | str:
            Запрашивает ввод пользователя.

        get_confirm() -> bool:
            Запрашивает подтверждение пользователя.

        yes_no(choice) -> bool:
            Обрабатывает ответ пользователя "yes" или "no".

        input_error() -> None:
            Выводит сообщение об ошибке ввода.

        get_or_stop(user_input) -> None | str:
            Проверяет ввод пользователя на наличие данных.

        show_date(date: datetime) -> str:
            Возвращает строку с датой в удобном формате.
    """

    def show_note(self, note: NoteModel, action=None) -> None:
        if note:
            action_text = f'Note is {action}' if action else ''
            print(
                f'{action_text}'
                f'\nID: {note.note_id}'
                f'\nTitle: {note.title}'
                f'\nBody: {note.body}'
                f'\nCreated: {self.show_date(note.created)}'
                f'\nUpdated: {self.show_date(note.updated)}'
                f'\n============================='
            )
        else:
            print('Not found. Try again')

    def show_notes(self, note_list: list[NoteModel]) -> None:
        if note_list:
            print('Showing all notes:')
            for index, note in enumerate(note_list, start=1):
                print(f'============={index:03}=============')
                self.show_note(note)
        else:
            print('No notes found')

    def get_user_input(self, note_list: list = None):
        match inspect.currentframe().f_back.f_code.co_name:
            case 'filter_by_date':
                return self.get_or_stop(
                    input('Enter the date (YYYY-MM-DD) '
                          '(or empty to stop): '))
            case 'search_by_word':
                return self.get_or_stop(
                    input('Enter the word to search '
                          '(or empty to stop): '))
            case 'search_notes':
                return self.get_or_stop(
                    input('Input ID or Title '
                          '(or empty to stop): '))
            case 'select_note':
                return self.get_or_stop(
                    input(f'Make choice 1-{len(note_list)} '
                          f'(or empty to stop): '))
            case 'create_note':
                return input('Title: ').strip(), \
                       input('Body: ').strip()
            case 'update_note':
                return input('New title (or empty): ').strip(), \
                       input('New body (or empty): ').strip()

    def get_confirm(self) -> bool:
        match inspect.currentframe().f_back.f_code.co_name:
            case 'create_note':
                return self.yes_no(input('Save changes? (y/n): '))
            case 'update_note':
                return self.yes_no(input('Save updated note? (y/n): '))
            case 'delete_note':
                return self.yes_no(input('Are you sure? (y/n): '))
            case 'yes_no':
                return self.yes_no(input('Only Yes/No (y/n): '))

    def yes_no(self, choice) -> bool:
        match choice.strip().lower():
            case 'yes' | 'y':
                return True
            case 'no' | 'n':
                print('Operation canceled.')
                return False
            case _:
                self.input_error()
                return self.get_confirm()

    @staticmethod
    def input_error() -> None:
        match inspect.currentframe().f_back.f_code.co_name:
            case 'get_confirm' | 'get_user_input' | 'select_note' | 'yes_no':
                print(f'Invalid input.')
            case 'filter_by_date':
                print(f'Invalid date format.')
            case 'create_note' | 'update_note':
                print(f'Empty data.')

    @staticmethod
    def get_or_stop(user_input) -> None | str:
        if not user_input.strip():
            print('Operation canceled.')
            return None
        else:
            return user_input.lower()

    @staticmethod
    def show_date(date: datetime) -> str:
        return date.strftime('%d-%m-%Y || %H:%M')
