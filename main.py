from controllers.command_controller import CommandController
from controllers.config import COMMAND_LIST
from controllers.file_controller import FileController
from controllers.note_controller import NoteController
from view.command_view import CommandView
from view.note_view import NoteView


def run():
    file_controller = FileController()

    note_view = NoteView()
    note_list = file_controller.read_data()
    note_controller = NoteController(view=note_view, note_list=note_list)

    cmd_view = CommandView()
    command_controller = CommandController(commands=COMMAND_LIST,
                                           view=cmd_view)

    while True:
        command_controller.show_all_commands()
        cmd = command_controller.get_command()
        match cmd:
            case 'create' | '1':
                note_controller.create_note()
                file_controller.save_changes = False
            case 'read one' | '2':
                note_controller.read_note()
            case 'read all' | '3':
                note_controller.read_note(full=True)
            case 'filter' | '4':
                note_controller.filter_by_date()
            case 'search' | '5':
                note_controller.search_by_word()
            case 'update' | '6':
                note_controller.update_note()
                file_controller.save_changes = False
            case 'delete' | '7':
                note_controller.delete_note()
                file_controller.save_changes = False
            case 'save' | '8':
                file_controller.data = note_controller.return_dict_notes()
                file_controller.update_data()
            case 'exit' | '9':
                if not file_controller.save_changes and file_controller.ask_save_changes():
                    file_controller.data = note_controller.return_dict_notes()
                    file_controller.update_data()
                exit()
            case _:
                command_controller.view.error_command(cmd)


if __name__ == "__main__":
    run()
