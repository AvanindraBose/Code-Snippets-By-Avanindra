from typing import Optional,List

class ListNode:
    def __init__(self,x=0,next=None):
        self.data = x
        self.next = next

class Solution:

    def delete_from_head(self,head : Optional[ListNode]) -> Optional[ListNode]:
        return head.next
    
    def Insert_At_Head(self,head: Optional[ListNode] ,new_ele : int) -> Optional[ListNode]:
        new_node = ListNode(new_ele)
        new_node.next = head
        head = new_node
        return head
    
    def get_linkedlist(self,head:Optional[ListNode]) -> List[int]:
        curr = head
        ans = []
        while curr != None :
            ans.append(curr.data)
            curr = curr.next
        return ans

if __name__ == "__main__":
    head = None
    sol = Solution()
    head = sol.Insert_At_Head(head,6)
    head = sol.Insert_At_Head(head,3)
    head = sol.Insert_At_Head(head,9)
    head = sol.Insert_At_Head(head,5)

    vec_before = sol.get_linkedlist(head)
    print("Linked List Before Deletion",vec_before)

    head = sol.delete_from_head(head)
    vec_after = sol.get_linkedlist(head)
    print("Linked List After Deletion",vec_after)

