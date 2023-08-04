#Implementiong DSA in programming
class Solution(object):
# create a class called solution with the object 'object'
    def mergeAlternately(self, word1, word2):
#define a method that instantiates the class 'solution'
        merged = []
#implement a string to allow manipulation of the values 
 
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
#determine the minimum length of the string

#incorporate a loop to iterate the values input     
        for i in range(min_len):
#use append to populate the list
            merged.append(word1[i])
            merged.append(word2[i])

        if len1 > len2:
#use extend to add all items of the list 
            merged.extend(word1[min_len:])
        elif len2 > len1:
            merged.extend(word2[min_len:])

#use.join to merge the lists
        return ''.join(merged)

# Test the function
if __name__ == "__main__":
    sol = Solution()
    word1 = "abcd"
    word2 = "pqr"
    result = sol.mergeAlternately(word1, word2)
    print(result)  # Output: "axbyczd"


