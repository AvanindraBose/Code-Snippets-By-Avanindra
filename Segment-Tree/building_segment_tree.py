# this segment tree building is only for range-sum. this will give an idea on the implementation of segment tree.

# TC -> O(n)
# Sc -> O(2*n) + O(log(n))

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

    def get_tree_array(self):
        return self.seg_tree


if __name__ == "__main__":

    nums = [3,2,1,4,5]

    n = len(nums)

    segment_tree = SegmentTree(n)

    segment_tree.build_tree(nums,0,0,n-1)

    tree_arr = segment_tree.get_tree_array()

    print(tree_arr)






