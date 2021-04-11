# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2021/04/11 18:45:38
# @modified 2021/04/11 21:46:51
# @filename avltree.py

"""二叉平衡树

只有4种情况是不平衡的

把需要重新平衡的结点叫做α，由于任意两个结点最多只有两个儿子，因此高度不平衡时，α结点的两颗子树的高度相差2.容易看出，这种不平衡可能出现在下面4中情况中：
来源: https://www.cnblogs.com/zhangbaochong/p/5164994.html


1. 对α的左儿子的左子树进行一次插入（左左，单旋转解决）

                6               3
              /   \           /   \
             3     7         1     6
            / \         =>    \   / \
           1   4               2 4   7
            \
             2

2.对α的左儿子的右子树进行一次插入（左右，双旋转解决，也就是先转成左左，然后单旋转）

                6                6                     4
              /   \            /   \                 /   \
             2     7          4     7               2     6
            / \         =>   /              =>     / \     \
           1   4            2                     1   3     7
              /            / \
             3            1   3

3.对α的右儿子的左子树进行一次插入（右左，双旋转解决，也就是先转成左左，然后单旋转）

                2                   2                   3
              /   \               /   \               /   \
             1     5             1     3             2     5
                  / \       =>          \     =>    /     / \
                 3   6                   5         1     4   6
                  \                     / \
                   4                   4   6
3.1 Root(1) = A; A.right = ARL; ARL.right = AR; AR.left = ARL.right
3.2 Root(2) = AR(1) = ARL;   => Root = ARL
    AR(1).left = A(1) = A;   => ARL.left = A
    A(1).right = AR(1).left; => A.right  = ARL.left
    
合并之后: Root = ARL; A.right = ARL.left; AR.left = ARL.right; ARL.left = A; ARL.right = AR;

4.对α的右儿子的右子树进行一次插入（右右，单旋转解决）


                2                     4
              /   \                /    \
             1     4              2      6
                  / \       =>   / \    /
                 3   6          1   3  5
                    /
                   5

Root = AR; AR.left = A; A.right = AR.left
"""

import random, math
import sys


PY2 = sys.version_info[0] == 2

DEBUG_FLAG = True
DEBUG_MSG  = []

if not PY2:
    xrange = range

def random_data_generator (max_r):
    for i in xrange(max_r):
        yield random.randint(0, max_r)


class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.height = 0 
    
    def __str__(self):
        return str(self.key) + "(" + str(self.height) + ")"
    
    def is_leaf(self):
        return (self.height == 0)
   
    def max_children_height(self):
        if self.leftChild and self.rightChild:
            return max(self.leftChild.height, self.rightChild.height)
        elif self.leftChild and not self.rightChild:
            return self.leftChild.height
        elif not self.leftChild and  self.rightChild:
            return self.rightChild.height
        else:
            return -1
        
    def balance (self):
        # TODO 这个数据可以缓存起来加速
        left_height = -1
        right_height = -1

        if self.leftChild:
            left_height = self.leftChild.height

        if self.rightChild:
            right_height = self.rightChild.height

        return left_height - right_height

    def set_left_child(self, node):
        self.leftChild = node

        if node != None:
            node.parent = self

    def set_right_child(self, node):
        self.rightChild = node

        if node != None:
            node.parent = self


    def print_node(self):
        if self.leftChild is None and self.rightChild is None:
            print(self.key, end="")
            return

        print(self.key, end = "")

        print("(", end = "")

        if self.leftChild:
            self.leftChild.print_node()
        else:
            print("None", end="")

        print(",", end="")

        if self.rightChild:
            self.rightChild.print_node()
        else:
            print("None", end="")

        print(")", end = "")


def debug_print(msg):
    global DEBUG_MSG
    if DEBUG_FLAG:
        print(msg)
        DEBUG_MSG.append(msg)

def debug_clear():
    global DEBUG_MSG
    DEBUG_MSG = []


