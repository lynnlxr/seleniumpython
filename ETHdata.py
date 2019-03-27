#coding=utf-8
import requests
url="https://api.etherscan.io/api?endblock=999999999&address=0xbb1fa4fdeb3459733bf67ebc6f893003fa976a82&offset=1000&apikey=11GPECQXMM7QMM2Q4AN9A9J8IGJ7RJP4YP&module=account&action=txlist&startblock=0&page=1&sort=desc"
f=requests.get(url)
data=f.json()
print(type(data))
print(data)
h=data["result"]
i = 0
t = len(h)
hash = 0
s = 0
user = 0
for i in range(t):
        #print(h[i]["timeStamp"])
        # print(type(h[i]["timeStamp"]))
    if 1550678400<=int(h[i]["timeStamp"])<=1550764800:
        print(h[i])
        print((h[i]["timeStamp"]))
        hash=hash+1
        s = s + int(h[i]["value"])
        if h[i]['from'] != h[i + 1]['from']:
            user = user + 1
print("Tx(24h):%d" %hash)    #Tx：24h的hash个数
print("Volume(24h):%d" %s)    #value之和
print("User(24h):%d" % user)  # get_users:不同from个数

#Tx：24h的hash个数
# def get_Transaction():
#     hash = 0
#     for i in range(t):
#         #print(h[i]["timeStamp"])
#         # print(type(h[i]["timeStamp"]))
#         if 1550678400<=int(h[i]["timeStamp"])<=1550764800:
#             print(h[i])
#             print((h[i]["timeStamp"]))
#             hash=hash+1
#     print("Tx(24h):%d" %hash)
# # get_volume:
# def get_volume():
#     s = 0
#     for i in range(t):
#         if 1550678400 <= int(h[i]["timeStamp"]) <= 1550764800:
#             s=s+int(h[i]["value"])
#     print("Volume(24h):%d" %s)
# # get_users:不同from个数
# def get_users():
#     user=0
#     for i in range(t):
#         if 1550678400 <= int(h[i]["timeStamp"]) <= 1550764800:
#             if h[i]['from']!=h[i+1]['from']:
#                 user=user+1
#     print("User(24h):%d" %user)

#
#
#
#
#
# if __name__=="__main__":
#     get_Transaction()
#     get_volume()
#     get_users()




