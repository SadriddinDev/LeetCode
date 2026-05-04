
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        # If the string is too long for an IP (max 3 digits * 4 segments)
        if len(s) > 12:
            return res

        def backtrack(start_idx, dots, current_ip):
            # Base Case: If we have 4 segments and reached the end of the string
            if dots == 4:
                if start_idx == len(s):
                    res.append(current_ip[:-1]) # Remove the trailing dot
                return

            # Explore 1, 2, or 3 digits for the current segment
            for length in range(1, 4):
                if start_idx + length > len(s):
                    break
                
                segment = s[start_idx : start_idx + length]
                
                # Check constraints:
                # 1. No leading zeros (unless the segment is just "0")
                # 2. Value must be <= 255
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue
                
                backtrack(start_idx + length, dots + 1, current_ip + segment + ".")

        backtrack(0, 0, "")
        return res

print(Solution().restoreIpAddresses("25525511135"))