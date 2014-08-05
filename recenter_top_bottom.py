import sublime
import sublime_plugin
from itertools import cycle

_settings = None
def settings():
    return _settings or sublime.load_settings('RecenterTopBottom.sublime-settings')

positions = None

class CaretWatcher(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        # caret has moved, reset positions to their default value
        global positions
        positions = cycle(settings().get('recenter_positions'))


class RecenterTopBottomCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global positions
        positions = positions or cycle(settings().get('recenter_positions'))
        posn = next(positions)
        if posn > 0:
            self.show_at_top(posn)
        elif posn < 0:
            self.show_at_bottom(abs(posn))
        else:
            self.view.run_command('show_at_center')

    def row(self):
        caret = self.view.sel()[0].begin()
        return self.view.rowcol(caret)[0]

    def show_at_top(self, target_line):
        top, _ = self.screen_extents()
        offset = self.row() - top - target_line
        self.view.run_command('scroll_lines', {'amount': -offset})

    def show_at_bottom(self, target_line):
        _, bottom = self.screen_extents()
        offset = bottom - self.row() - target_line
        self.view.run_command('scroll_lines', {'amount': offset})

    def screen_extents(self):
        screenful = self.view.visible_region()
        top_row, _ = self.view.rowcol(screenful.begin())
        bottom_row, _ = self.view.rowcol(screenful.end())
        return (top_row, bottom_row)
