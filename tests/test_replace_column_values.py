import unittest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.replace_column_values import replace_column_values

class TestReplaceColumnValues(unittest.TestCase):
    
    def setUp(self):
        self.data = {
            'Column 1': ['A', 'D', 'I', 'X', 'I', 'N', 'Q'],
            'Column 2': ['B', 'E', 'J', 'Y', 'M', 'O', 'S'],
            'Column 3': ['Type A', 'Type A', 'Type A', 'Type B', 'Type B', 'Type B', 'Type B']
        }
        self.df = pd.DataFrame(self.data)
    
    def test_replace_column_values(self):
        output_df = replace_column_values(self.df)

        expected_data = {
            'Column 1': ['A', 'D', 'I', 'X', 'I', 'N', 'Q'],
            'Column 2': ['D', 'I', 'J', 'I', 'N', 'Q', 'S'],
            'Column 3': ['Type A', 'Type A', 'Type A', 'Type B', 'Type B', 'Type B', 'Type B']
        }
        expected_df = pd.DataFrame(expected_data)
        
        pd.testing.assert_frame_equal(output_df, expected_df)

if __name__ == '__main__':
    unittest.main()
