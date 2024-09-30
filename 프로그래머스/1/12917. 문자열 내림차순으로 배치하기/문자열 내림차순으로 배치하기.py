def solution(s):
    ord_list = []
    chr_list = []
    for i in s:
        ord_list.append(ord(i))
    ord_list.sort()
    ord_list.reverse()
    for j in ord_list:
        chr_list.append(chr(j))
    return "".join(chr_list)