import json

#从python对象格式化一个json String 
information={"当事人":"周永华","性别":"男","民族":"汉族","出生地":"内蒙古自治区新巴尔虎右旗","案由":"故意杀人罪","相关法院":"内蒙古自治区呼伦贝尔市中级人民法院"}
print(information)
#indent参数是将其格式化 sort_keys参数是将其按字母顺序排序
jsonStr=json.dumps(information,indent=4)
print(jsonStr)

#将python对象写入一个json文件
with open('data.json','w',encoding='utf-8') as f:
    json.dump(information,f,ensure_ascii=False,indent=4)

#json String转化成python对象(字典/list)
obj=json.loads(jsonStr)
print(obj)
print(type(obj))
s='[1,"A","caecae",{"name":"Skye","age":19}]'
obj=json.loads(s)
print(obj)
print(type(obj))

#读取json文件中的信息并转换成python对象
obj=json.load(open('data.json','r'))
print(obj)
print(type(obj))