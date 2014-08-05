import sublime
import sublime_plugin
from itertools import cycle

_settings = None
def settings():
    return _settings or sublime.load_settings('ShowAtArbitrary.sublime-settings')

positions = None

class CaretWatcher(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        # caret has moved, reset positions to their default value
        global positions
        positions = cycle(settings().get('target_lines'))


class ShowAtArbitraryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global positions
        positions = positions or cycle(settings().get('target_lines'))
        target_line = next(positions)
        if target_line > 0:
            self.show_from_top(target_line)
        elif target_line < 0:
            self.show_from_bottom(abs(target_line))
        else:
            self.view.run_command('show_at_center')

    def row(self):
        caret = self.view.sel()[0].begin()
        return self.view.rowcol(caret)[0]

    def show_from_top(self, target_line):
        top, _ = self.screen_extents()
        offset = self.row() - top - target_line
        self.view.run_command('scroll_lines', {'amount': -offset})

    def show_from_bottom(self, target_line):
        _, bottom = self.screen_extents()
        offset = bottom - self.row() - target_line
        self.view.run_command('scroll_lines', {'amount': offset})

    def screen_extents(self):
        screenful = self.view.visible_region()
        top_row, _ = self.view.rowcol(screenful.begin())
        bottom_row, _ = self.view.rowcol(screenful.end())
        return (top_row, bottom_row)
