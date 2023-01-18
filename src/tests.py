from deserialization import Entity, Deserializer
from pandas import to_datetime
import unittest

entity_list = [
    Entity(name='Test1', velocity=50, time=to_datetime('2023-01-18 12:50:00')), 
    Entity(name='Test2', velocity=60, time=to_datetime('2023-01-18 13:50:00')), 
    Entity(name='Test3', velocity=70, time=to_datetime('2023-01-18 14:50:00')), 
    Entity(name='Test3', velocity=80, time=to_datetime('2023-01-18 15:50:00'))
]

class DeserializerTest(unittest.TestCase):
    def csv_test(self):
        self.assertEqual(
            Deserializer.deserialize_csv('../data.csv', 
            entity_list)
            )

if __name__ == "__main__":
    unittest.main()