class reverse_string:
    def reverse_string(self, s):
        if not isinstance(s, str) :
            raise TypeError("Input must be a string.")
        elif len(s) < 2 :
            raise ValueError("Not Good")
        else:  
            return s[::-1]


reverser = reverse_string()

# print(reverser.reverse_string("asd"))     # 正常反轉: dsa
# print(reverser.reverse_string("a"))       # 印出 "Not Good"
# print(reverser.reverse_string(123))       # 印出 "Not Good"
print(reverser.reverse_string("asd "))    # 反轉並保留空格: " dsa"

    
    
