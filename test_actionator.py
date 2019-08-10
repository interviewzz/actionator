import unittest
from actionator import addAction, getStats, _reset_state


class TestActionator(unittest.TestCase):
    def setUp(self):
        _reset_state()

    def test_add_action_with_valid_json(self):
        error = addAction('{"action":"jump", "time":100}')
        self.assertIsNone(error)

    def test_add_action_returns_error_with_invalid_json(self):
        error = addAction('{forgot_to_use_quotes:jump}')
        self.assertIn('invalid JSON', error)

    def test_add_action_json_not_a_dict(self):
        error = addAction('[1,2,3]')
        self.assertIn('missing required key', error)

    def test_add_action_json_missing_time_key(self):
        error = addAction('{"action":"jump"}')
        self.assertIn('missing required key', error)

    def test_add_action_json_missing_action_key(self):
        error = addAction('{"time":100}')
        self.assertIn('missing required key', error)

    def test_get_stats(self):
        addAction('{"action":"jump", "time":100}')
        addAction('{"action":"jump", "time":100}')
        addAction('{"action":"skip", "time":50}')

        self.assertEqual(getStats(), '[{"action": "jump", "avg": 100.0}, '
                                     '{"action": "skip", "avg": 50.0}]')

    def test_get_stats_rounds_to_two_decimals(self):
        addAction('{"action":"jump", "time":10}')
        addAction('{"action":"jump", "time":40}')
        addAction('{"action":"jump", "time":50}')

        self.assertEqual(getStats(), '[{"action": "jump", "avg": 33.33}]')

    def test_get_stats_returns_empty_with_no_actions(self):
        self.assertEqual(getStats(), '[]')


if __name__ == '__main__':
    unittest.main()
