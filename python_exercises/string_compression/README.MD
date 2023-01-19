Create a function string_compression(s:str)->str that takes a string and performs basic string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3". If the compressed string would not become smaller than the original string, return the original string.

Test case:

Input:

s = "aabcccccaaa"

string_compression(s)

Output:

"a2b1c5a3"

Note:

    Your function should return the compressed string only if it's shorter than the original string otherwise return the original string
    Your function should only consider alphabets in the input and ignore spaces and special characters
    The test case is provided to check the correctness of your function , you need to test your function against multiple test cases to check the robustness of your solution.