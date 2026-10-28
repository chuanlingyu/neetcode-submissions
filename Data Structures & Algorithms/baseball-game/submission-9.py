class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for operation in operations:
            match operation:
                case "+":
                    record.append(record[-1] + record[-2])
                case "C":
                    val = record.pop()
                case "D":
                    record.append(record[-1] * 2)
                case _:
                    record.append(int(operation))

        return sum(record)