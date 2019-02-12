#代入用のリストの作成
lList = ["HONEY", "花葬", "浸食"]
mList = ["Hysteria", "Cave"]
pList = ["ラック", "ミュージックアワー", "メリッサ"]

#好きなミュージシャンの辞書の作成
musicians = {"L'Arc-en-Ciel" : lList}

musicians["MUSE"] = mList
musicians["ポルノグラフィティ"] = pList

print(musicians["L'Arc-en-Ciel"])
print(musicians["MUSE"])
print(musicians["ポルノグラフィティ"])

