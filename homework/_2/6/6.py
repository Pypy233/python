from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

# add package here

iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target
# 使用x_train y_train作为训练集
x_train, x_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=0.3)


class Solution():
    def solve(self, test_data):
        # call function logisticRegression
        sc = StandardScaler()
        sc.fit(x_train)
        x_train_std = sc.transform(x_train)
        x_test_std = sc.transform(x_test)
        x_combined_std = np.vstack((x_train_std, x_test_std))
        y_combined_std = np.hstack((y_train, y_test))
        lr = LogisticRegression(C=1000.0)

        lr.fit(x_train_std, y_train)
        return lr.predict(test_data)
        pass
