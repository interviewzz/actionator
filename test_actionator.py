import unittest
import json
from actionator import addAction, getStats

class TestActionator(unittest.TestCase):
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

        self.assertEqual(getStats(), '[{"action":"jump", "avg":100}, '\
        '{"action":"skip", "avg":50}]')

if __name__ == '__main__':
    unittest.main()
