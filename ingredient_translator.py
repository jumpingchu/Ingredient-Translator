"""
Translate ingredient names:
Chinese <---> Japanese.
"""

import json
import pyperclip
from tkinter import *

TW_JP_dict = {
    '高果糖糖漿':'果糖ブドウ糖液糖',
    '菊糖':'イヌリン',
    '異麥芽寡糖':'イソモルトオリゴ糖',
    '葡萄糖':'グルコース',
    '氯化鈉':'塩化ナトリウム',
    '葡萄柚濃縮果汁':'グレープフルーツ濃縮果汁',
    '檸檬酸':'クエン酸',
    '檸檬酸鈉':'クエン酸ナトリウム',
    '蘋果酸':'リンゴ酸',
    '氯化鉀':'塩化カリウム',
    '氯化鎂':'塩化マグネシウム',
    '乳酸鈣':'乳酸カルシウム',
    '葡萄糖酸內酯':'グルコノラクトン',
    '麩酸鈉':'グルタミン酸ナトリウム',
    '碳酸鎂':'炭酸マグネシウム',
    '胺基酸':'アミノ酸'
}

# 存取字典為 json
# with open("TW_to_JP.json", "w", encoding="utf-8") as f:
#     json.dump(TW_JP_dict, f, ensure_ascii=False)

window = Tk()
window.title('中日翻譯機')

# 翻譯 function
def translate():
    """
    輸入中文或日文，會自動判斷翻譯的目標語言
    按下翻譯後，同步複製到剪貼簿
    """
    # 清除前一次的輸出，Entry delete index 第一個為 0
    e2.delete(0, 'end')
    
    # 若輸入為中文，則輸出日文
    if e_value.get() in TW_JP_dict.keys():
        word = TW_JP_dict[e_value.get()]
    
    # 反之，若輸入為日文，則輸出中文
    else:
        word_index = list(TW_JP_dict.values()).index(e_value.get())
        word = list(TW_JP_dict.keys())[word_index]
    
    # 置中插入 (因為改用Entry替代Text，所以置中直接在 Enrty 中進行)
    # tag_configure, tag_add 使用在 Text
#    e2.tag_configure('center', justify='center')
    e2.insert(END, word)
#    e2.tag_add('center', 1.0, END)

    # 複製至剪貼簿
    pyperclip.copy(word)

# 翻譯按鈕
b = Button(window,text='翻譯', command=translate, height=1, width=5)
b.grid(row=0, column=2, padx=10)

# 輸入區塊
l = Label(window, text='輸入想要翻譯的字: ')
l.grid(row=0, column=0, padx=10)

e_value = StringVar()
e = Entry(window, textvariable=e_value, justify='center')
e.grid(row=0, column=1, ipady=4)

# 顯示翻譯區塊
e2 = Entry(window, justify='center', width=15)
e2.grid(row=0, column=3, ipady=4)

window = mainloop()
