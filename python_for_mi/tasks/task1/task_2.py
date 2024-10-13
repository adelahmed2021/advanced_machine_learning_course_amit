###!!@mocleW EPGTQ!!!6789
massege = "##!!@mocleW EPGTQ!!!6789"
reverse_string=massege[massege.index('@')+1:massege.index(' ')]
reverse_string=(list(reverse_string))
reverse_string.reverse()
reverse_string=''.join(reverse_string)
vowels=massege[massege.index(' ')+1:massege.index('Q')+1]
vowels=vowels.replace('E','')
result = reverse_string +' '+ vowels
print(result)