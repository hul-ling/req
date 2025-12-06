import pandas as pd

#读取CSV文件
df = pd.read_csv('day2.csv')

#将'rating'列转换为浮点数类型，以便进行数值计算
df['rating'] = df['评分'].astype(float)

#新增“档级”列（cut自动分级）
df['level'] = pd.cut(df['rating'],
                     bins=[0, 7, 8, 9.5, 10],
                     labels=[ '良好', '优秀', '经典','神作'])

#生产透视表：每档级的电影数量
pivot = df.groupby('level').size().reset_index(name='电影数量')

#输出结果到excel文件
with pd.ExcelWriter('day3.xlsx',engine='openpyxl') as w:
    df.to_excel(w,sheet_name='原始数据',index=False)
    pivot.to_excel(w,sheet_name='透视',index=False)

print('报告已生成：day3.xlsx（原始',len(df),'行）')