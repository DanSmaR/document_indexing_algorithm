from __future__ import annotations
from typing import Generic, TypeVar


from ting_file_management.abstract_queue import AbstractQueue
from utils.linked_list import LinkedList


T = TypeVar("T")


class Queue(AbstractQueue, Generic[T]):
    def __init__(self) -> None:
        self.__list: LinkedList[T] = LinkedList()

    def __len__(self) -> int:
        return len(self.__list)

    def is_empty(self) -> bool:
        return self.__list.is_empty()

    def enqueue(self, value: T) -> None:
        self.__list.add_last(value)

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is already empty")
        return self.__list.remove_first()

    def search(self, index: int) -> T:
        return self.__list.get_element_at(index)
