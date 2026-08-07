class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ops=[]
        
        for operation in operations:
            
            if operation=="C":
                ops.pop()
            
            elif operation=="D":
                ops.append(ops[-1]*2)
            
            elif operation=="+":
                ops.append(ops[-1]+ops[-2])
            
            else:
                ops.append(int(operation))
        return sum(ops)


