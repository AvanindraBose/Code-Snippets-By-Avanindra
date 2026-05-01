from typing import Optional,List

class ListNode:
    def __init__(self , x = 0 , next = None):
        self.data = x
        self.next = next

class Solution:
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
    
    def print_linked_list(self,head:Optional[ListNode]) -> None:
        curr = head

        while curr != None:
            print(curr.data)
            curr = curr.next
        
    
if __name__ == "__main__":
    head = None
    sol = Solution()
    head = sol.Insert_At_Head(head,4)
    head = sol.Insert_At_Head(head,5)
    head = sol.Insert_At_Head(head,2)
    head = sol.Insert_At_Head(head,7)
    head = sol.Insert_At_Head(head,1)

    vec = sol.get_linkedlist(head)
    print("Printing List After Inserting At head", vec)
    print("Printing elements of linked list",sol.print_linked_list(head))




