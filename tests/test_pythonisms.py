from pythonisms import __version__
from pythonisms.iterator_generator import LinkedList,Node
import pytest


def test_version():
    assert __version__ == '0.1.0'


# Can successfully iterate over the linkedlist
def test_iter(ll_test):
  ll_test.append(1)
  result = []
  for i in ll_test:
    result.append(i)
  assert result == [7,5,1] 

# Can successfully check for not equality in nodes
def test_node_eq():
  node1=Node(1)
  node2=Node(2)
  assert (node1==node2) == False

# Can successfully check for equality in nodes
def test_node_not_eq():
  node1=Node(1)
  node2=Node(1)
  assert (node1==node2) == True

# Can successfully check two linkedlists are equal
def test_equal(ll_test , ll_test2):
  assert (ll_test == ll_test2) == True
  
  
# Can successfully check two linkedlists are not equal
def test_not_equal (ll_test,ll_test3):
  assert (ll_test == ll_test3) == False

# can successfully check for getitem which depends on iterating.
def test_get_Item(ll_test):
  actual = ll_test[1]
  expected = 5
  assert actual == expected
  
def list_comprehension():
    ll = LinkedList()
    ll.append(7)
    ll.append(5)
    ll.append(9)
    ll.append(10)
    lst = [i for i in ll ]
    assert lst == [7, 5, 9, 10]

@pytest.fixture
def ll_test():
  ll=LinkedList()
  ll.append(7)
  ll.append(5)
  return ll

@pytest.fixture
def ll_test2():
  ll = LinkedList()
  ll.append(7)
  ll.append(5)
  return ll

@pytest.fixture
def ll_test3():
  ll = LinkedList()
  ll.append(20)
  ll.append(21)
  return ll

@pytest.fixture
def test_is_greater():
    linked_list= LinkedList()
    linked_list2= LinkedList()
    linked_list.append(6)
    linked_list.append(7)
    linked_list2.append(7)
    linked_list2.append(6)
    sum0 = 0 
    sum1 = 0
    for i in linked_list:
        sum0 += i
    for j in linked_list2:
        sum1 += j
    expected = False
    actual = sum0 < sum1
    assert expected == actual
    
def test_is_greater_length():
    linked_list= LinkedList()
    linked_list2= LinkedList()
    linked_list.append(6)
    linked_list.append(7)
    linked_list2.append(7)
    linked_list2.append(6)
    expected = False
    actual = len(linked_list)<len(linked_list2)
    assert expected == actual