#!/usr/bin/env python3

import unittest
from bstree import tree_node, recursive_bstree, iterative_bstree

class recursive_bstree_Test(unittest.TestCase):
    def test_case_1(self):
        main_tree = recursive_bstree()

        self.assertTrue(main_tree.empty())
        self.assertEqual(len(main_tree), 0)
        self.assertEqual(main_tree.max_height(), 0)
        self.assertTrue(main_tree.balanced())

        answer_res = []

        def value_capture(value):
            answer_res.append(value)

        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [])

        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [])

        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [])


        # add 10 4 14 2 7
        main_tree.push(10).push(4).push(14).push(2).push(7)

        """
        Current tree :

                    10
                   / \\
                  4   14
                 / \\
                2   7

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 5)
        self.assertEqual(main_tree.max_height(), 3)
        self.assertTrue(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [10, 4, 2, 7, 14])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [2, 4, 7, 10, 14])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [2, 7, 4, 14, 10])


        # add 18 3 1 0
        main_tree.push(18).push(3).push(1).push(0)

        """
        Current tree :

                    10
                   / \\
                  4   14
                 / \\  \\
                2   7   18
               / \\
              1   3
             /
            0

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 9)
        self.assertEqual(main_tree.max_height(), 5)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [10, 4, 2, 1, 0, 3, 7, 14, 18])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [0, 1, 2, 3, 4, 7, 10, 14, 18])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [0, 1, 3, 2, 7, 4, 18, 14, 10])


        tree2 = main_tree.deepcopy()

        self.assertEqual(main_tree, tree2)
        self.assertTrue(main_tree.equal(tree2))

        node1 = main_tree.find(10)
        node2 = main_tree.find(7)
        node3 = main_tree.find(18)

        self.assertIsNotNone(node1)
        self.assertIsNotNone(node2)
        self.assertIsNotNone(node3)


        # add 9, 5, 17
        self.assertTrue(main_tree.insert(node1, 9))
        self.assertTrue(main_tree.insert(node2, 5))
        self.assertTrue(main_tree.insert(node3, 17))

        """
        Current tree :

                     9
                  /    \\
                 4      14
                / \\   /  \\
               2   5  10   17
              / \\  \\      \\
             1   3   7       18
            /
           0

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 12)
        self.assertEqual(main_tree.max_height(), 5)
        self.assertTrue(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [9, 4, 2, 1, 0, 3, 5, 7, 14, 10, 17, 18])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [0, 1, 2, 3, 4, 5, 7, 9, 10, 14, 17, 18])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [0, 1, 3, 2, 7, 5, 4, 10, 18, 17, 14, 9])


        self.assertFalse(main_tree.erase(42))
        self.assertFalse(main_tree.erase(6))

        # remove 5, 9, 1, 18
        self.assertTrue(main_tree.erase(5))
        self.assertTrue(main_tree.erase(9))
        self.assertTrue(main_tree.erase(1))
        self.assertTrue(main_tree.erase(18))

        """
        Current tree :

                     7
                    / \\
                   4   14
                  /   /  \\
                 2   10   17
                / \\
               0   3

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 8)
        self.assertEqual(main_tree.max_height(), 4)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [7, 4, 2, 0, 3, 14, 10, 17])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [0, 2, 3, 4, 7, 10, 14, 17])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [0, 3, 2, 4, 10, 17, 14, 7])


        tree2 = main_tree.deepcopy()

        self.assertEqual(main_tree, tree2)
        self.assertTrue(main_tree.equal(tree2))


        # remove 2, 7, 14, 17, 10
        self.assertTrue(main_tree.erase(2))
        self.assertTrue(main_tree.erase(7))
        self.assertTrue(main_tree.erase(14))
        self.assertTrue(main_tree.erase(17))
        self.assertTrue(main_tree.erase(10))

        """
        Current tree :

                     4
                    /
                   0
                    \\
                     3
        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 3)
        self.assertEqual(main_tree.max_height(), 3)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [4, 0, 3])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [0, 3, 4])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [3, 0, 4])

        self.assertNotEqual(main_tree, tree2)
        self.assertFalse(main_tree.equal(tree2))


        # remove 3, 0, 4
        self.assertTrue(main_tree.erase(3))
        self.assertTrue(main_tree.erase(0))
        self.assertTrue(main_tree.erase(4))

        """
        Tree is empty now
        """

        self.assertTrue(main_tree.empty())
        self.assertEqual(len(main_tree), 0)
        self.assertEqual(main_tree.max_height(), 0)
        self.assertTrue(main_tree.balanced())

        self.assertNotEqual(main_tree, tree2)
        self.assertFalse(main_tree.equal(tree2))

    def test_case_2(self):
        main_tree = recursive_bstree()
        tree2 = main_tree.deepcopy()

        self.assertEqual(main_tree, tree2)
        self.assertTrue(main_tree.equal(tree2))
        self.assertIsNone(main_tree.find(-14))
        self.assertFalse(main_tree.erase(-14))

        # add -27
        main_tree.push(-27)

        tree2.push(-27)

        self.assertEqual(main_tree, tree2)
        self.assertTrue(main_tree.equal(tree2))

        tree2.push(-14)

        self.assertNotEqual(main_tree, tree2)
        self.assertFalse(main_tree.equal(tree2))

        # add -14
        main_tree.push(-14)

        self.assertEqual(main_tree, tree2)
        self.assertTrue(main_tree.equal(tree2))

        # add -5
        main_tree.push(-5)

        self.assertNotEqual(main_tree, tree2)
        self.assertFalse(main_tree.equal(tree2))

        """
        Current tree :

                    -27
                      \\
                       -14
                         \\
                          -5

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 3)
        self.assertEqual(main_tree.max_height(), 3)
        self.assertFalse(main_tree.balanced())

        answer_res = []

        def value_capture(value):
            answer_res.append(value)

        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [-27, -14, -5])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [-27, -14, -5])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [-5, -14, -27])


        self.assertFalse(main_tree.insert(tree_node(42), -26))
        self.assertFalse(main_tree.insert(tree_node(-14), -26))
        self.assertFalse(main_tree.insert(tree_node(-27), -26))

        self.assertIsNone(main_tree.find(52))
        self.assertIsNone(main_tree.find(-26))

        node = main_tree.find(-14)

        self.assertIsNotNone(node)

        # add -19
        self.assertTrue(main_tree.insert(node, -19))

        node2 = main_tree.find(-5)

        self.assertIsNotNone(node2)

        # add -10, -7
        self.assertTrue(main_tree.insert(node2, -10))
        self.assertTrue(main_tree.insert(node2, -7))

        """
        Current tree :

                    -27
                      \\
                      -19
                        \\
                         -10
                         / \\
                       -14  -7
                             \\
                              -5

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 6)
        self.assertEqual(main_tree.max_height(), 5)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [-27, -19, -10, -14, -7, -5])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [-27, -19, -14, -10, -7, -5])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [-14, -5, -7, -10, -19, -27])

        # add -6, -17, -52
        self.assertTrue(main_tree.insert(node2, -6))
        self.assertTrue(main_tree.insert(node, -17))
        main_tree.push(-52)

        """
        Current tree :

                    -27
                    / \\
                  -52  -19
                         \\
                          -10
                          / \\
                        -17  -7
                          \\  \\
                          -14  -6
                                \\
                                 -5

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 9)
        self.assertEqual(main_tree.max_height(), 6)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(
            answer_res, [-27, -52, -19, -10, -17, -14, -7, -6, -5])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(
            answer_res, [-52, -27, -19, -17, -14, -10, -7, -6, -5])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(
            answer_res, [-52, -14, -17, -5, -6, -7, -10, -19, -27])


        tree2 = main_tree.deepcopy()

        # remove -10, -6, -52, -17
        self.assertTrue(main_tree.erase(-10))
        self.assertTrue(main_tree.erase(-6))
        self.assertTrue(main_tree.erase(-52))
        self.assertTrue(main_tree.erase(-17))

        """
        Current tree :

                    -27
                      \\
                       -19
                         \\
                          -14
                            \\
                             -7
                              \\
                               -5

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 5)
        self.assertEqual(main_tree.max_height(), 5)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [-27, -19, -14, -7, -5])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [-27, -19, -14, -7, -5])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [-5, -7, -14, -19, -27])


        self.assertNotEqual(main_tree, tree2)
        self.assertFalse(main_tree.equal(tree2))
        self.assertIsNone(main_tree.find(-10))
        self.assertIsNone(main_tree.find(-6))
        self.assertIsNone(main_tree.find(-52))
        self.assertIsNone(main_tree.find(-17))


class iterative_bstree_Test(unittest.TestCase):
    def test_case_1(self):
        main_tree = iterative_bstree()

        self.assertTrue(main_tree.empty())
        self.assertEqual(len(main_tree), 0)
        self.assertEqual(main_tree.max_height(), 0)
        self.assertEqual(main_tree.max_width(), 0)
        self.assertTrue(main_tree.balanced())

        answer_res = []

        def value_capture(value):
            answer_res.append(value)

        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [])

        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [])

        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [])


        # add 10 4 14 2 7
        main_tree.push(10).push(4).push(14).push(2).push(7)

        """
        Current tree :

                    10
                   / \\
                  4   14
                 / \\
                2   7

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 5)
        self.assertEqual(main_tree.max_height(), 3)
        self.assertEqual(main_tree.max_width(), 2)
        self.assertTrue(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [10, 4, 2, 7, 14])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [2, 4, 7, 10, 14])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [2, 7, 4, 14, 10])


        # add 18 3 1 0
        main_tree.push(18).push(3).push(1).push(0)

        """
        Current tree :

                    10
                   / \\
                  4   14
                 / \\  \\
                2   7   18
               / \\
              1   3
             /
            0

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 9)
        self.assertEqual(main_tree.max_height(), 5)
        self.assertEqual(main_tree.max_width(), 3)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [10, 4, 2, 1, 0, 3, 7, 14, 18])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [0, 1, 2, 3, 4, 7, 10, 14, 18])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [0, 1, 3, 2, 7, 4, 18, 14, 10])


        tree2 = main_tree.deepcopy()

        self.assertEqual(main_tree, tree2)
        self.assertTrue(main_tree.equal(tree2))

        node1 = main_tree.find(10)
        node2 = main_tree.find(7)
        node3 = main_tree.find(18)

        self.assertIsNotNone(node1)
        self.assertIsNotNone(node2)
        self.assertIsNotNone(node3)


        # add 9, 5, 17
        self.assertTrue(main_tree.insert(node1, 9))
        self.assertTrue(main_tree.insert(node2, 5))
        self.assertTrue(main_tree.insert(node3, 17))

        """
        Current tree :

                     9
                  /    \\
                 4      14
                / \\   /  \\
               2   5  10   17
              / \\  \\      \\
             1   3   7       18
            /
           0

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 12)
        self.assertEqual(main_tree.max_height(), 5)
        self.assertEqual(main_tree.max_width(), 4)
        self.assertTrue(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [9, 4, 2, 1, 0, 3, 5, 7, 14, 10, 17, 18])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [0, 1, 2, 3, 4, 5, 7, 9, 10, 14, 17, 18])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [0, 1, 3, 2, 7, 5, 4, 10, 18, 17, 14, 9])


        self.assertFalse(main_tree.erase(42))
        self.assertFalse(main_tree.erase(6))

        # remove 5, 9, 1, 18
        self.assertTrue(main_tree.erase(5))
        self.assertTrue(main_tree.erase(9))
        self.assertTrue(main_tree.erase(1))
        self.assertTrue(main_tree.erase(18))

        """
        Current tree :

                     7
                    / \\
                   4   14
                  /   /  \\
                 2   10   17
                / \\
               0   3

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 8)
        self.assertEqual(main_tree.max_height(), 4)
        self.assertEqual(main_tree.max_width(), 3)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [7, 4, 2, 0, 3, 14, 10, 17])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [0, 2, 3, 4, 7, 10, 14, 17])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [0, 3, 2, 4, 10, 17, 14, 7])


        tree2 = main_tree.deepcopy()

        self.assertEqual(main_tree, tree2)
        self.assertTrue(main_tree.equal(tree2))


        # remove 2, 7, 14, 17, 10
        self.assertTrue(main_tree.erase(2))
        self.assertTrue(main_tree.erase(7))
        self.assertTrue(main_tree.erase(14))
        self.assertTrue(main_tree.erase(17))
        self.assertTrue(main_tree.erase(10))

        """
        Current tree :

                     4
                    /
                   0
                    \\
                     3
        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 3)
        self.assertEqual(main_tree.max_height(), 3)
        self.assertEqual(main_tree.max_width(), 1)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [4, 0, 3])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [0, 3, 4])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [3, 0, 4])

        self.assertNotEqual(main_tree, tree2)
        self.assertFalse(main_tree.equal(tree2))


        # remove 3, 0, 4
        self.assertTrue(main_tree.erase(3))
        self.assertTrue(main_tree.erase(0))
        self.assertTrue(main_tree.erase(4))

        """
        Tree is empty now
        """

        self.assertTrue(main_tree.empty())
        self.assertEqual(len(main_tree), 0)
        self.assertEqual(main_tree.max_height(), 0)
        self.assertEqual(main_tree.max_width(), 0)
        self.assertTrue(main_tree.balanced())

        self.assertNotEqual(main_tree, tree2)
        self.assertFalse(main_tree.equal(tree2))

    def test_case_2(self):
        main_tree = iterative_bstree()
        tree2 = main_tree.deepcopy()

        self.assertEqual(main_tree, tree2)
        self.assertTrue(main_tree.equal(tree2))
        self.assertIsNone(main_tree.find(-14))
        self.assertFalse(main_tree.erase(-14))

        # add -27
        main_tree.push(-27)

        tree2.push(-27)

        self.assertEqual(main_tree, tree2)
        self.assertTrue(main_tree.equal(tree2))

        tree2.push(-14)

        self.assertNotEqual(main_tree, tree2)
        self.assertFalse(main_tree.equal(tree2))

        # add -14
        main_tree.push(-14)

        self.assertEqual(main_tree, tree2)
        self.assertTrue(main_tree.equal(tree2))

        # add -5
        main_tree.push(-5)

        self.assertNotEqual(main_tree, tree2)
        self.assertFalse(main_tree.equal(tree2))

        """
        Current tree :

                    -27
                      \\
                       -14
                         \\
                          -5

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 3)
        self.assertEqual(main_tree.max_height(), 3)
        self.assertEqual(main_tree.max_width(), 1)
        self.assertFalse(main_tree.balanced())

        answer_res = []

        def value_capture(value):
            answer_res.append(value)

        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [-27, -14, -5])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [-27, -14, -5])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [-5, -14, -27])


        self.assertFalse(main_tree.insert(tree_node(42), -26))
        self.assertFalse(main_tree.insert(tree_node(-14), -26))
        self.assertFalse(main_tree.insert(tree_node(-27), -26))

        self.assertIsNone(main_tree.find(52))
        self.assertIsNone(main_tree.find(-26))

        node = main_tree.find(-14)

        self.assertIsNotNone(node)

        # add -19
        self.assertTrue(main_tree.insert(node, -19))

        node2 = main_tree.find(-5)

        self.assertIsNotNone(node2)

        # add -10, -7
        self.assertTrue(main_tree.insert(node2, -10))
        self.assertTrue(main_tree.insert(node2, -7))

        """
        Current tree :

                    -27
                      \\
                      -19
                        \\
                         -10
                         / \\
                       -14  -7
                             \\
                              -5

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 6)
        self.assertEqual(main_tree.max_height(), 5)
        self.assertEqual(main_tree.max_width(), 2)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [-27, -19, -10, -14, -7, -5])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [-27, -19, -14, -10, -7, -5])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [-14, -5, -7, -10, -19, -27])

        # add -6, -17, -52
        self.assertTrue(main_tree.insert(node2, -6))
        self.assertTrue(main_tree.insert(node, -17))
        main_tree.push(-52)

        """
        Current tree :

                    -27
                    / \\
                  -52  -19
                         \\
                          -10
                          / \\
                        -17  -7
                          \\  \\
                          -14  -6
                                \\
                                 -5

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 9)
        self.assertEqual(main_tree.max_height(), 6)
        self.assertEqual(main_tree.max_width(), 2)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(
            answer_res, [-27, -52, -19, -10, -17, -14, -7, -6, -5])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(
            answer_res, [-52, -27, -19, -17, -14, -10, -7, -6, -5])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(
            answer_res, [-52, -14, -17, -5, -6, -7, -10, -19, -27])


        tree2 = main_tree.deepcopy()

        # remove -10, -6, -52, -17
        self.assertTrue(main_tree.erase(-10))
        self.assertTrue(main_tree.erase(-6))
        self.assertTrue(main_tree.erase(-52))
        self.assertTrue(main_tree.erase(-17))

        """
        Current tree :

                    -27
                      \\
                       -19
                         \\
                          -14
                            \\
                             -7
                              \\
                               -5

        """

        self.assertFalse(main_tree.empty())
        self.assertEqual(len(main_tree), 5)
        self.assertEqual(main_tree.max_height(), 5)
        self.assertEqual(main_tree.max_width(), 1)
        self.assertFalse(main_tree.balanced())

        answer_res.clear()
        main_tree.preorder(value_capture)
        self.assertEqual(answer_res, [-27, -19, -14, -7, -5])

        answer_res.clear()
        main_tree.inorder(value_capture)
        self.assertEqual(answer_res, [-27, -19, -14, -7, -5])

        answer_res.clear()
        main_tree.postorder(value_capture)
        self.assertEqual(answer_res, [-5, -7, -14, -19, -27])


        self.assertNotEqual(main_tree, tree2)
        self.assertFalse(main_tree.equal(tree2))
        self.assertIsNone(main_tree.find(-10))
        self.assertIsNone(main_tree.find(-6))
        self.assertIsNone(main_tree.find(-52))
        self.assertIsNone(main_tree.find(-17))


if __name__ == "__main__":
    import random

    unittest.TestLoader.sortTestMethodsUsing = \
        lambda _1, _2, _3: random.choice([1, 0, -1])

    unittest.main()
