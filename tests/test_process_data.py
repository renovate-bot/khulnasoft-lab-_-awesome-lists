import unittest
import os
import json
from scripts.process_data import process_data

class TestProcessData(unittest.TestCase):

    def setUp(self):
        self.raw_data_dir = 'data/raw/'
        self.processed_data_dir = 'data/processed/'

        if not os.path.exists(self.raw_data_dir):
            os.makedirs(self.raw_data_dir)
        if not os.path.exists(self.processed_data_dir):
            os.makedirs(self.processed_data_dir)

        self.raw_data = [
            {"name": "Repo1", "stars": 1500},
            {"name": "Repo2", "stars": 500}
        ]

        with open(os.path.join(self.raw_data_dir, 'test.json'), 'w') as file:
            json.dump(self.raw_data, file)

    def tearDown(self):
        for dir in [self.raw_data_dir, self.processed_data_dir]:
            for file in os.listdir(dir):
                os.remove(os.path.join(dir, file))
            os.rmdir(dir)

    def test_process_data(self):
        process_data()
        processed_file = os.path.join(self.processed_data_dir, 'test.json')

        self.assertTrue(os.path.exists(processed_file))

        with open(processed_file, 'r') as file:
            processed_data = json.load(file)

        self.assertEqual(len(processed_data), 1)
        self.assertEqual(processed_data[0]['name'], 'Repo1')

if __name__ == '__main__':
    unittest.main()
