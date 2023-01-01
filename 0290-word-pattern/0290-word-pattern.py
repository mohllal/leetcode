class Solution:
    # O(n) time and O(n) space
    def wordPattern(self, p: str, s: str) -> bool:
        s_arr = s.split()
        p_dict = {}
        s_dict = {}

        if len(s_arr) != len(p):
            return False

        for index in range(len(s_arr)):
            if s_arr[index] in s_dict:
                if s_dict[s_arr[index]] != p[index]:
                    return False
            else:
                s_dict[s_arr[index]] = p[index]

            if p[index] in p_dict:
                if p_dict[p[index]] != s_arr[index]:
                    return False
            else:
                p_dict[p[index]] = s_arr[index]

        return True