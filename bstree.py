from queue import Queue, LifoQueue

class tree_node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class recursive_bstree:
    __slots__ = ("_size", "_root")

    def __init__(self):
        self._size = 0
        self._root = None

    def empty(self):
        return False if self._root else True

    def __len__(self):
        return self._size

    def __eq__(self, other):
        return self.equal(other)

    def equal(self, other):
        if not self._root and not other._root and self._size == other._size:
            return True
        elif self._root and not other._root \
             or other._root and not self._root \
             or self._size != other._size:
            return False

        def recursion(node, node2):
            if node.value != node2.value:
                return False

            if node.left and node2.left:
                if not recursion(node.left, node2.left):
                    return False
            elif node.left and not node2.left or node2.left and not node.left:
                return False

            if node.right and node2.right:
                if not recursion(node.right, node2.right):
                    return False
            elif node.right and not node2.right \
                 or node2.right and not node.right:
                return False

            return True

        return recursion(self._root, other._root)

    def max_height(self):
        if not self._root:
            return 0

        def recursion(node):
            left_height = recursion(node.left) if node.left else 0
            right_height = recursion(node.right) if node.right else 0

            return 1 + max(left_height, right_height)

        return recursion(self._root)

    def balanced(self):
        if not self._root:
            return True

        def recursion(node):
            left_balanced, left_height = \
                recursion(node.left) if node.left else (True, 0)

            # to stop recursion only
            if not left_balanced:
                return False, 0

            right_balanced, right_height = \
                recursion(node.right) if node.right else (True, 0)

            # to stop recursion only
            if not right_balanced:
                return False, 0

            def take_a_look_balance_factor():
                balance_factor = left_height - right_height

                return balance_factor >= -1 and balance_factor <= 1

            if not take_a_look_balance_factor():
                return False, 0

            return True, 1 + max(left_height, right_height)

        return recursion(self._root)[0]

    def deepcopy(self):
        tree = recursive_bstree()

        if not self._root:
            return tree

        tree._root = tree_node(self._root.value)

        def recursion(node, node2):
            if node.left:
                node2.left = tree_node(node.left.value)
                recursion(node.left, node2.left)
            if node.right:
                node2.right = tree_node(node.right.value)
                recursion(node.right, node2.right)

        recursion(self._root, tree._root)

        tree._size = self._size

        return tree

    def preorder(self, func):
        if not self._root:
            return

        def recursion(node):
            func(node.value)

            if node.left:
                recursion(node.left)

            if node.right:
                recursion(node.right)

        recursion(self._root)

    def inorder(self, func):
        if not self._root:
            return

        def recursion(node):
            if node.left:
                recursion(node.left)

            func(node.value)

            if node.right:
                recursion(node.right)

        recursion(self._root)

    def postorder(self, func):
        if not self._root:
            return

        def recursion(node):
            if node.left:
                recursion(node.left)

            if node.right:
                recursion(node.right)

            func(node.value)

        recursion(self._root)

    def find(self, value):
        if not self._root:
            return None

        def recursion(node):
            if value == node.value:
                return node
            elif value < node.value:
                if not node.left:
                    return None

                return recursion(node.left)
            else:
                if not node.right:
                    return None

                return recursion(node.right)

        return recursion(self._root)

    def push(self, value):
        if not self._root:
            self._root = tree_node(value)
            self._size = 1
            return self

        def recursion(node):
            if value < node.value:
                if not node.left:
                    node.left = tree_node(value)
                else:
                    recursion(node.left)
            else:
                if not node.right:
                    node.right = tree_node(value)
                else:
                    recursion(node.right)

        recursion(self._root)

        self._size += 1

        return self

    def insert(self, existing_node, value_to_insert):
        def recursion(node):
            if existing_node.value == node.value \
               and existing_node is node:
                node_to_insert = tree_node(value_to_insert)

                node_to_insert.left = node.left

                if node.right:
                    node_to_insert.right = node.right

                    def reinsert(node2, node_to_reinsert):
                        if node2.left:
                            reinsert(node2.left, node_to_reinsert)
                        else:
                            node2.left = node_to_reinsert

                    reinsert(node.right, node)
                else:
                    node_to_insert.right = node

                node.left = None
                node.right = None

                return True, node_to_insert
            elif existing_node.value < node.value:
                if not node.left:
                    return False, node

                inserted, node.left = recursion(node.left)

                return inserted, node
            else:
                if not node.right:
                    return False, node

                inserted, node.right = recursion(node.right)

                return inserted, node

        inserted, self._root = recursion(self._root)

        if inserted:
            self._size += 1

        return inserted

    def erase(self, value):
        if not self._root:
            return False

        def recursion(node):
            if value == node.value:
                if not node.left and not node.right:
                    substitution_node = None
                elif node.left and not node.right:
                    substitution_node = node.left
                elif node.right and not node.left:
                    substitution_node = node.right
                else:
                    def find_substitution(current, parent):
                        if not current.left and not current.right:
                            if current is parent.right:
                                parent.right = None
                            return current
                        elif current.left and not current.right:
                            if current is parent.right:
                                parent.right = current.left
                            return current
                        else:
                            return find_substitution(current.right, current)

                    substitution_node = find_substitution(node.left, node)

                    if substitution_node is not node.left:
                        substitution_node.left = node.left
                    substitution_node.right = node.right

                return True, substitution_node
            elif value < node.value and node.left:
                erased, node.left = recursion(node.left)
            elif value > node.value and node.right:
                erased, node.right = recursion(node.right)
            else:
                erased = False

            return erased, node

        erased, self._root = recursion(self._root)

        if erased:
            self._size -= 1

        return erased


