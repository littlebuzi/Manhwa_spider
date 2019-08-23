<hr>
<br>

# 目的

<br>

1.目标网站：https://www.这里是网址.cc/

![1565345268608](https://littlebuzi.github.io/post-images/1565345268608.png)

2.目标结果：获取全部漫画图片文件，并分好文件夹


<hr>
<br>

# 实现过程


<br>


## 基本逻辑

![1565360279264](https://littlebuzi.github.io/post-images/1565360279264.png)

## 代码实现

<br>

```

import requests
from bs4 import BeautifulSoup
import re
import os

#1-1030
for num1 in range(1,1031):
    circle = requests.get('https://这里是网址/book/'+str(num1))
    # 将获取的图片地址依次放入count中
    count = []
    # 将获取的网页内容放入BeautifulSoup
    soup = BeautifulSoup(circle.text, 'lxml')
    # 根据谷歌SelectGadGet这个插件，获取html标签，比如获取：#gallery-list

for item_book in soup.select('.d_bg_t'):
    for book_name in item_book.find_all('a'):
        if(book_name.string!='韩国'and book_name.string!='男性'):
            book_name_clean=book_name.string
            print(num1, book_name_clean)

os.makedirs('D://manhua//整站漫画爬取//' + str(num1) +'.'+ book_name_clean )

#menu_path_num = []

for item in soup.select('.d_menu>ul>li'):
    # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
    for a in item.find_all('a'):
        #print('a', a)
        # m 是 img标签中存在的属性
        menu_path = 'https://www.manhwa.cc/' + a.get('href')
        #count.append(menu_path)
        #menu_path_num.append(re.findall(r"\d+\.?\d*", menu_path))
        menu_path_num=re.findall(r"\d+\.?\d*", menu_path)

        #当前一部书爬取循环，从上面得到每一章地址后，遍历这么多“章”次

        #for num in menu_path_num:
        print('book_url:',menu_path)
        circle = requests.get(menu_path)
        # 将获取的图片地址依次放入count中
        count = []
        # 将获取的网页内容放入BeautifulSoup
        soup = BeautifulSoup(circle.text, 'lxml')
        # 根据谷歌SelectGadGet这个插件，获取html标签，比如获取：#gallery-list
				
        for title in soup.select('div.fl.r_tab_l'):
            for title in title.find_all('span'):
                print('title:', title.text)
                title=title.text

        for item in soup.select('.r_img'):
            # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
            for img in item.find_all('img'):
                print('img_url:', img)
                # m 是 img标签中存在的属性
                img_path = img.get('data-original')
                count.append(img_path)
        # 用enumerate依次取出count中的图片地址 放入v中
        os.makedirs('D://manhua//整站漫画爬取//' +  book_name_clean + '//' + str(title) + '//')
        for i, v in enumerate(count):
            # 将获取的v值再次放入request中进行与网站相应
            image = requests.get(v)
            # 存取图片过程中，出现不能存储 int 类型，故而，我们对他进行类型转换 str()。w:读写方式打开，b：二进制进行读写。图片一般用到的都是二进制。
            with open('D://manhua//整站漫画爬取//' + book_name_clean + '//'+ str(title) + '//' +str(i) + '.jpg', 'wb') as file:
            #with open('C://Users//50159//Desktop//manhua//test//' + str(num1) + '_' + str(i) + '.jpg', 'wb') as file:
                # content：图片转换成二进制，进行保存。
                file.write(image.content)
            print(i)
```

到这基本工作已完成，进入测试阶段，出现以下

<hr>
<br>

# 测试问题


1.第250本左右，书名字开始出现异常，爬取书名有其他文字并出现混乱，因为之前是通过最前面几本书的情况，通过抛弃字样，来筛选出书名，而后1030本里标签发生变动，所以之后通过只取第一个出现的标签代替现在的筛选。

2.文件夹命名及生成文件夹出错，由于整理时出现混乱，代码写重复了。而后修改。

3.中途停止，可能是网站识别到了这是爬虫，而后添加伪浏览器头部head，还是会停，基本是connect超时。

针对上面问题，修改成了2.0版本:

```

import requests
from bs4 import BeautifulSoup
import re
import os

#1-1030
for num1 in range(2,1031):
    #716字符问题无法生成文件夹
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
    circle = requests.get('https://这里是网址/book/' + str(num1))

# 将获取的图片地址依次放入count中
count = []
# 将获取的网页内容放入BeautifulSoup
soup = BeautifulSoup(circle.text, 'lxml')
# 根据谷歌SelectGadGet这个插件，获取html标签，比如获取：#gallery-list

for item_book in soup.select('.d_bg_t'):
    for book_name in item_book.select('a')[0]:
        book_name_clean = book_name.string
        print(num1, book_name_clean)

#os.makedirs('D://manhua//整站漫画爬取//' + str(num1) +'.'+ book_name_clean )

for item_book in soup.select('.d_bg_t'):
    for book_name in item_book.find_all('a'):
        if(book_name.string!='韩国'and book_name.string!='男性'):
            book_name_clean=book_name.string
            print(num1, book_name_clean)

#menu_path_num = []

for item in soup.select('.d_menu>ul>li'):
    # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
    for a in item.find_all('a'):
        #print('a', a)
        # m 是 img标签中存在的属性
        menu_path = 'https://www.manhwa.cc/' + a.get('href')
        #count.append(menu_path)
        #menu_path_num.append(re.findall(r"\d+\.?\d*", menu_path))
        menu_path_num=re.findall(r"\d+\.?\d*", menu_path)

        #当前一部书爬取循环，从上面得到每一章地址后，遍历这么多“章”次

        #for num in menu_path_num:
        print('book_url:',menu_path)
        
        circle = requests.get(menu_path)
        # 将获取的图片地址依次放入count中
        count = []
        # 将获取的网页内容放入BeautifulSoup
        soup = BeautifulSoup(circle.text, 'lxml')

        for title in soup.select('div.fl.r_tab_l'):
            for title in title.find_all('span'):
                print('title:', title.text)
                title=title.text

        for item in soup.select('.r_img'):
            # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
            for img in item.find_all('img'):
                print('img_url:', img)
                # m 是 img标签中存在的属性
                img_path = img.get('data-original')
                count.append(img_path)
                
        # 用enumerate依次取出count中的图片地址 放入v中
        os.makedirs('D://manhua//整站漫画爬取//' +  book_name_clean + '//' + str(title) + '//')
        for i, v in enumerate(count):
            # 将获取的v值再次放入request中进行与网站相应
            image = requests.get(v)
            # 存取图片过程中，出现不能存储 int 类型，故而，我们对他进行类型转换 str()。w:读写方式打开，b：二进制进行读写。图片一般用到的都是二进制。
            with open('D://manhua//整站漫画爬取//' + book_name_clean + '//'+ str(title) + '//' +str(i) + '.jpg', 'wb') as file:
            #with open('C://Users//50159//Desktop//manhua//test//' + str(num1) + '_' + str(i) + '.jpg', 'wb') as file:
                # content：图片转换成二进制，进行保存。
                file.write(image.content)
            print(i)
						
```

<hr>
<br>

# 爬取过程：

<hr>
<br>

![1565361188393](https://littlebuzi.github.io/post-images/1565361188393.png)

![1565361235369](https://littlebuzi.github.io/post-images/1565361235369.png)

![1565361244280](https://littlebuzi.github.io/post-images/1565361244280.png)

基本可行，最高纪录 ，爬取四本后停止。

真的太多了，一本大小平均150M左右。

<hr>
<br>

# 总结：

<hr>
<br>

爬取正本漫画 ✅

整站漫画半自动化爬取（停止需手动启动一次）✅

全自动下载网站漫画 （会被网站截停）❌

<br>

<center>
	
2.0优化版

</center>

<br>

------

<br>

# 特点

<br>

ui界面添加✅

网站截停后 播放音乐提醒 接近半自动重启 ✅

各个细节爬取优化，优化接近自身无报错 ✅

cmd输出界面优化✅

计时器检测添加中（待）

全自动重启（待）

<br>

------

<br>

# 逻辑

<br>

![1565871675669](https://littlebuzi.github.io/post-images/1565871675669.png)

<br>

------

<br>

# 代码

<br>

## 启动代码：

```

import os

os.system(r"python D:\manhua\这里是网址\manhua4.py")

os.system(r"F:\CloudMusic\是萝莉控真是太好了.mp3")

```

## 爬取代码：

```

import requests
from bs4 import BeautifulSoup
import re
import os

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog, QGridLayout, QLabel, QPushButton, QFrame, QProgressBar

first=1

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
                circle = requests.get('https://这里是网址/book/' + str(num1))

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
                    menu_path = 'https://这里是网址/' + a.get('href')
                    # count.append(menu_path)
                    # menu_path_num.append(re.findall(r"\d+\.?\d*", menu_path))
                    menu_path_num = re.findall(r"\d+\.?\d*", menu_path)

                    # 当前一部书爬取循环，从上面得到每一章地址后，遍历这么多“章”次

                    # for num in menu_path_num:
                    #print('book_url:', menu_path)


                    circle = requests.get(menu_path)
                    count = []
                    soup = BeautifulSoup(circle.text, 'lxml')
                    #print(menu_path)
                    print('.', end='')

                    for title in soup.select('div.fl.r_tab_l'):
                        for title in title.find_all('span'):
                            #print('title:', title.text)
                            title = title.text

                    for item in soup.select('.r_img'):
                        for img in item.find_all('img'):
                            #print('img_url:', img)
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

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=InputDialog()
    myshow.show()
    sys.exit(app.exec_())


```

<br>

------

<br>

# 过程

<br>

![1565763309680](https://littlebuzi.github.io/post-images/1565763309680.png)

![1565763331643](https://littlebuzi.github.io/post-images/1565763331643.png)

![1565763348226](https://littlebuzi.github.io/post-images/1565763348226.png)

<br>

------

<br>

# 总结

<br>

整站漫画全自动化爬取✅

不能自动重启❌

基本百分之95的功能实现，项目可宣布成功完成！✅

<br>
