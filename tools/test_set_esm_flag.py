import struct
import unittest

import set_esm_flag


class SetFlag(unittest.TestCase):
    def test_sets_bit_one_and_keeps_the_rest(self):
        data = b'TES4' + struct.pack('<II', 30, 0x200) + b'\0' * 30
        out = set_esm_flag.set_flag(data)
        self.assertEqual(struct.unpack_from('<I', out, 8)[0], 0x201)
        self.assertEqual(len(out), len(data))
        self.assertEqual(out[12:], data[12:])

    def test_refuses_a_non_plugin(self):
        with self.assertRaises(ValueError):
            set_esm_flag.set_flag(b'XXXX' + b'\0' * 20)


if __name__ == '__main__':
    unittest.main()