class AVLTree():
    def __init__(self, *args):
        self.rootNode = None
        self.elements_count = 0
        self.rebalance_count = 0
        if len(args) == 1:
            for i in args[0]:
                self.insert (i)
        
    def height(self):
        if self.rootNode:
            return self.rootNode.height
        else:
            return 0
        
    def rebalance (self, node_to_rebalance):
        self.rebalance_count += 1
        A = node_to_rebalance 
        F = A.parent #allowed to be NULL
        if node_to_rebalance.balance() == -2:
            # 右篇2层（情况3和情况4）
            right_balance = node_to_rebalance.rightChild.balance()

            if right_balance <= 0:
                # 右子树偏右（情况4）
                """Rebalance, case RRC """
                debug_print("rebalance: case 4")
                AR = A.rightChild
                ARR = AR.rightChild

                assert A is not None
                assert AR is not None
                assert ARR is not None

                A.set_right_child(AR.leftChild)
                AR.set_left_child(A)
                                                          
                if F is None:
                    # A是根节点
                    self.rootNode = AR
                    self.rootNode.parent = None                                                   
                else:
                    if F.rightChild == A:
                        F.set_right_child(AR)                                                                
                    else:                                                                      
                        F.set_left_child(AR)

                self.recompute_heights (A) 
                self.recompute_heights (AR.parent)

            else:
                # 右子树偏左（情况3，双旋转）
                # 合并之后: Root = ARL; A.right = ARL.left; AR.left = ARL.right; ARL.left = A; ARL.right = AR;

                debug_print("rebalance: case 3")
                B = AR = A.rightChild
                C = ARL = AR.leftChild

                assert A is not None
                assert AR is not None
                assert ARL is not None

                A.set_right_child(ARL.leftChild)
                AR.set_left_child(ARL.rightChild)
                ARL.set_left_child(A)
                ARL.set_right_child(AR)

                if F is None:                                                             
                    self.rootNode = C
                    self.rootNode.parent = None                                                    
                else:                                                                        
                    if F.rightChild == A:                                                         
                        F.set_right_child(C)                                                                               
                    else:                                                                      
                        F.set_left_child(C)

                self.recompute_heights (A)
                self.recompute_heights (AR)

        else:
            # 左子树比右子树高（情况1和情况2）
            assert(node_to_rebalance.balance() == +2)
            if node_to_rebalance.leftChild.balance() >= 0:
                # 左子树偏左（情况1）
                debug_print("rebalance: case 1")

                B = AL = A.leftChild
                C = ALL = B.leftChild
                """Rebalance, case LLC """

                assert A is not None
                assert AL is not None
                assert ALL is not None

                A.leftChild = B.rightChild
                if (A.leftChild): 
                    A.leftChild.parent = A
                    
                B.rightChild = A
                A.parent = B
                if F is None:
                    self.rootNode = B
                    self.rootNode.parent = None                    
                else:
                    if F.rightChild == A:
                        F.rightChild = B
                    else:
                        F.leftChild = B
                    B.parent = F
                self.recompute_heights (A)
                self.recompute_heights (B.parent) 
            else:
                # 左子树偏右（情况2）
                debug_print("rebalance: case 2")
                B = A.leftChild
                C = B.rightChild 
                """Rebalance, case LRC """
                assert (not A is None and not B is None and not C is None)
                A.leftChild = C.rightChild
                if A.leftChild:
                    A.leftChild.parent = A
                B.rightChild = C.leftChild
                if B.rightChild:
                    B.rightChild.parent = B
                C.leftChild = B
                B.parent = C
                C.rightChild = A
                A.parent = C
                if F is None:
                   self.rootNode = C
                   self.rootNode.parent = None
                else:
                   if (F.rightChild == A):
                       F.rightChild = C
                   else:
                       F.leftChild = C
                   C.parent = F
                self.recompute_heights (A)
                self.recompute_heights (B)
                
    def sanity_check (self, *args):
        if len(args) == 0:
            node = self.rootNode
        else:
            node = args[0]
        if (node  is None) or (node.is_leaf() and node.parent is None ):
            # trival - no sanity check needed, as either the tree is empty or there is only one node in the tree     
            pass    
        else:
            if node.height != node.max_children_height() + 1:
                raise Exception ("Invalid height for node " + str(node) + ": " + str(node.height) + " instead of " + str(node.max_children_height() + 1) + "!" )
                
            balFactor = node.balance()
            #Test the balance factor
            if not (balFactor >= -1 and balFactor <= 1):
                raise Exception ("Balance factor for node " + str(node) + " is " + str(balFactor) + "!")
            #Make sure we have no circular references
            if not (node.leftChild != node):
                raise Exception ("Circular reference for node " + str(node) + ": node.leftChild is node!")
            if not (node.rightChild != node):
                raise Exception ("Circular reference for node " + str(node) + ": node.rightChild is node!")
            
            if ( node.leftChild ): 
                if not (node.leftChild.parent == node):
                    raise Exception ("Left child of node " + str(node) + " doesn't know who his father is!")
                if not (node.leftChild.key <=  node.key):
                    raise Exception ("Key of left child of node " + str(node) + " is greater than key of his parent!")
                self.sanity_check(node.leftChild)
            
            if ( node.rightChild ): 
                if not (node.rightChild.parent == node):
                    raise Exception ("Right child of node " + str(node) + " doesn't know who his father is!")
                if not (node.rightChild.key >=  node.key):
                    raise Exception ("Key of right child of node " + str(node) + " is less than key of his parent!")
                self.sanity_check(node.rightChild)
            
    def recompute_heights (self, start_from_node):
        changed = True
        node = start_from_node
        while node and changed:
            old_height = node.height
            node.height = (node.max_children_height() + 1 if (node.rightChild or node.leftChild) else 0)
            changed = node.height != old_height
            node = node.parent
       
    def do_insert (self, parent_node, child_node):
        node_to_rebalance = None
        if child_node.key < parent_node.key:
            if not parent_node.leftChild:
                # 左子树为空
                parent_node.set_left_child(child_node)
                if parent_node.height == 0:
                    node = parent_node
                    while node:
                        node.height = node.max_children_height() + 1
                        if not node.balance () in [-1, 0, 1]:
                            node_to_rebalance = node
                            break #we need the one that is furthest from the root
                        node = node.parent
                else:
                    # 高度不为0，并且左子树为空，说明插入前肯定有右子树，插入左子树后依然是平衡的，不需要进行调整
                    pass
            else:
                self.do_insert(parent_node.leftChild, child_node)
        else:
            if not parent_node.rightChild:
                # 右子树为空
                parent_node.set_right_child(child_node)

                if parent_node.height == 0:
                    node = parent_node
                    while node:
                        node.height = node.max_children_height() + 1
                        if not node.balance () in [-1, 0, 1]:
                            node_to_rebalance = node
                            break #we need the one that is furthest from the root
                        node = node.parent       
            else:
                self.do_insert(parent_node.rightChild, child_node)
        
        if node_to_rebalance:
            self.rebalance (node_to_rebalance)
    
    def insert (self, key):
        # 1、插入节点
        # 2、判断是否平衡，如果不平衡进行调整
        new_node = Node (key)
        if not self.rootNode:
            self.rootNode = new_node
        else:
            if not self.find(key):
                self.elements_count += 1
                self.do_insert (self.rootNode, new_node)
      
    def find_biggest(self, start_node):
        node = start_node
        while node.rightChild:
            node = node.rightChild
        return node 
    
    def find_smallest(self, start_node):
        node = start_node
        while node.leftChild:
            node = node.leftChild
        return node
     
    def inorder_non_recursive (self):
        node = self.rootNode
        retlst = []
        while node.leftChild:
            node = node.leftChild
        while (node):
            retlst += [node.key]
            if (node.rightChild):
                node = node.rightChild
                while node.leftChild:
                    node = node.leftChild
            else:
                while ((node.parent)  and (node == node.parent.rightChild)):
                    node = node.parent
                node = node.parent
        return retlst
 
    def preorder(self, node, retlst = None):
        if retlst is None:
            retlst = []
        retlst += [node.key]
        if node.leftChild:
            retlst = self.preorder(node.leftChild, retlst) 
        if node.rightChild:
            retlst = self.preorder(node.rightChild, retlst)
        return retlst         
           
    def inorder(self, node, retlst = None):
        if retlst is None:
            retlst = [] 
        if node.leftChild:
            retlst = self.inorder(node.leftChild, retlst)
        retlst += [node.key] 
        if node.rightChild:
            retlst = self.inorder(node.rightChild, retlst)
        return retlst
        
    def postorder(self, node, retlst = None):
        if retlst is None:
            retlst = []
        if node.leftChild:
            retlst = self.postorder(node.leftChild, retlst) 
        if node.rightChild:
            retlst = self.postorder(node.rightChild, retlst)
        retlst += [node.key]
        return retlst  
    
    def as_list (self, pre_in_post):
        if not self.rootNode:
            return []
        if pre_in_post == 0:
            return self.preorder (self.rootNode)
        elif pre_in_post == 1:
            return self.inorder (self.rootNode)
        elif pre_in_post == 2:
            return self.postorder (self.rootNode)
        elif pre_in_post == 3:
            return self.inorder_non_recursive()      
          
    def find(self, key):
        return self.find_in_subtree (self.rootNode, key )
    
    def find_in_subtree (self,  node, key):
        if node is None:
            return None  # key not found
        if key < node.key:
            return self.find_in_subtree(node.leftChild, key)
        elif key > node.key:
            return self.find_in_subtree(node.rightChild, key)
        else:  # key is equal to node key
            return node
    
    def remove (self, key):
        # first find
        node = self.find(key)
        
        if not node is None:
            self.elements_count -= 1
            
            #     There are three cases:
            # 
            #     1) The node is a leaf.  Remove it and return.
            # 
            #     2) The node is a branch (has only 1 child). Make the pointer to this node 
            #        point to the child of this node.
            # 
            #     3) The node has two children. Swap items with the successor
            #        of the node (the smallest item in its right subtree) and
            #        delete the successor from the right subtree of the node.
            if node.is_leaf():
                self.remove_leaf(node)
            elif (bool(node.leftChild)) ^ (bool(node.rightChild)):  
                self.remove_branch (node)
            else:
                assert (node.leftChild) and (node.rightChild)
                self.swap_with_successor_and_remove (node)
            
    def remove_leaf (self, node):
        parent = node.parent
        if (parent):
            if parent.leftChild == node:
                parent.leftChild = None
            else:
                assert (parent.rightChild == node)
                parent.rightChild = None
            self.recompute_heights(parent)
        else:
            self.rootNode = None
        del node
        # rebalance
        node = parent
        while (node):
            if not node.balance() in [-1, 0, 1]:
                self.rebalance(node)
            node = node.parent
        
        
    def remove_branch (self, node):
        parent = node.parent
        if (parent):
            if parent.leftChild == node:
                parent.leftChild = node.rightChild or node.leftChild
            else:
                assert (parent.rightChild == node)
                parent.rightChild = node.rightChild or node.leftChild
            if node.leftChild:
                node.leftChild.parent = parent
            else:
                assert (node.rightChild)
                node.rightChild.parent = parent 
            self.recompute_heights(parent)
        del node
        # rebalance
        node = parent
        while (node):
            if not node.balance() in [-1, 0, 1]:
                self.rebalance(node)
            node = node.parent
        
    def swap_with_successor_and_remove (self, node):
        successor = self.find_smallest(node.rightChild)
        self.swap_nodes (node, successor)
        assert (node.leftChild is None)
        if node.height == 0:
            self.remove_leaf (node)
        else:
            self.remove_branch (node)
            
    def swap_nodes (self, node1, node2):
        assert (node1.height > node2.height)
        parent1 = node1.parent
        leftChild1 = node1.leftChild
        rightChild1 = node1.rightChild
        parent2 = node2.parent
        assert (not parent2 is None)
        assert (parent2.leftChild == node2 or parent2 == node1)
        leftChild2 = node2.leftChild
        assert (leftChild2 is None)
        rightChild2 = node2.rightChild
        
        # swap heights
        tmp = node1.height 
        node1.height = node2.height
        node2.height = tmp
       
        if parent1:
            if parent1.leftChild == node1:
                parent1.leftChild = node2
            else:
                assert (parent1.rightChild == node1)
                parent1.rightChild = node2
            node2.parent = parent1
        else:
            self.rootNode = node2
            node2.parent = None
            
        node2.leftChild = leftChild1
        leftChild1.parent = node2
        node1.leftChild = leftChild2 # None
        node1.rightChild = rightChild2
        if rightChild2:
            rightChild2.parent = node1 
        if not (parent2 == node1):
            node2.rightChild = rightChild1
            rightChild1.parent = node2
            
            parent2.leftChild = node1
            node1.parent = parent2
        else:
            node2.rightChild = node1
            node1.parent = node2           
           
    # use for debug only and only with small trees            
    def out(self, start_node = None):
        if start_node == None:
            start_node = self.rootNode
        space_symbol = "*"
        spaces_count = 80
        out_string = ""
        initial_spaces_string  = space_symbol * spaces_count + "\n" 
        if not start_node:
            return "AVLTree is empty"
        else:
            level = [start_node]
            while (len([i for i in level if (not i is None)])>0):
                level_string = initial_spaces_string
                for i in xrange(len(level)):
                    j = (i+1)* spaces_count / (len(level)+1)
                    level_string = level_string[:j] + (str(level[i]) if level[i] else space_symbol) + level_string[j+1:]
                level_next = []
                for i in level:
                    level_next += ([i.leftChild, i.rightChild] if i else [None, None])
                level = level_next
                out_string += level_string                    
        return out_string

    def print_tree(self):
        if self.rootNode is None:
            print("None")
        else:
            self.rootNode.print_node()
            print("")


