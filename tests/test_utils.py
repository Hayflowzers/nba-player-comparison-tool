import unittest
from app.utils import get_player_stats, compare_players_stats

class TestUtils(unittest.TestCase):
    def test_get_player_stats(self):
        stats = get_player_stats('LeBron James')
        self.assertIsNotNone(stats)
        self.assertEqual(stats.iloc[0]['player_name'], 'LeBron James')

    def test_compare_players_stats(self):
        stats1, stats2 = compare_players_stats('LeBron James', 'Kevin Durant')
        self.assertEqual(stats1.iloc[0]['player_name'], 'LeBron James')
        self.assertEqual(stats2.iloc[0]['player_name'], 'Kevin Durant')

if __name__ == '__main__':
    unittest.main()
