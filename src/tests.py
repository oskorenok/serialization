from pandas import to_datetime

from deserialization import Deserializer, Entity

entity_list = [
    Entity(name="Test1", velocity=50, time=to_datetime("2023-01-18 12:50:00")),
    Entity(name="Test2", velocity=60, time=to_datetime("2023-01-18 13:50:00")),
    Entity(name="Test3", velocity=70, time=to_datetime("2023-01-18 14:50:00")),
    Entity(name="Test3", velocity=80, time=to_datetime("2023-01-18 15:50:00")),
]


def test_csv_deserializer() -> None:
    assert (
        Deserializer.deserialize_csv("data.csv") == entity_list
    ), "Deserialized data from data.csv isn't equal to entity_list"


def test_json_deserializer() -> None:
    assert (
        Deserializer.deserialize_json("data.csv") == entity_list
    ), "Deserialized data from data.json isn't equal to entity_list"


def test_yaml_deserializer() -> None:
    assert (
        Deserializer.deserialize_yaml("data.csv") == entity_list
    ), "Deserialized data from data.yaml isn't equal to entity_list"


if __name__ == "__main__":
    test_csv_deserializer()
    print("OK")
