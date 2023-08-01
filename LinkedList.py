class Node():
  def __init__(self, data):
    self.data = data
    self.next = None


class singlelinkedlist():
  def __init__(self):
    self.head = None

  def traversal(self):
    if self.head is None:
      print('SLL is empty')
    else:
      a = self.head
      while a is not None:
        print(a.data, end=' ')
        a = a.next

  def push_Beginning(self, data):
    print()
    nb = Node(data)
    nb.next = self.head
    self.head = nb

  def push_End(self, data):
    print()
    ne = Node(data)
    a = self.head
    while a.next is not None:
      a = a.next
    a.next = ne

  def insert_Inter(self, data, position):
    print()
    nii = Node(data)
    a = self.head
    for i in range(position - 1):
      a = a.next
    nii.next = a.next
    a.next = nii

  def pop_Beginning(self):
    print()
    a = self.head
    self.head = a.next
    a.next = None

  def pop_End(self):
    print()
    a = self.head.next
    b = self.head
    while a.next is not None:
      a = a.next
      b = b.next
    b.next = None

  def del_Inter(self, position):
    print()
    a = self.head.next
    b = self.head
    for i in range(position - 2):
      a = a.next
      b = b.next
    b.next = a.next
    a.next = None

  def get_mid(self):
    print()
    length = 0
    a = self.head

    while a:
      a = a.next
      length += 1

    count = length // 2
    p = self.head

    while count > 0:
      a = a.next
      count = -1
    return p.data