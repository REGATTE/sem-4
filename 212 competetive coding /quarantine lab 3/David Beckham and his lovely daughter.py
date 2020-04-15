//David Beckham and his lovely daughter
"""
David Beckham is a nice dude and a father. One day, he comes home very late and asks his little daughter to tell him a bedtime story. Since his daughter waited for David a long time, she has decided not to tell any funny story to her dad. However, David is so persistent in listening to a story from his daughter. Now his daughter has decided to give David a challenge. If David solve the challenge, then she will tell the story otherwise not. The challenge is, David’s daughter has N number of dolls in a sequence S = [s1,s2,s3….sN] (i.e. string of length N). Each doll si has either a number or letter written on it. Now David can change the sequence in any way through swapping, shuffling or even removal of dolls from the S and make a new sequence T which is a palindrome. Now David’s daughter asks him to make a lengthy palindrome with dolls and tell him that what is the number of dolls X. If S = [abc] then X = 1 as the palindrome are either a OR b OR c If S = [aabbcc] then X = 6. As the palindromes can be abccba OR baccab OR cbaabc OR any other palindromic string of length 6. If S = [abbaccd] then X = 7. If S = [aba] then X = 3.

Input Format

abc

Constraints

NA

Output Format

1
"""

def David(my_string) :
    counter = dict.fromkeys(list(my_string), 0)
    for l in list(my_string) :
        counter[l] = counter[l] + 1
    half_word = ''
    center = ''
    for letter in counter :
        quot_mod = divmod(counter[letter],2)
        to_add = letter * quot_mod[0]
        half_word = half_word + to_add
        if quot_mod[1] == 1:
            center = letter
    return half_word + center + half_word[::-1]
string = ((David(input())))
print(len(string))