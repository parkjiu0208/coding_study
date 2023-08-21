newstr = 'aBcDeFg'
mylist = list(newstr)
final = []
for i in range(len(newstr)):
    if mylist[i].isupper() == True:
        final += str(mylist[i]).lower()
        i+=1
    elif mylist[i].isupper() == False:
        final += str(mylist[i]).upper()
        i+=1

new = ''.join(final)
print(new)

# print(input().swapcase()) ... swapcase()라는 좋은 메소드가 있었다. 하하ㅠㅠ