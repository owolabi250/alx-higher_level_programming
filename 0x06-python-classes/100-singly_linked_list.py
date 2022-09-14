#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Contains the classes Node and SinglyLinkedList."""


class Node:
    """This is the Node class definition."""

    def __init__(self, data, next_node=None):
        """Initialize the data and next_node attributes.
        Args:
            data (int): Data of the node.
            next_node (Node): Next node of the singly linked list.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter method for the data attribute.
        Returns:
            The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for the data attribute.
        Args:
            value (int): Data of the node.
        """
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for the next_node attribute.
        Returns:
            The next node of the singly linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for the next_node attribute.
        Args:
            value (Node): Next node of the singly linked list.
        """
        if isinstance(value, Node) is False and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList(Node):
    """This is the SinglyLinkedList class definition."""

    def __init__(self):
        """Initialize the head attribute."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.
        The new Node should be inserted in ascending order.
        Args:
            value (int): Data of the new node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None:
                if value < current.next_node.data:
                    break
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the list."""
        current = self.__head
        string = ""
        while current is not None:
            string += str(current.data)
            if current.next_node is not None:
                string += "\n"
            current = current.next_node
        return string
