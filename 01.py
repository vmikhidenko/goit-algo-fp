# Визначення класу вузла однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Функція для вставки вузла на початок списку
def push(head_ref, new_data):
    node = Node(new_data)
    node.next = head_ref
    return node

# Функція для виведення списку
def printList(node):
    while node is not None:
        print(f"{node.data} -> ", end='')
        node = node.next
    print("NULL")

# 1. Функція реверсування однозв'язного списку
def reverseList(head_ref):
    prev = None
    current = head_ref
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# 2. Сортування вставками для однозв'язного списку
def sortedInsert(head_ref, new_node):
    if head_ref is None or head_ref.data >= new_node.data:
        new_node.next = head_ref
        return new_node
    else:
        current = head_ref
        while current.next is not None and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head_ref

def insertionSort(head_ref):
    sorted = None
    current = head_ref
    while current is not None:
        next = current.next
        sorted = sortedInsert(sorted, current)
        current = next
    return sorted

# 3. Функція об'єднання двох відсортованих однозв'язних списків
def mergeLists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1 is not None:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next

# Приклад використання функцій
if __name__ == "__main__":
    list1 = None
    list2 = None

    # Заповнюємо перший список
    list1 = push(list1, 5)
    list1 = push(list1, 3)
    list1 = push(list1, 1)

    # Заповнюємо другий список
    list2 = push(list2, 6)
    list2 = push(list2, 4)
    list2 = push(list2, 2)

    # Сортуємо списки (хоча вони вже відсортовані при вставці)
    list1 = insertionSort(list1)
    list2 = insertionSort(list2)

    print("Перший список: ", end='')
    printList(list1)

    print("Другий список: ", end='')
    printList(list2)

    # Об'єднуємо списки
    mergedList = mergeLists(list1, list2)
    print("Об'єднаний відсортований список: ", end='')
    printList(mergedList)

    # Реверсуємо об'єднаний список
    mergedList = reverseList(mergedList)
    print("Реверсований об'єднаний список: ", end='')
    printList(mergedList)
