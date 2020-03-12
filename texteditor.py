def wbcjg(x):#文本初加工
    with open(x) as file_object:
        contents=file_object.read()
    import string
    remove1=contents.maketrans('','',string.punctuation)
    contents=contents.translate(remove1)
    contents=contents.lower()
    contents = list(contents.split())
    return contents
def wbcbcl(x):#文本初步处理，去掉停用词，形成列表
    value =x
    from nltk.corpus import stopwords
    for i in stopwords.words('english'):
        n=value.count(i)
        for j in range(n):
            value.remove(i)
    return value
def cptj(x):#词频统计
    from nltk import FreqDist
    ciping=FreqDist(x)
    return ciping
def ciyuntu():
    LJ=E1.get()
    import os
    if not os.path.isfile(LJ):
        wenjianbucunzai()
    else:
        from wordcloud import WordCloud
        import matplotlib.pyplot as plt
        f = open(LJ).read()
        wordcloud = WordCloud(
            background_color="white",  # 设置背景
            width=1500,  # 设置宽度
            height=960,  # 设置高度
            margin=10  # 设置边缘
        ).generate(f)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()
def wenjianbucunzai():#假设文件不存在
        top2=Tk()
        top2.title('文件不存在')
        top2.geometry("300x200")
        def tc2():
            top2.destroy()
        L2= Label(top2, text='【请输入存在的文件名】')
        L2.pack(pady='11m')
        OK1 = Button(top2, text='OK', command=tc2)
        OK1.pack()
        top2.mainloop()
from tkinter import *
def XS():
    LJ = E1.get()
    import os
    if not os.path.isfile(LJ):
        wenjianbucunzai()
    else:
        top3=Tk()
        top3.title(LJ[:-4])
        top3.geometry("600x600")
        text = Text(top3, width=300, height=590,bd=5)
        with open(LJ) as file_object:
            contents=file_object.read()
        text.pack()
        text.insert(INSERT,contents)
        top3.mainloop()
def CSTJ():
    LJ = E1.get()
    import os
    if not os.path.isfile(LJ):
        wenjianbucunzai()
    else:
        a=wbcjg(LJ)
        num=len(a)
        top4=Tk()
        top4.title('词数统计')
        top4.geometry('200x100')
        L4 = Label(top4, text='本文共有【{}】词'.format(num))
        L4.pack(pady='11m')
def CPTJ():
    LJ = E1.get()
    import os
    if not os.path.isfile(LJ):
        wenjianbucunzai()
    else:
        a=wbcjg(LJ)
        b=wbcbcl(a)
        c=cptj(b)
        c.plot(6, cumulative=False)
def WJXR():
    top5=Tk()
    top5.title('文件写入')
    top5.geometry('600x650')
    LB5=Label(top5,text='【请输入纯英文文章（可用英文标点）】')
    LB5.pack(pady='2m')
    texT=Text(top5,width=100, height=40,bd=5)
    def XIERU():
        Content=texT.get('1.0','end')
        top6=Tk()
        top6.title('文件名')
        top6.geometry('300x150')
        lB=Label(top6,text='请输入文件名(以.txt结尾)')
        E=Entry(top6,bd=5)
        lB.pack()
        E.pack()
        def OK():
            a=open(E.get(),'w')
            a.write(Content)
            a.close()
            top6.destroy()
        OK_B=Button(top6,text='OK',command=OK)
        OK_B.pack()
        top5.destroy()
    XIERU_B=Button(top5,text='【写入】',command=XIERU)
    texT.pack()
    XIERU_B.pack(pady='2m')
def gjc():
    LJ = E1.get()
    import os
    if not os.path.isfile(LJ):
        wenjianbucunzai()
    else:
        a = wbcjg(LJ)
        b = wbcbcl(a)
        c = cptj(b)
        d = []
        for ker in c.most_common():
            d.append(ker)
        top7 = Tk()
        top7.title('关键词')
        top7.geometry('300x300')
        T = Text(top7, width=300, height=300, bd=5)
        T.pack()
        T.insert(INSERT, '本文的关键词为{}，{}，{}，{}，{}，{}'.format(d[0][0], d[1][0], d[2][0], d[3][0], d[4][0], d[5][0]))
top1=Tk()
top1.title('文本编辑器')
top1.geometry("290x280")
Lb1=Label(top1,text='【请输入文件名】')
E1=Entry(top1,bd=5,width=20)
ciyuntu_B=Button(top1,text='词云图',command=ciyuntu)
XS_B=Button(top1,text='显示文本',command=XS)
CSTJ_B=Button(top1,text='词数统计',command=CSTJ)
CPTJ_B=Button(top1,text='词频统计',command=CPTJ)
WJXR_B=Button(top1,text='文件写入',command=WJXR)
GJC_B=Button(top1,text='关键词',command=gjc)
Lb1.grid_configure(column=1,row=1,columnspan=1,rowspan=1,pady='10m',padx='2.5m')
E1.grid_configure(column=2,row=1,columnspan=1,rowspan=1)
CSTJ_B.grid_configure(column=1,row=5,columnspan=1,rowspan=1,pady='2m')
CPTJ_B.grid_configure(column=2,row=5,columnspan=1,rowspan=1,pady='2m')
ciyuntu_B.grid_configure(column=1,row=6,columnspan=1,rowspan=1,pady='2m')
XS_B.grid_configure(column=1,row=4,columnspan=1,rowspan=1,pady='2m')
WJXR_B.grid_configure(column=2,row=4,columnspan=1,rowspan=1,pady='2m')
GJC_B.grid_configure(column=2,row=6,columnspan=1,rowspan=1,pady='2m')
top1.mainloop()




