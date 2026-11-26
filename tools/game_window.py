"""Move the game window to another monitor (Windows only, standard library).

    python tools/game_window.py 2       # monitor 2 (monitors are numbered from the primary, 1)

tools/live.py calls move() at the start of every in-game check when tools/local.json (not in git)
says {"monitor": 2}. The window keeps its size and is centred on that monitor. Losing focus opens the
pause menu: the checks unpause after moving.
"""
import ctypes
import ctypes.wintypes as wt
import json
import sys
from pathlib import Path

LOCAL = Path(__file__).resolve().parent / 'local.json'
SWP_NOSIZE, SWP_NOZORDER, SWP_NOACTIVATE = 0x1, 0x4, 0x10
MONITORINFOF_PRIMARY = 1


class MONITORINFO(ctypes.Structure):
    _fields_ = [('cbSize', wt.DWORD), ('rcMonitor', wt.RECT), ('rcWork', wt.RECT), ('dwFlags', wt.DWORD)]


def monitors():
    """Work areas (left, top, right, bottom), the primary monitor first."""
    user32 = ctypes.windll.user32
    found = []
    proc = ctypes.WINFUNCTYPE(ctypes.c_int, wt.HMONITOR, wt.HDC, ctypes.POINTER(wt.RECT), wt.LPARAM)

    def each(h, _dc, _rc, _lp):
        mi = MONITORINFO()
        mi.cbSize = ctypes.sizeof(MONITORINFO)
        user32.GetMonitorInfoW(h, ctypes.byref(mi))
        r = mi.rcWork
        found.append((not mi.dwFlags & MONITORINFOF_PRIMARY, (r.left, r.top, r.right, r.bottom)))
        return 1

    user32.EnumDisplayMonitors(None, None, proc(each), 0)
    return [r for _, r in sorted(found, key=lambda x: x[0])]


def game_window():
    user32 = ctypes.windll.user32
    for title in ('Fallout: New Vegas', 'FalloutNV'):
        h = user32.FindWindowW(None, title)
        if h:
            return h
    return None


def move(n):
    """Centre the game window on monitor n (1 = primary). False if there is no game window or monitor."""
    mons = monitors()
    h = game_window()
    if not h or not 1 <= n <= len(mons):
        return False
    user32 = ctypes.windll.user32
    r = wt.RECT()
    user32.GetWindowRect(h, ctypes.byref(r))
    w, ht = r.right - r.left, r.bottom - r.top
    left, top, right, bottom = mons[n - 1]
    x = left + max(0, (right - left - w) // 2)
    y = top + max(0, (bottom - top - ht) // 2)
    return bool(user32.SetWindowPos(h, None, x, y, 0, 0, SWP_NOSIZE | SWP_NOZORDER | SWP_NOACTIVATE))


def focus():
    """Bring the game window to the front: in the background the game drops to about 10 frames a
    second and game time crawls. Windows only lets the foreground process hand focus over, so press
    and release Alt first (the usual way round the foreground lock)."""
    h = game_window()
    if not h:
        return False
    user32 = ctypes.windll.user32
    VK_MENU, KEYUP = 0x12, 0x2
    user32.keybd_event(VK_MENU, 0, 0, 0)
    user32.keybd_event(VK_MENU, 0, KEYUP, 0)
    user32.ShowWindow(h, 5)
    return bool(user32.SetForegroundWindow(h))


def wanted_monitor():
    try:
        return int(json.loads(LOCAL.read_text(encoding='utf-8')).get('monitor', 0))
    except (OSError, ValueError):
        return 0


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'focus':
        print('focused' if focus() else 'not focused')
        sys.exit(0)
    print('moved' if move(int(sys.argv[1]) if len(sys.argv) > 1 else wanted_monitor() or 1) else 'not moved')
