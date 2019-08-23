import requests
from bs4 import BeautifulSoup
import re
import os

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog, QGridLayout, QLabel, QPushButton, QFrame, QProgressBar

first=16

class InputDialog(QWidget):

    def __init__(self):
        super(InputDialog,self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("漫画爬取")
        self.setGeometry(50,50,1200,600)

        label1=QLabel("第一本:")
        label2=QLabel("最后一本:")

        self.nameLable = QLabel("1")#1
        self.first=int(self.nameLable.text())
        self.nameLable.setText(str(self.first))
        self.nameLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.styleLable = QLabel("1")#1030
        self.last=self.styleLable.text()
        self.styleLable.setText(str(self.last))
        self.styleLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)

        # 设置进度条(弃用)

        nameButton=QPushButton("更改")
        nameButton.clicked.connect(self.selectName)
        styleButton=QPushButton("更改")
        styleButton.clicked.connect(self.selectStyle)
        okButton = QPushButton("OK")
        okButton.clicked.connect(self.selectOk)

        mainLayout=QGridLayout()
        mainLayout.addWidget(label1,0,0)
        mainLayout.addWidget(self.nameLable,0,1)
        mainLayout.addWidget(nameButton,0,2)
        mainLayout.addWidget(label2,1,0)
        mainLayout.addWidget(self.styleLable,1,1)
        mainLayout.addWidget(styleButton,1,2)
        mainLayout.addWidget(okButton,2,1)

        self.setLayout(mainLayout)

    #爬取代码
    def ManHua(self):

        for num1 in range(first,1030):
            import urllib.request  # url包

            def openUrl(circle):
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                    'Host': 'jandan.net'
                }
                req = urllib.request.Request(circle, headers=headers)
                response = urllib.request.urlopen(req)  # 请求
                html = response.read()  # 获取
                html = html.decode("utf-8")  # 解码
                print(html)  # 打印

            if __name__ == "__main__":
                circle = requests.get('https://www.manhwa.cc/book/' + str(num1))

            count = []
            soup = BeautifulSoup(circle.text, 'lxml')

            for item_book in soup.select('.d_bg_t'):
                for book_name in item_book.select('a')[0]:
                    book_name_clean = book_name.string
                    print('')
                    print("正在下载：",num1, book_name_clean)
                    aa=0
                    #print(aa,num1)
                    if num1>aa:
                        aa=num1
                        #print(aa)
                        for i in range(int(num1*(100/1030))+1):
                            print('\r'+'总进度：' + '▇' * (i // 2) + str(i) + '%', end='')
                            print('')

            for item in soup.select('.d_menu>ul>li'):
                for a in item.find_all('a'):
                    menu_path = 'https://www.manhwa.cc/' + a.get('href')
                    # count.append(menu_path)
                    # menu_path_num.append(re.findall(r"\d+\.?\d*", menu_path))
                    menu_path_num = re.findall(r"\d+\.?\d*", menu_path)

                    # 当前一部书爬取循环，从上面得到每一章地址后，遍历这么多“章”次

                    # for num in menu_path_num:
                    #print('book_url:', menu_path)


                    circle = requests.get(menu_path)
                    # 将获取的图片地址依次放入count中
                    count = []
                    # 将获取的网页内容放入BeautifulSoup
                    soup = BeautifulSoup(circle.text, 'lxml')
                    #print(menu_path)
                    print('.', end='')

                    for title in soup.select('div.fl.r_tab_l'):
                        for title in title.find_all('span'):
                            #print('title:', title.text)
                            title = title.text

                    for item in soup.select('.r_img'):
                        # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
                        for img in item.find_all('img'):
                            #print('img_url:', img)
                            # m 是 img标签中存在的属性
                            img_path = img.get('data-original')
                            count.append(img_path)

                    #自动识别'文件夹+文件'重复后跳过下载如何continue
                    if(os.path.exists('D:/manhua/manhuatest/' + book_name_clean + '/' + str(title) + '/')):
                        continue
                    else:
                        os.makedirs('D:/manhua/manhuatest/' + book_name_clean + '/' + str(title) + '/')

                        for i, v in enumerate(count):
                            image = requests.get(v)
                            if (os.path.exists('D:/manhua/manhuatest/' + book_name_clean + '/' + str(title) + '/' + str(i) + '.jpg')):
                                continue
                            else:
                                with open('D:/manhua/manhuatest/' + book_name_clean + '/' + str(title) + '/' + str(i) + '.jpg', 'wb') as file:
                                    file.write(image.content)
                                #print(i)
                                continue
                        continue


    def selectName(self):
        name,ok = QInputDialog.getText(self,"第一本","第一本序号:",
                                       QLineEdit.Normal,self.nameLable.text())
        if ok and (len(name)!=0):
            self.nameLable.setText(name)
    def selectStyle(self):
        style, ok = QInputDialog.getText(self, "最后一本", "最后一本序号:",
                                        QLineEdit.Normal, self.nameLable.text())
        if ok and (len(style)!=0):
            self.styleLable.setText(style)
    def selectOk(self):
        self.ManHua()
        os.system(r"F:\CloudMusic\是萝莉控真是太好了.mp3")
        #self.first=int(self.nameLable.text())
        #self.last=self.styleLable.text()
        #print(self.first, self.last)
        #os.system(r"python D:\manhua\整站爬取www.manhwa.cc\manhua3.py")



if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=InputDialog()
    myshow.show()
    #InputDialog().ManHua()
    sys.exit(app.exec_())





