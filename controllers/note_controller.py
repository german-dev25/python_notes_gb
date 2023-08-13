from datetime import datetime

from models.note_model import NoteModel
from view.note_view import NoteView


class NoteController:
    """
    Управляет заметками и их представлением.

    Атрибуты:
        view (NoteView): Объект для отображения информации о заметках.
        note_list (list[NoteModel]): Список объектов NoteModel,
        представляющих заметки.

    Методы:
        __init__(view: NoteView, note_list: list[dict[str, str]]):
            Инициализирует объект NoteController.

        create_note() -> None:
            Создаёт новую заметку, запрашивая у пользователя заголовок и
            содержание.

        read_note(full=False) -> None:
            Отображает информацию о заметках в полном или сокращенном виде.

        update_note() -> None:
            Обновляет информацию о выбранной заметке, запрашивая новый
            заголовок и содержание.

        delete_note() -> None:
            Удаляет выбранную заметку.

        filter_by_date() -> None:
            Отображает заметки, созданные или обновленные в указанную дату.

        search_by_word() -> None:
            Отображает заметки, содержащие указанное слово в заголовке или
            содержании.

        search_notes(note_list: list[NoteModel]) -> None | list[NoteModel]:
            Ищет заметки в списке по ID или заголовку, и отображает
            результаты поиска.

        select_note(note_list: list[NoteModel]) -> None | NoteModel:
            Позволяет пользователю выбрать одну из заметок из списка.

        return_dict_notes() -> list[dict]:
            Возвращает список заметок в виде словарей.
    """
    def __init__(self,
                 view: NoteView,
                 note_list: list[dict[str, str]]):
        self.view = view
        self.note_list = self.get_all_notes(note_list)

    @staticmethod
    def get_all_notes(data: list[dict[str, str]]) -> list[NoteModel]:
        return [NoteModel.from_dict(note_data) for note_data in data]

    def create_note(self) -> None:
        title, body = self.view.get_user_input()
        if not (title or body):
            self.view.input_error()
            return
        elif self.view.get_confirm():
            self.note_list.append(NoteModel(title=title, body=body))
            self.view.show_note(note=self.note_list[-1], action='create')

    def read_note(self, full=False) -> None:
        if full:
            self.view.show_notes(self.note_list)
        else:
            self.search_notes(self.note_list)

    def update_note(self) -> None:
        upd = self.search_notes(self.note_list)

        if upd:
            selected_note = (self.select_note(upd) if len(upd) > 1 else upd[0])
            if selected_note:
                title, body = self.view.get_user_input()
                if not (title or body):
                    self.view.input_error()
                    return
                elif self.view.get_confirm():
                    selected_note.title = title or selected_note.title
                    selected_note.body = body or selected_note.body
                    selected_note.updated = datetime.now()
                    self.view.show_note(selected_note, action='update')

    def delete_note(self) -> None:
        dlt = self.search_notes(self.note_list)

        if dlt:
            selected_note = (self.select_note(dlt) if len(dlt) > 1 else dlt[0])
            if selected_note and self.view.get_confirm():
                self.note_list.remove(selected_note)
                self.view.show_note(selected_note, action='delete')

    def filter_by_date(self) -> None:
        user_input = self.view.get_user_input()

        if user_input:
            try:
                target_date = datetime.strptime(user_input, '%Y-%m-%d').date()
                filtered_notes = [note for note in self.note_list if
                                  note.created.date() == target_date
                                  or note.updated.date() == target_date]
                self.view.show_notes(filtered_notes)
            except ValueError:
                self.view.input_error()
                return self.filter_by_date()

    def search_by_word(self) -> None:
        user_input = self.view.get_user_input()
        if user_input:
            result = [note for note in self.note_list
                      if user_input in note.title
                      or user_input in note.body]
            self.view.show_notes(result)

    def search_notes(self,
                     note_list: list[NoteModel]
                     ) -> None | list[NoteModel]:
        user_input = self.view.get_user_input()
        if user_input:
            result = [note for note in note_list
                      if note.note_id.lower() == user_input
                      or note.title.lower() == user_input]
            self.view.show_notes(result)
            return result

    def select_note(self,
                    note_list: list[NoteModel]
                    ) -> None | NoteModel:
        try:
            choice = int(self.view.get_user_input(note_list=note_list))
            if choice > 0:
                return note_list[choice - 1]
            else:
                self.view.input_error()
        except (IndexError, ValueError):
            self.view.input_error()
        return self.select_note(note_list=note_list)

    def return_dict_notes(self) -> list[dict]:
        return [note.to_dict() for note in self.note_list]
