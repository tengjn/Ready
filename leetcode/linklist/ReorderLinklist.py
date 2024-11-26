# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 处理特殊情况：空链表、单节点链表或双节点链表，无需重排
        if not head or not head.next or not head.next.next:
            return
            
        # 步骤1：使用快慢指针找到链表的中点位置
        # slow会指向中点位置，fast用于控制slow的移动
        # 例如：1->2->3->4中，slow最终指向2
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next          # 慢指针每次移动一步
            fast = fast.next.next     # 快指针每次移动两步
            
        # 步骤2：将链表从中点断开，并反转后半部分
        # 保存后半部分的起始节点
        # 例如：对于1->2->3->4，second指向3
        second = slow.next
        # 断开前后两个链表，前半部分的末尾指向null
        slow.next = None
        
        # 反转后半部分链表
        # prev用于构建反向连接，curr是当前处理的节点
        prev = None
        curr = second
        # 通过不断改变next指针方向来反转链表
        while curr:
            # 保存下一个要处理的节点
            next_temp = curr.next
            # 反转当前节点的指针
            curr.next = prev
            # 移动prev和curr指针
            prev = curr
            curr = next_temp
        # prev现在是反转后的后半部分的头节点    
        second = prev
        
        # 步骤3：合并两个链表
        # first指向前半部分，second指向反转后的后半部分
        first = head
        # 交替连接两个链表的节点
        while first and second:
            # 保存两个链表中下一个要处理的节点
            first_next = first.next
            second_next = second.next
            
            # 将second节点插入到first之后
            first.next = second
            second.next = first_next
            
            # 移动指针到下一对要处理的节点
            first = first_next
            second = second_next
