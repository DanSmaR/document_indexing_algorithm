from __future__ import annotations
from typing import Generic, TypeVar, Optional


T = TypeVar("T")


class LinkedList(Generic[T]):
    class Node(Generic[T]):
        def __init__(
                self,
                value: T,
                prev: Optional[LinkedList.Node],
                next: Optional[LinkedList.Node]
                ):
            self.value = value
            self.next = next
            self.prev = prev

        def __str__(self):
            return (
                f"Node(value={self.value}",
                f" prev={self.prev}, next={self.next})"
            )

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__length = 0

    def __str__(self) -> str:
        return f"LinkedList(len={self.__length}, value={self.head})"

    def __len__(self) -> int:
        return self.__length

    def is_empty(self) -> bool:
        return self.__length == 0

    def add_first(self, value: T) -> None:
        if self.is_empty():
            self.head = self.tail = LinkedList.Node(value, None, None)
        else:
            self.head.prev = LinkedList.Node(value, None, self.head)
            self.head = self.head.prev
        self.__length += 1

    def add_last(self, value: T) -> None:
        if self.is_empty():
            self.head = self.tail = LinkedList.Node(value, None, None)
        else:
            self.tail.next = LinkedList.Node(value, self.tail, None)
            self.tail = self.tail.next
        self.__length += 1

    def remove_first(self) -> T:
        if self.is_empty():
            raise RuntimeError("There's no item to remove")
        node_value: T = self.head.value
        self.head = self.head.next
        self.__length -= 1

        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None

        return node_value

    def remove_last(self) -> T:
        if self.is_empty():
            raise RuntimeError("There's no item to remove")
        node_value: T = self.tail.value
        self.tail = self.tail.prev
        self.__length -= 1

        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None

        return node_value

    def get_element_at(self, index: int) -> Optional[T]:
        if self.is_empty():
            return None
        if index < 0 or index >= self.__length:
            raise IndexError("Índice Inválido ou Inexistente")
        node_to_get_the_value = self.head
        if not node_to_get_the_value:
            return None
        while index > 0 and node_to_get_the_value.next:
            node_to_get_the_value = node_to_get_the_value.next
            index -= 1
        return node_to_get_the_value.value
