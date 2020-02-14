import requests
list_file = []*8
for i in range(1,9):
    list_file.append("image/"+str(i)+".txt")
print(list_file)
list_image_url = []
dict_ = {"0":"英语","1":"语文","2":"数学","3":"历史","4":"生物","5":"地理","6":"政治","7":"物理"}
dict_eng = {"0":"1","1":"2","2":"3","3":"4","4":"5","5":"6","6":"7","7":"8"}
for i in range(7,8):
    with open(list_file[i],'r') as f:
        list_image_url = f.read().split("\n")
    for j in range(0,len(list_image_url)-1):
        re = requests.get(list_image_url[j])
        print(dict_[str(i)]+"第"+str(j)+"张图片")
        with open("image/"+dict_eng[str(i)]+"/"+str(j)+".jpg","wb") as f:
            f.write(re.content)
        # print()
print(len(list_image_url))
