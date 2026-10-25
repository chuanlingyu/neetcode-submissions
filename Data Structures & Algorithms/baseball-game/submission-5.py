class Solution:
    def calPoints(self, operations: List[str]) -> int:
        check = []
        sum = 0

        for i in range(len(operations)):
            element = operations[i]
            
            if element == "+":
                val = check[-1] + check[-2]
                check.append(val)
                sum += val
            elif element == "C":
                val = check[-1]
                check.pop()
                sum -= val
            elif element == 'D':
                val = 2 * check[-1]
                check.append(val)
                sum += val
            else:
                val = int(element)
                check.append(val)
                sum += val

        return sum