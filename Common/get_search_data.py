#coding=utf-8
def get_search_data():
    filename="E:\\Seleniumlynn\\BaiduSearch\\data\\searchdata.txt"
    f=open(filename,"r")
    s=[]
    for i in f.readlines():
        i=i.strip("\n")
        s.append(i)
    return s
if __name__=="__main__":
    d=get_search_data()
    print(d)
    print(type(d))



