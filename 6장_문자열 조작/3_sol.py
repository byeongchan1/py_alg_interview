# https://leetcode.com/problems/reorder-data-in-log-files/

# 로그파일 재정렬


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        # 람다식으로 정렬 (정렬 우선순위 지정 가능)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # letter경우 뒤의것으로 sort하고, 같을경우 identifiers로 판단
        
        return letters + digits # list에서 '+'는 뒤에 붙이기 역할