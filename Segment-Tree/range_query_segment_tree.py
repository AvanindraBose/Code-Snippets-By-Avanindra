# In this I will learn to apply range query in segment tree
# For Example Find out the sum of elements from index 2,4.
# T.C -> O(log(n))
# S.C -> O(2*n) + O(logn)
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

    def query(self,start,end,i,l,r):
        #  3 cases possible here

        ans = 0

        mid = (l+r)//2

        if r < start or l > end :
            #  out of bound
            return 0
        elif l >= start and r <= end :
            return self.seg_tree[i]
        else :
            # partial boundary
            #  visit left side
            ans += self.query(start,end,2*i+1,l,mid)

            #  visit right side
            ans += self.query(start,end,2*i+2,mid+1,r)

        return ans


    def get_tree_array(self):
        return self.seg_tree


if __name__ == "__main__":

    nums = [3,1,7,5,6]
    
    n = len(nums)

    segment_tree = SegmentTree(n)

    segment_tree.build_tree(nums,0,0,n-1)

    tree_arr = segment_tree.get_tree_array()

    print(nums)

    ans = segment_tree.query(2,4,0,0,n-1)

    print(ans)

    

    