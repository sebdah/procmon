import unittest

import src.process as process


class ProcessMatchTestCase(unittest.TestCase):
    def test_matching_case_sensitive(self):
        self.assertEqual(process.match('abc', 'b'), True)
        self.assertEqual(process.match('abc', 'b', case_insensitive=False), True)

    def test_not_matching_case_sensitive(self):
        self.assertEqual(process.match('abc', 'B'), False)
        self.assertEqual(process.match('abc', 'B', case_insensitive=False), False)

    def test_matching_case_insensitive(self):
        self.assertEqual(process.match('abc', 'B', case_insensitive=True), True)

    def test_no_match(self):
        self.assertEqual(process.match('abc', 'd', case_insensitive=False), False)
        self.assertEqual(process.match('abc', 'd', case_insensitive=True), False)

    def test_match_string_empty(self):
        self.assertEqual(process.match('abc', '', case_insensitive=True), False)

    def test_source_string_empty(self):
        self.assertEqual(process.match('', 'd', case_insensitive=True), False)


class ProcessListProcessesTestCase(unittest.TestCase):
    def test_yield(self):
        procs = []
        for proc in process.list_processes():
            procs.append(proc)

        self.assertGreater(len(procs), 0)


if __name__ == '__main__':
    unittest.main()
