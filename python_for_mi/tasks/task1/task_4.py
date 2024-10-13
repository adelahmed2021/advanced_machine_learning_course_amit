massege = '##$$$@!yalpstcejorp EPUVT****9887'
reverse_string = massege[massege.index('!')+1:massege.index(' ')]
reverse_string = (list(reverse_string))
reverse_string.reverse()
reverse_string = ''.join(reverse_string)
vowels = massege[massege.index(' ')+1:massege.index('*')]
vowels = vowels.replace('E', 'A')
vowels = vowels.replace('U', 'O')
result = reverse_string + ' ' + vowels


print(result)
