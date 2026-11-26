"""Set the master (ESM) flag on a built plugin, in place.

fnv-mcp's builder writes .esp files only. The core plugin is a master of the company plugin, so its
TES4 header gets flag 0x1 after each build; the engine goes by the flag, not the file extension.

    python tools/set_esm_flag.py <plugin.esp>
"""
import struct
import sys


def set_flag(data: bytes) -> bytes:
    if data[:4] != b'TES4':
        raise ValueError('not a plugin: no TES4 header')
    flags = struct.unpack_from('<I', data, 8)[0]
    return data[:8] + struct.pack('<I', flags | 0x1) + data[12:]


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    with open(argv[0], 'rb') as f:
        data = f.read()
    with open(argv[0], 'wb') as f:
        f.write(set_flag(data))
    print('master flag set on %s' % argv[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
