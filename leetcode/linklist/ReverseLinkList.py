class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next  # 保存当前节点的下一个节点
        current.next = prev      # 反转指针方向
        prev = current           # 移动 prev 到当前节点
        current = next_node      # 移动 current 到下一个节点

    return prev  # prev 现在是新的头节点


# 辅助函数：打印链表
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# 示例用法
if __name__ == "__main__":
    # 创建一个链表: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("原始链表:")
    print_linked_list(head)

    # 反转链表
    reversed_head = reverse_linked_list(head)

    print("反转后的链表:")
    print_linked_list(reversed_head)