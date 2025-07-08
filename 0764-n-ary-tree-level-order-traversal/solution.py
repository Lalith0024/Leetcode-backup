class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        q = [root]
        ans = []

        while q:
            temp = []
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                temp.append(node.val)
                if node.children:
                    q.extend(node.children)
            ans.append(temp)
        return ans


#always write a clean code no need to append and all and use variables because its readabale 
#try to analyze dont panic if there is no left or right there is a children array juz extened instead of append 
#the template would be same but the intution of the problem should be differenet juz slight modifications will lead to more change in the problem more effective readable is the code that better are chances at interview 
