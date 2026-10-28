class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum = 0

        for operation in operations:
            match operation:
                case "+":
                    record.append(record[-1] + record[-2])
                    sum += record[-1]
                case "C":
                    val = record.pop()
                    sum -= val
                case "D":
                    record.append(record[-1] * 2)
                    sum += record[-1]
                case _:
                    record.append(int(operation))
                    sum += record[-1]

        return sum