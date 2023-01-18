import datetime
import json
from dataclasses import dataclass
from typing import Any, List

import numpy as np
import pandas as pd


@dataclass
class Entity:
    """
    Entity dataclass that has three fields.

    Attributes:
        name(str): The name of entity.
        velocity(int): The measured velocity.
        time(datetime): Date/Time of measurement.
    """

    name: str
    velocity: int
    time: datetime.datetime

    def __setattr__(self, __name: str, __value: Any) -> None:
        """Overridden __settatr__ method that checks typing

        Args:
            __name (str): The attribute name.
            __value (Any): The value of attribute to be checked.

        Raises:
            RuntimeError: ValueError

        Returns:
            None
        """
        if __name == "name":
            if not isinstance(__value, str):
                raise ValueError("name must be string")
            self.__dict__[__name] = __value

        elif __name == "velocity":
            if not isinstance(__value, int):
                raise ValueError("velocity must be integer")
            self.__dict__[__name] = __value

        elif __name == "time":
            if not isinstance(__value, datetime.datetime):
                raise ValueError("name must be datetime object")
            self.__dict__[__name] = __value


class Deserializer:
    """
    Deserializer class that do deserialization.
    """

    @staticmethod
    def read_and_transform(dataframe: pd.DataFrame) -> List[Entity]:
        """
        Method that takes dataframe (Pandas/Dask) iterates within it
        and returns the Entity list.

        Args:
            dataframe (pd.DataFrame/dask.DataFrame): DataFrame

        Returns:
            List[Entity]: List of deserialized entities.
        """
        entities = []
        for _, rows in dataframe.iterrows():
            entities.append(
                Entity(
                    rows["Name"],
                    rows["Velocity"],
                    pd.to_datetime(rows["Time"]),
                )
            )
        return entities

    @classmethod
    def deserialize_csv(cls, file_path: str) -> List[Entity]:
        """
        CSV file deserialization class method.

        Args:
            file_path (str): Path to the file.

        Returns:
            List[Entity]: List of deserialized entities.
        """

        data = pd.read_csv(file_path, index_col=False)
        return cls.read_and_transform(data)

    @classmethod
    def deserialize_json(cls, file_path: str) -> List[Entity]:
        """
        JSON deserialization class method.

        Args:
            file_path (str): Path to the file.

        Returns:
            List[Entity]: List of deserialized entities.
        """
        data = pd.read_json(file_path)
        return cls.read_and_transform(data)

    @classmethod
    def deserialize_xml(cls, file_path: str) -> List[Entity]:
        """
        XML deserialization class method.

        Args:
            file_path (str): Path to the file.

        Returns:
            List[Entity]: List of deserialized entities.
        """
        data = pd.read_xml(file_path)
        return cls.read_and_transform(data)
