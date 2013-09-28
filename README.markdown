# PyWorkspaces

Python utilities for working with multiple workspaces in Ubuntu

## System Requirements

 * Ubuntu &ge; 12.10
 * `wmctrl`

# Usage

 * `workspaces.get_windows()` - returns a list of dicts, each containing `id`, `desktop`, `machine`, and `title`
 * `workspaces.move_window(id, x, y)` - moves the window identified by `id` to the desktop located at `(x,y)`

Desktops are indexed starting at (0,0) for the top-left-most. `id` is an internal value.