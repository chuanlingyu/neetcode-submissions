class Solution:
    def calPoints(self, operations: List[str]) -> int:
        check = []
        output = 0
        for i in range(len(operations)):
            if operations[i] == 'C':
                num = check.pop(-1)
                output -= num
                continue
            elif operations[i] == '+':
                num = check[-1] + check[-2]
            elif operations[i] == 'D':
                num = 2 * check[-1]
            else:
                num = int(operations[i])  
            
            output += num
            check.append(num)

        return output