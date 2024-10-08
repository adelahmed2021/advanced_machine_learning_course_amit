massege = '&&&**$gnirtS PLIO!!@1234'
reverse_string=massege[massege.index('$')+1:massege.index(' ')]
reverse_string=(list(reverse_string))
reverse_string.reverse()
reverse_string=''.join(reverse_string)
vowels=massege[massege.index(' ')+1:massege.index('!')]
vowels=vowels.replace('I','E')
vowels=vowels.replace('O','U')
result = reverse_string +' '+ vowels
print(result)