from unittest import TestCase, main
from unittest.mock import MagicMock

from src.event import Event

class TestEvent(TestCase):
    def setUp(self):
        self.db = MagicMock()
        self.db.get_data.return_value = [(1,)]
        self.event = Event(self.db, sport='Football" OR "1"="1')

    def test_insert_event_uses_parameterized_sport_lookup(self):
        self.event.insert_event()

        query, params = self.db.get_data.call_args_list[0].args

        self.assertEqual(query, "SELECT ID FROM Sports WHERE Name = :sport")
        self.assertEqual(params, {"sport": 'Football" OR "1"="1'})
        self.assertNotIn('Football" OR "1"="1', query)

    def test_get_event_uses_parameterized_filter_value(self):
        malicious_value = 'Final" OR "1"="1'

        self.event.get_event("competition", malicious_value)

        query, params = self.db.get_data.call_args.args

        self.assertIn("WHERE c.Name = :data", query)
        self.assertEqual(params, {"data": malicious_value})
        self.assertNotIn(malicious_value, query)

    def test_get_event_rejects_unknown_category(self):
        with self.assertRaises(ValueError):
            self.event.get_event("unknown", "value")


if __name__ == "__main__":
    main()
