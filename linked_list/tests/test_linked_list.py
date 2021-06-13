from linked_list import __version__
from linked_list.linked_list import Node , Linked_List
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_instance():
    ll = Linked_List()
    assert isinstance(ll, Linked_List) 

def test_LinkedList_include():
    test_LinkedList = Linked_List()
    test_LinkedList.insert(0)
    test_LinkedList.insert(1)
    assert test_LinkedList.include(1) == True
    assert test_LinkedList.include(88) == False   

def test_append_1():
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    assert ll.head.value == 1
    assert ll.head.next.value==2


def test__str__():
    test_LinkedList = Linked_List()
    test_LinkedList.insert('H')
    test_LinkedList.insert('A')
    test_LinkedList.insert('Z')
    test_LinkedList.insert('M')
    test_LinkedList.insert('A')
    test_LinkedList.insert('H')
    assert test_LinkedList.__str__() == "H -> A -> M -> Z -> A -> H -> Null"


def test_insert_before(llFixture):
    llFixture.insertBefore(2,10)
    assert llFixture.__str__() == '7 -> 3 -> 10 -> 2 -> 5 -> Null'



def test_insert_after(llFixture):
    llFixture.insertAfter(3,12)     
    assert llFixture.__str__() == "7 -> 3 -> 12 -> 2 -> 5 -> Null"



@pytest.fixture
def llFixture():
    linked_list_o=Linked_List()
    linked_list_o.insert(5) 
    linked_list_o.insert(2)
    linked_list_o.insert(3)
    linked_list_o.insert(7)
    return linked_list_o

