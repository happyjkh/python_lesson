gender=input('请输入性别（男或女）：')
weight=eval(input('请输入体重（KG）：'))
high=eval(input('请输入身高 ( 公分 )：'))
age=eval(input('请输入年龄：'))
if gender=='男':
    BMR=13.7*weight + 5.0 *high - 6.8*age + 66
elif gender=='女':
    BMR=9.6*weight + 1.8 *high -4.7 *age+ 655
else:
    BMR=-1

if BMR!=-1:
    print('基础代谢率为：',BMR)
else:
    print('无法识别')
