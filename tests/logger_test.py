import unittest

import src.logger as logger


class LoggingTestCase(unittest.TestCase):
    def test_set_debug(self):
        logger.set_log_level('debug')
        self.assertEqual(logger.log.level, 10)

    def test_set_info(self):
        logger.set_log_level('info')
        self.assertEqual(logger.log.level, 20)

    def test_set_warning(self):
        logger.set_log_level('warning')
        self.assertEqual(logger.log.level, 30)

    def test_set_error(self):
        logger.set_log_level('error')
        self.assertEqual(logger.log.level, 40)


if __name__ == '__main__':
    unittest.main()
