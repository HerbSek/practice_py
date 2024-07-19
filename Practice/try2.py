# DUPLICATE 

# class solution():
#     def __init__(self,nums):
#         self.nums = nums

#     def findDuplicate(self):
#         my_set = set()
#         for i in self.nums:
#             if i in my_set:
#                 return True
#             my_set.add(i)
#         return False 


# my_array = [1,2,3,4]
# my_solu=solution(my_array)

# print(my_solu.findDuplicate())



# def array_alo(my_array): 
#     my_array.sort()
#     print(my_array)
#     for i in range(0,len(my_array)-1):
#         if my_array[i] == my_array[i+1]:
#             return True
#     return False

# if __name__ == '__main__':
#     my_array1 = [1,2,3,4,5,5,2,3,4]
#     print(array_alo(my_array1))


# PANGRAM (A sentence where every letter of the English alphabet appears at least once )

# s = "TheQuickBrownFoxJumpsOverTheLazyDog"
# s2 = 'This is not a pangram'

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# def function(sentence, alphabet= alphabet):
#     lower = sentence.lower()
#     my_set = set()
#     for i in lower:
#         if i in alphabet:
#             my_set.add(i)
#     return len(my_set) == len(alphabet)

# if __name__ == '__main__':
#     print(function(s))
#     print(function(s2))


# REVERSE VOWELS 

# Input: s= "hello"
# Output: "holle"

s= "AeIoU"


def function(s , vowels = ['a','e','i','o','u','A','E','I','O','U']):
    f_point = 0
    l_point = len(s)-1
    s = list(s)
    while f_point < l_point:
        while s[f_point] not in vowels and f_point < l_point:
            f_point += 1
        while s[l_point] not in vowels and f_point < l_point:
            l_point -= 1
        s[f_point], s[l_point] = s[l_point], s[f_point]
        f_point+=1
        l_point-=1
    return(''.join(s))


print(function(s))