import requests
from bs4 import BeautifulSoup
import re
import os

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog, QGridLayout, QLabel, QPushButton, QFrame

class InputDialog(QWidget):

    def __init__(self):
        super(InputDialog,self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("漫画爬取")
        self.setGeometry(400,400,300,260)

        label1=QLabel("第一本:")
        label2=QLabel("最后一本:")

        self.nameLable = QLabel("2")#1
        self.first=int(self.nameLable.text())
        self.nameLable.setText(str(self.first))
        self.nameLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.styleLable = QLabel("2")#1030
        self.last=self.styleLable.text()
        self.styleLable.setText(str(self.last))
        self.styleLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)

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
        #2/3/4/
        #多线程同时几个py def传值出去++？
        num=8
        for num1 in range(num,num+1):

            #循环过大（大于2都不行） 会直接返回Process finished with exit code -1073740791 (0xC0000409)
            #716字符问题无法生成文件夹
            #循环不行 只能采用一次次一本本下载完提醒 按多一次
            #后来发现不是循环不行 是这个
            # self.nameLable.setText(num1-1)
            # self.styleLable.setText(num1)
            #循环也有点关系

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

            # circle = requests.get('https://www.manhwa.cc/book/'+str(num1))
            # 将获取的图片地址依次放入count中
            count = []
            # 将获取的网页内容放入BeautifulSoup
            soup = BeautifulSoup(circle.text, 'lxml')
            # 根据谷歌SelectGadGet这个插件，获取html标签，比如获取：#gallery-list

            for item_book in soup.select('.d_bg_t'):
                for book_name in item_book.select('a')[0]:
                    book_name_clean = book_name.string
                    print(num1, book_name_clean)

            for item in soup.select('.d_menu>ul>li'):
                # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
                for a in item.find_all('a'):
                    # print('a', a)
                    # m 是 img标签中存在的属性
                    menu_path = 'https://www.manhwa.cc/' + a.get('href')
                    # count.append(menu_path)
                    # menu_path_num.append(re.findall(r"\d+\.?\d*", menu_path))
                    menu_path_num = re.findall(r"\d+\.?\d*", menu_path)

                    # 当前一部书爬取循环，从上面得到每一章地址后，遍历这么多“章”次

                    # for num in menu_path_num:
                    print('book_url:', menu_path)

                    circle = requests.get(menu_path)
                    # 将获取的图片地址依次放入count中
                    count = []
                    # 将获取的网页内容放入BeautifulSoup
                    soup = BeautifulSoup(circle.text, 'lxml')

                    for title in soup.select('div.fl.r_tab_l'):
                        for title in title.find_all('span'):
                            print('title:', title.text)
                            title = title.text

                    for item in soup.select('.r_img'):
                        # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
                        for img in item.find_all('img'):
                            print('img_url:', img)
                            # m 是 img标签中存在的属性
                            img_path = img.get('data-original')
                            count.append(img_path)

                    # 用enumerate依次取出count中的图片地址 放入v中
                    os.makedirs('D://manhua//整站爬取www.manhwa.cc//整站漫画爬取//' + book_name_clean + '//' + str(title) + '//')
                    for i, v in enumerate(count):
                        # 将获取的v值再次放入request中进行与网站相应
                        image = requests.get(v)
                        # 存取图片过程中，出现不能存储 int 类型，故而，我们对他进行类型转换 str()。w:读写方式打开，b：二进制进行读写。图片一般用到的都是二进制。
                        with open('D://manhua//整站爬取www.manhwa.cc//整站漫画爬取//' + book_name_clean + '//' + str(
                                title) + '//' + str(
                                i) + '.jpg', 'wb') as file:
                            # with open('C://Users//50159//Desktop//manhua//test//' + str(num1) + '_' + str(i) + '.jpg', 'wb') as file:
                            # content：图片转换成二进制，进行保存。
                            file.write(image.content)
                        print(i)



            #爬取代码

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
        #self.first=int(self.nameLable.text())
        #self.last=self.styleLable.text()
        #print(self.first, self.last)
        #os.system(r"python D:\manhua\整站爬取www.manhwa.cc\manhua3.py")


if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=InputDialog()
    myshow.show()
    sys.exit(app.exec_())
    os.system(r"F:\CloudMusic\是萝莉控真是太好了.mp3")

