import unittest
from sql import Postgres


class Test(unittest.TestCase):

    def test_db(self):
        pg = Postgres()
        pg.populate()
        count = pg.read()
        self.failIf(count != 5)
        pg.disconnect()


def main():
    unittest.main()

if __name__ == '__main__':
    main()