def main():
    """check empty tree creation"""
    global DEBUG_FLAG
    DEBUG_FLAG = False

    a = AVLTree ()
    a.sanity_check()
    
    """check not empty tree creation"""
    seq = [1,2,3,4,5,6,7,8,9,10,11,12]
    seq_copy = [1,2,3,4,5,6,7,8,9,10,11,12]
    #random.shuffle(seq)
    b = AVLTree (seq)
    b.sanity_check()
    
    """check that inorder traversal on an AVL tree 
    (and on a binary search tree in the whole) 
    will return values from the underlying set in order"""
    assert (b.as_list(3) == b.as_list(1) == seq_copy)
    
    """check that node deletion works"""
    c = AVLTree (random_data_generator (10000))
    before_deletion = c.elements_count
    for i in random_data_generator (1000):
        c.remove(i)
    after_deletion = c.elements_count

    c.sanity_check()
    assert (before_deletion >= after_deletion)
    
    # c.print_tree()
    
    """check that an AVL tree's height is strictly less than 
    1.44*log2(N+2)-1 (there N is number of elements)"""
    assert (c.height() < 1.44 * math.log(after_deletion+2, 2) - 1)

def test_rebalance_4():
    print("\ntest_rebalance_4")
    tree = AVLTree()

    for new_value in (1,2,3):
        tree.insert(new_value)
        tree.print_tree()

def test_rebalance_3():
    debug_clear()
    print("\ntest_rebalance_3")
    tree = AVLTree()

    for new_value in (1,5,2):
        tree.insert(new_value)
        tree.print_tree()

    assert DEBUG_MSG[0] == "rebalance: case 3"



def test_rebalance_2():
    debug_clear()
    print("\ntest_rebalance_2")
    tree = AVLTree()

    for new_value in (5,1,2):
        tree.insert(new_value)
        tree.print_tree()

    assert DEBUG_MSG[0] == "rebalance: case 2"

def test_rebalance_1():
    debug_clear()
    print("\ntest_rebalance_1")
    tree = AVLTree()

    for new_value in (5,2,1):
        tree.insert(new_value)
        tree.print_tree()
   
def test_main():
    test_rebalance_1() 
    test_rebalance_2() 
    test_rebalance_3()
    test_rebalance_4()


if __name__ == "__main__":  
    test_main()
    main()



