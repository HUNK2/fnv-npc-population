import unittest
from allow_new_vars import check, declared


class AllowNewVarsTest(unittest.TestCase):
    OLD = [(1, 'iinit', 1), (2, 'fprice', 0)]

    def test_declared_order_and_kinds(self):
        self.assertEqual(declared('scn X\nint iInit ; c\nfloat fPrice\nbegin GameMode\nend'),
                         [('iinit', 1), ('fprice', 0)])

    def test_append_is_allowed(self):
        self.assertIsNone(check(self.OLD, [('iinit', 1), ('fprice', 0), ('inew', 1)]))

    def test_rename_reorder_retype_remove_are_refused(self):
        for new in ([('iinit', 1), ('fcost', 0)], [('fprice', 0), ('iinit', 1)],
                    [('iinit', 0), ('fprice', 0)], [('iinit', 1)]):
            self.assertIsNotNone(check(self.OLD, new))

    def test_a_function_script_is_told_apart(self):
        from allow_new_vars import is_function
        self.assertTrue(is_function('scn CCBuildFn\n\nint iAct\n\nbegin Function {iAct}\nend\n'))
        self.assertFalse(is_function('scn CCCoreScript\n\nint iInit\n\nbegin GameMode\nend\n'))


if __name__ == '__main__':
    unittest.main()
