"""
<html>
<head>
<meta charset="utf-8">
<title>试试看啦</title>
</head>
<body>
    <h1>试试看啦</h1>
    <p></p>
    <a href="美女第二朵花.pdf">美女第二朵花.pdf</a>
    <p></p>
</body>
</html>
1)提取当前文件夹内所有文件的路径和时间信息,按照时间信息排序
2)从指定URL提取已有的文件信息
3)重新生成index.html文件
"""
import os,sys,time,urllib.request

#0)
url_path = "https://revitalizeast.github.io/webview/index.html"

# 1) 提取当前文件夹的文件信息,不包含子文件夹信息和不必要的文件
array_fn_title =[]
array_title=[]
print("The available list:")
for fn in os.listdir("."):
    if (not os.path.isdir(fn)
        and not fn == "index.html"
        and not fn == os.path.basename(sys.argv[0])) :
        fn_time_str = time.strftime("%y%m%d_%H%M%S", time.localtime(os.path.getmtime(fn)))
        fn_title    = fn_time_str + " " + fn
        array_fn_title.append((fn, fn_title))
        array_title.append(fn_title)
        print(fn_title)

# 2) 提取已有文件信息
try:
    url_req = urllib.request.urlopen(url_path)
    url_str = url_req.read().decode()
    url_strlist = url_str.split("\n")
    #print(url_strlist)
    #print("The existed list:")
    for str_item in url_strlist:
        str_item = str_item.strip()
        # <a href="dangerous.txt">200922_094011 dangerous.txt</a>
        if str_item.startswith("<a href="):
            fn_title = str_item.split(">")[1].split("<")[0]
            if array_title.count(fn_title) == 0:
                fn = str_item.split('"')[1].split('"')[0]
                #print(fn_title)
                array_fn_title.append((fn,fn_title))
except:
    print("No index.html")

#3) 排序
def keyTitle(elem):
    return elem[1]
array_fn_title.sort(key=keyTitle, reverse=True)
#print("The combined list:")
#for (fn,fn_title) in array_fn_title:
#    print(fn_title)

#4) 生成文件
fp = open("index.html","w",encoding="utf-8")
fp.write("<html>" + "\n")
fp.write("<head>" + "\n")
fp.write('<meta charset="utf-8">' + "\n")
fp.write('<title>see see la</title>' + "\n")
fp.write('</head>' + "\n")
fp.write('<body>'+ "\n")
fp.write('<h1>分拆后的.mp4适合手机，若PC先下载再看更好</h1>' + "\n")
fp.write('<p></p>' + "\n")

for (fn,fn_title) in array_fn_title:
    fp.write('<a href="' + fn + '">' + fn_title +'</a>' + "\n")
    fp.write('<p></p>' + "\n")

fp.write('</body>'+ "\n")
fp.write("</html>" + "\n")
fp.close()