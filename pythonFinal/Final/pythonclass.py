class Vinyl: #Class Artifact
    def __init__(self, album, artist, year):
        self.__album = album
        self.__artist = artist
        self.__year = year

    def display(self):
        print (self.__album + ' - ' + self.__artist + ' - ' + str(self.__year))

def run01():
    ink_warantorn = Vinyl('INK', 'Waruntorn Paonil', 2022)
    ink_warantorn.display()

    born_this_way = ("Born This Way", "Lady Gaga", 2011)
    lemonade = ("Lemonade", "Beyonce", 2016)
    my_everything = ("My Everything", "Ariana Grande", 2014)
    artifacts = LinkedList()
    artifacts.append(Node(born_this_way))
    artifacts.append(Node(lemonade))
    artifacts.append(Node(my_everything))
    print(artifacts.list())

###########

from queue import Queue, LifoQueue

class Account:
    def __init__(self, account_name, opening_balance):
        self.account_name = account_name
        self.balance = opening_balance

def run02():
    bank_account01 = Account('Mr.A',20000)
    bank_account02 = Account('Mr.B',15000)
    bank_account03 = Account('Mr.C',10000)

    my_size = 3
    q = Queue(maxsize=my_size)

    q.put(bank_account01)
    q.put(bank_account02)
    q.put(bank_account03)

    #print(q.get().account_name) #Run to  Mr.A (queue)

    stack = LifoQueue(maxsize=my_size)
    stack.put(bank_account01)
    stack.put(bank_account02)
    stack.put(bank_account03)

    #print(stack.get().account_name) #Run to Mr.C (stack)

##########

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first_node = None
        self.size = 0

    def append(self, node):
        if self.first_node is None:
            self.first_node = node
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                current_node = current_node.next

            current_node.next = node
        self.size += 1

    def list(self):
        result = ''
        if self.first_node is None:
            result = 'Empty Linked List'
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                result = result + str(current_node.value) + ', '
                current_node = current_node.next
            result = result + str(current_node.value)
        return result

def run03():
    node3 = Node(3)
    node9 = Node(9)
    node7 = Node(7)
    node1 = Node(1)
    node14 = Node(14)
    node2 = Node(2)
    node5 = Node('Five')
    bank_account01 = Account('Mr.A', 20000)
    node_bank01 = Node(bank_account01)

    my_linked_list = LinkedList()
    #print(my_linked_list.list()) #Run to  Empty Linked List

    my_linked_list.append(node3)
    my_linked_list.append(node9)
    my_linked_list.append(node7)
    my_linked_list.append(node1)
    my_linked_list.append(node14)
    my_linked_list.append(node2)
    my_linked_list.append(node5)
    my_linked_list.append(node_bank01)

    print(my_linked_list.list())

    print(my_linked_list.size)
