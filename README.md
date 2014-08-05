# ShowAtArbitrary

A [Sublime Text 3][ST3] plugin that cycles between moving the current line to the top, middle and bottom of the visible screen area.

## Installation

1. Click `Preferences > Browse Packages...`
2. Clone this repo to that directory: <pre> git clone git://github.com/hbaughman/ShowAtArbitrary.git </pre>

## Commands

This plugin provides a single command called `show_at_arbitrary`. Repeated calls to this command will move the current line to the top, middle, and bottom of the visible screen area. The margin between the current line and the edge of the screen, as well as the order, can be customized in the settings file.

## Keybindings

The default keybinding is `ctrl+shift+g`:

    { "keys": ["ctrl+shift+g"], "command": "show_at_arbitrary" }


## Settings

To change the margins between the current line and the edge of the screen or the ordering of jumps create a file called `Packages/User/ShowAtArbitrary.sublime-settings` and redefine the `target_lines` setting. 

Positive values cause the page to be offset that many lines from the top of the screen. Negative values, that many lines from the bottom. A value of `0` moves the current line to the center as the default sublime feature `show_at_center`.

    { "target_lines": [4, 0, -4] }

[ST3]: http://www.sublimetext.com/3
