# ML-for-SQL-Injection
机器学习检测SQL注入

本项目是使用机器学习算法来分类SQL注入语句与正常语句：
使用了SVM,Adaboost，决策树，随机森林，逻辑斯蒂回归，KNN，贝叶斯等算法分别对SQL注入语句与正常语句进行分类。
data是收集的样本数据
file中存放的是训练好的各个模型
featurepossess.py是对原始样本进行预处理，提特征。
sqlsvm.py等py文件是训练模型
testsql是对训练好的模型进行测试，用准确率来度量模型效果。
