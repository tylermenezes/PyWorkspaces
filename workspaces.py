#!/usr/bin/python
import re
import subprocess

class workspaces():
    @staticmethod
    def _cmd(*args):
        return subprocess.Popen(args, stdout=subprocess.PIPE).stdout.read().decode("utf-8")

    @staticmethod
    def get_display_size():
        size = (re.split(' *', workspaces._cmd('wmctrl', '-d').replace("\n", "")))[8].split('x')
        return {"x": int(size[0]), "y": int(size[1])}

    @staticmethod
    def get_workspace_count():
        total_size = (re.split(' *', workspaces._cmd('wmctrl', '-d').replace("\n", "")))[3].split('x')
        total_size = [int(x) for x in total_size]
        display = workspaces.get_display_size()
        return {"x": int(total_size[0]/display['x']), "y": int(total_size[1]/display['y'])}

    @staticmethod
    def _workspace_coords_to_screen_coords(x, y):
        disp_size = workspaces.get_display_size()
        workspace_size = workspaces.get_workspace_count()

        x_coord = -1 * disp_size['x'] * (workspace_size['x'] - 1 - x)
        y_coord = -1 * disp_size['y'] * (workspace_size['y'] - 1- y)

        return {"x": x_coord, "y": y_coord}

    @staticmethod
    def move_window(id, desk_x, desk_y):
        coords = workspaces._workspace_coords_to_screen_coords(desk_x, desk_y)
        subprocess.call(['wmctrl', '-i', '-r', id, '-e', '0,' + str(coords['x']) + ',' + str(coords['y']) + ',-1,-1'])

    @staticmethod
    def get_windows():
        windows = workspaces._cmd('wmctrl', '-l').split("\n")
        lines = [re.split(' *', desc, 3) for desc in windows]
        return [dict(zip(['id', 'desktop', 'machine', 'title'], line)) for line in lines]