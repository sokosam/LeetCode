class Solution:
    def compress(self, chars: List[str]) -> int:
        char_ptr = 0
        compared_char = chars[0]
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == compared_char:
                count += 1
            else:
                if count != 1:
                    str_count = str(count)
                    for j in range(1, 1 + len(str_count)):
                        chars[char_ptr + j] = str_count[j - 1]

                    char_ptr += 1 + len(str_count)
                else:
                    char_ptr += 1
                compared_char = chars[i]
                chars[char_ptr] = compared_char
                count = 1

        if count != 1:
            str_count = str(count)
            for j in range(1, 1 + len(str_count)):
                chars[char_ptr + j] = str_count[j - 1]
            char_ptr += 1 + len(str_count)
            return char_ptr
        return char_ptr + 1
            