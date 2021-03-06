# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:40:05 2017

@author: wf
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from featurepossess import generate
from sklearn.externals import joblib

sql_matrix=generate("./data/sqlnew.csv","./data/sql_matrix.csv",1)
nor_matrix=generate("./data/normal_less.csv","./data/nor_matrix.csv",0)

df = pd.read_csv(sql_matrix)
df.to_csv("./data/all_matrix.csv",encoding="utf_8_sig",index=False)
df = pd.read_csv( nor_matrix)
df.to_csv("./data/all_matrix.csv",encoding="utf_8_sig",index=False, header=False, mode='a+')

# with open('sql_matrix', 'ab') as f:
#     f.write(open('nor_matrix', 'rb').read())
feature_max = pd.read_csv('./data/all_matrix.csv')
arr=feature_max.values
data = np.delete(arr, -1, axis=1) #删除最后一列
#print(arr)
target=arr[:,7]
#随机划分训练集和测试集
train_data,test_data,train_target,test_target = train_test_split(data,target,test_size=0.3,random_state=3)
#模型
clf=tree.DecisionTreeClassifier(criterion="entropy",max_depth=1)
clf.fit(train_data,train_target)#训练模型
joblib.dump(clf, './file/tree.model')
print("tree.model has been saved to 'file/tree.model'")
#clf = joblib.load('svm.model')
y_pred=clf.predict(test_data)#预测
print("y_pred:%s"%y_pred)
print("test_target:%s"%test_target)
#Verify
print('Precision:%.3f' %metrics.precision_score(y_true=test_target,y_pred=y_pred))#查全率
print('Recall:%.3f' %metrics.recall_score(y_true=test_target,y_pred=y_pred))#查准率
print(metrics.confusion_matrix(y_true=test_target,y_pred=y_pred))#混淆矩阵