class iterative_bstree:
    __slots__ = ("_size", "_root")

    def __init__(self):
        self._size = 0
        self._root = None

    def empty(self):
        return False if self._root else True

    def __len__(self):
        return self._size

    def __eq__(self, other):
        return self.equal(other)

    def equal(self, other):
        if not self._root and not other._root and self._size == other._size:
            return True
        elif self._root and not other._root \
             or other._root and not self._root \
             or self._size != other._size:
            return False

        stack = LifoQueue()
        stack2 = LifoQueue()
        node = self._root
        node2 = other._root

        while True:
            if node.right and node2.right:
                stack.put_nowait(node.right)
                stack2.put_nowait(node2.right)
            elif node.right and not node2.right \
                 or node2.right and not node.right:
                return False

            if node.value != node2.value:
                return False

            if node.left and node2.left:
                node = node.left
                node2 = node2.left
                continue
            elif node.left and not node2.left or node2.left and not node.left:
                return False

            if stack.empty():
                break

            node = stack.get_nowait()
            node2 = stack2.get_nowait()

        return True

    def max_height(self):
        if not self._root:
            return 0

        stack = LifoQueue()
        height_res_stack = LifoQueue()
        node = self._root
        previously_consumed = self._root

        while True:
            if previously_consumed is not node.left \
               and previously_consumed is not node.right:
                while node.left:
                    stack.put_nowait(node)

                    if node.right:
                        stack.put_nowait(node.right)

                    node = node.left

                if node.right:
                    stack.put_nowait(node)
                    node = node.right
                    continue

                height = 1
            else:
                if node.left and node.right:
                    left_height = height_res_stack.get_nowait()
                    right_height = height_res_stack.get_nowait()
                elif node.left and not node.right:
                    left_height = height_res_stack.get_nowait()
                    right_height = 0
                elif node.right and not node.left:
                    right_height = height_res_stack.get_nowait()
                    left_height = 0

                height = 1 + max(left_height, right_height)

            height_res_stack.put_nowait(height)

            if stack.empty():
                break

            previously_consumed = node
            node = stack.get_nowait()

        return height_res_stack.get_nowait()

    def max_width(self):
        if not self._root:
            return 0

        width = 1
        queue = Queue()
        lower_row = Queue()
        node = self._root

        while True:
            if node.left:
                lower_row.put_nowait(node.left)
            if node.right:
                lower_row.put_nowait(node.right)

            if width < lower_row.qsize():
                width = lower_row.qsize()

            if not queue.empty():
                node = queue.get_nowait()
                continue

            if lower_row.empty():
                break

            queue = lower_row
            lower_row = Queue()
            node = queue.get_nowait()

        return width

    def balanced(self):
        if not self._root:
            return True

        stack = LifoQueue()
        height_res_stack = LifoQueue()
        node = self._root
        previously_consumed = self._root

        while True:
            if previously_consumed is not node.left \
               and previously_consumed is not node.right:
                while node.left:
                    stack.put_nowait(node)

                    if node.right:
                        stack.put_nowait(node.right)

                    node = node.left

                if node.right:
                    stack.put_nowait(node)
                    node = node.right
                    continue

                height = 1
            else:
                if node.left and node.right:
                    left_height = height_res_stack.get_nowait()
                    right_height = height_res_stack.get_nowait()
                elif node.left and not node.right:
                    left_height = height_res_stack.get_nowait()
                    right_height = 0
                elif node.right and not node.left:
                    right_height = height_res_stack.get_nowait()
                    left_height = 0

                def take_a_look_balance_factor():
                    balance_factor = left_height - right_height

                    return balance_factor >= -1 and balance_factor <= 1

                if not take_a_look_balance_factor():
                    return False

                height = 1 + max(left_height, right_height)

            height_res_stack.put_nowait(height)

            if stack.empty():
                break

            previously_consumed = node
            node = stack.get_nowait()

        return True

    def deepcopy(self):
        tree = iterative_bstree()

        if not self._root:
            return tree

        tree._root = tree_node(self._root.value)

        stack = LifoQueue()
        stack2 = LifoQueue()
        node = self._root
        node2 = tree._root

        while True:
            if node.right:
                node2.right = tree_node(node.right.value)
                stack.put_nowait(node.right)
                stack2.put_nowait(node2.right)

            if node.left:
                node2.left = tree_node(node.left.value)
                node = node.left
                node2 = node2.left
                continue

            if stack.empty():
                break

            node = stack.get_nowait()
            node2 = stack2.get_nowait()

        tree._size = self._size

        return tree

    def preorder(self, func):
        if not self._root:
            return

        stack = LifoQueue()
        node = self._root

        while True:
            func(node.value)

            if node.right:
                stack.put_nowait(node.right)

            if node.left:
                node = node.left
                continue

            if stack.empty():
                break

            node = stack.get_nowait()

    def inorder(self, func):
        if not self._root:
            return

        stack = LifoQueue()
        node = self._root
        from_stack = False

        while True:
            while not from_stack and node.left:
                stack.put_nowait(node)
                node = node.left

            func(node.value)

            if node.right:
                node = node.right
                from_stack = False
                continue

            if stack.empty():
                break

            node = stack.get_nowait()
            from_stack = True

    def postorder(self, func):
        if not self._root:
            return

        stack = LifoQueue()
        node = self._root
        previously_consumed = self._root

        while True:
            if previously_consumed is not node.left \
               and previously_consumed is not node.right:
                while node.left:
                    stack.put_nowait(node)

                    if node.right:
                        stack.put_nowait(node.right)

                    node = node.left

                if node.right:
                    stack.put_nowait(node)
                    node = node.right
                    continue

            func(node.value)

            if stack.empty():
                break

            previously_consumed = node
            node = stack.get_nowait()

    def find(self, value):
        if not self._root:
            return None

        node = self._root

        while True:
            if value == node.value:
                return node
            elif value < node.value:
                if not node.left:
                    return None

                node = node.left
            else:
                if not node.right:
                    return None

                node = node.right

    def push(self, value):
        if not self._root:
            self._root = tree_node(value)
            self._size = 1
            return self

        node = self._root

        while True:
            if value < node.value:
                if not node.left:
                    node.left = tree_node(value)
                    break
                node = node.left
            else:
                if not node.right:
                    node.right = tree_node(value)
                    break
                node = node.right

        self._size += 1

        return self

    def insert(self, existing_node, value_to_insert):
        node = self._root
        parent = None

        while True:
            if existing_node.value == node.value \
               and existing_node is node:
                node_to_insert = tree_node(value_to_insert)

                node_to_insert.left = node.left

                if node.right:
                    node_to_insert.right = node.right

                    node2 = node.right

                    while node2.left:
                        node2 = node2.left

                    node2.left = node
                else:
                    node_to_insert.right = node

                node.left = None
                node.right = None

                if not parent:
                    self._root = node_to_insert
                elif node is parent.left:
                    parent.left = node_to_insert
                else:
                    parent.right = node_to_insert

                self._size += 1

                return True
            elif existing_node.value < node.value:
                if not node.left:
                    return False

                parent = node
                node = node.left
            else:
                if not node.right:
                    return False

                parent = node
                node = node.right

    def erase(self, value):
        if not self._root:
            return False

        parent = None
        node = self._root

        while True:
            if value == node.value:
                if not node.left and not node.right:
                    if not parent:
                        self._root = None
                    elif node is parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                elif node.left and not node.right:
                    if not parent:
                        self._root = node.left
                    elif node is parent.left:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                elif node.right and not node.left:
                    if not parent:
                        self._root = node.right
                    elif node is parent.left:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                else:
                    node2 = node.left

                    if not node2.left and not node2.right \
                       or node2.left and not node2.right:
                        if node is self._root:
                            node2.right = node.right
                            self._root = node2
                        else:
                            if node is parent.left:
                                parent.left = node2
                                node2.right = node.right
                            else:
                                parent.right = node2
                                node2.right = node.right
                    else:
                        while True:
                            parent2 = node2
                            node2 = node2.right

                            if not node2.right:
                                break

                        parent2.right = node2.left if node2.left else None

                        if node is self._root:
                            node2.left = node.left
                            node2.right = node.right
                            self._root = node2
                        else:
                            if node is parent.left:
                                parent.left = node2
                            else:
                                parent.right = node2

                            node2.left = node.left
                            node2.right = node.right

                break
            elif value < node.value:
                if not node.left:
                    return False

                parent = node
                node = node.left
            else:
                if not node.right:
                    return False

                parent = node
                node = node.right

        self._size -= 1

        return True
