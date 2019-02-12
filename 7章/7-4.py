list = [1, 9, 27, 5, 97]
print("数字あてクイズです")
print("qを入力すると終了します")
while True:
    try:
        str = input("数字を入力してください:")
        if str == "q":
            break
        if int(str) in list:
            print("正解")
        else:
            print("不正解")
    except:
        print("数字を入力するか、qで終了します")