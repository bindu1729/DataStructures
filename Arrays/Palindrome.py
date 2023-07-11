class Palindrome:
    def __init__(self):
        pass

    def isPalindrome(self, input_str):

        if input_str is None or type(input_str) != str:
            raise ValueError("Invalid inputs")

        return input_str == input_str[::-1]
    def isPalindromeWithoutRevFunc(self,input_str):
        #time cmpl = O(n)
        #space cmpl = O(2N)
        if input_str is None or type(input_str) != str:
            raise ValueError("Invalid inputs")
        rever_str = ""
        for index in range(len(input_str)-1,-1,-1):
            rever_str += input_str[index]
        return rever_str == input_str

    def isPalindromeInPlace(self,input_str):
        #time cmpl = O(n)
        #space cmpl = O(N+2)
        if input_str is None or type(input_str) != str:
            raise ValueError("Invalid inputs")
        start = 0
        end = len(input_str)-1
        while start < end:
            if input_str[start] != input_str[end]:
                return False
            start += 1
            end -= 1
        return True

        # rever = input_str[::-1]
        # if input_str == rever:
        #     return True
        # else:
        #     return False




if __name__ == '__main__':
    pal = Palindrome()
    input_str = "civic"
    if pal.isPalindromeInPlace(input_str):
        print(f"Given String {input_str} is Palindrome")
    else:
        print(f"Given String {input_str} is not Palindrome")