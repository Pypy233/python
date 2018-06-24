from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.svm import SVC
# add package here

iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target
# 利用x_train y_train作为训练集
x_train, x_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=0.3)


class Solution():
    def solve(self, test_data):
        # call function classification
        sc = StandardScaler()
        sc.fit(x_train)
        x_train_std = sc.transform(x_train)
        x_test_std=sc.transform(x_test)
        x_combined_std = np.vstack((x_train_std, x_test_std))
        y_combined = np.hstack((y_train, y_test))
        clf = SVC(kernel='linear', C=1.0).fit(x_train_std, y_train)
        print(clf.score(x_test, y_test))
        return clf.predict(test_data)
        pass
