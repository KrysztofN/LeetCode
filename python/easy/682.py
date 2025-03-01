class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for op in operations:
            if (op.lstrip("-")).isdigit():
                ans.append(int(op))
            elif op == "+":
                ans.append(ans[-1] + ans[-2])
            elif op == "D":
                ans.append(ans[-1] * 2)
            elif op == "C":
                ans.pop()
        return sum(ans)