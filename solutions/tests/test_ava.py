import unittest
from ..ava import ListNode, Solution

class TestMergeTwoLists(unittest.TestCase):
    def list_to_nodes(self, lst):
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def nodes_to_list(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def test_merge_two_lists(self):
        solution = Solution()

        list1 = self.list_to_nodes([1, 2, 4])
        list2 = self.list_to_nodes([1, 3, 4])
        merged = solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.nodes_to_list(merged), [1, 1, 2, 3, 4, 4])

        list1 = self.list_to_nodes([])
        list2 = self.list_to_nodes([])
        merged = solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.nodes_to_list(merged), [])

        list1 = self.list_to_nodes([])
        list2 = self.list_to_nodes([0])
        merged = solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.nodes_to_list(merged), [0])
