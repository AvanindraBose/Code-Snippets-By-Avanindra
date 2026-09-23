# T.C for Updating Segment Tree -> O(logn) , for q queries It would be O(q*logn)
#  S.C -> O(2*n) + O(logn)

class SegmentTree:
    def __init__(self,n):
        self.seg_tree = [0]*(2*n)

    def build_tree(self,nums,idx,l,r):
        # recrusion to build the segment tree
        #  base case 

        if l == r :
            self.seg_tree[idx] = nums[r]
            return

        mid = (l+r)//2

        # fill left subtree
        self.build_tree(nums,2*idx+1,l,mid)

        # fill right subtree
        self.build_tree(nums,2*idx+2,mid+1,r)

        self.seg_tree[idx] = self.seg_tree[2*idx+1] + self.seg_tree[2*idx+2]

        return

    def update_tree(self,idx,val,i,l,r):
        #  idx = position in nums where I want to update
        # i = index of Seg Tree Array

        #  base case
        if l == r :
            # I have reached that index in segtree
            self.seg_tree[i] = val
            return

        mid = (l+r)//2

        if idx <= mid :
            # go to left subtree
            self.update_tree(idx,val,2*i+1,l,mid)
        else :
            self.update_tree(idx,val,2*i+2,mid+1,r)

        self.seg_tree[i] = self.seg_tree[2*i + 1] + self.seg_tree[2*i + 2]

        return

    def get_tree_array(self):
        return self.seg_tree


if __name__ == "__main__":

    nums = [3,5,1,2,7]

    n = len(nums)
    
    segment_tree = SegmentTree(n)

    segment_tree.build_tree(nums,0,0,n-1)

    tree_arr_before = segment_tree.get_tree_array()

    print("Segment Tree Array Before Updating : ",tree_arr_before)

    new_val = 12

    idx = 2 

    #  update at idx 2 with value 12
    nums[idx] = new_val

    segment_tree.update_tree(idx,new_val,0,0,n-1)

    tree_arr_after = segment_tree.get_tree_array()

    print("Segment Tree Array After Updating : ",tree_arr_after)

    
