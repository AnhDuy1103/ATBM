import string
plaintex="van cong anh duy"
key=22
a=list(string.ascii_lowercase)  # Tạo danh sách chữ cái từ a đến z
b=a[key:]+a[:key]
print("Ten duoc ma hoa: ",end='')
for i in plaintex:
    if i in a:
        print(b[a.index(i)],end='')
    else:
        print(i,end="")

