#辞書の作成
my_dict = {"height":168.5}

#作成した辞書に要素を追加
my_dict["eyecolor"] = "brown"
my_dict["nationality"] = "日本"

target = input("input 'height' or 'eyecolor' or 'nationality':")

if target in my_dict:
    print(str(my_dict[target]))
else:
    print("not found")


'''
print("身長：" + str(my_dict["height"]))
print("目の色：" + my_dict["eyecolor"])
print("国籍：" + my_dict["nationality"])
'''
