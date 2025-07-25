import numpy as np
from sklearn.svm import LinearSVC


### Functions for you to fill in ###

def one_vs_rest_svm(train_x, train_y, test_x):
    """
    Trains a linear SVM for binary classifciation

    Args:
        train_x - (n, d) NumPy array (n datapoints each with d features)
        train_y - (n, ) NumPy array containing the labels (0 or 1) for each training data point
        test_x - (m, d) NumPy array (m datapoints each with d features)
    Returns:
        pred_test_y - (m,) NumPy array containing the labels (0 or 1) for each test data point
    """
    clf=LinearSVC(C=0.1,random_state=0) #C es un parámetro que se usa para controlar el "overfitting" o el "underfitting". random_state es un parámetro que se usa
                                        #para controlar la aleatoriedad en la inicialización de los parámetros del modelo predictivo empleado por el algoritmo. Un valor
                                        #constante de random_state permite que los resultados sean más reproducibles, pues la incialización comienza siempre en "el mismo punto"
    clf.fit(train_x,train_y)
    pred_test_y=clf.predict(test_x)
    return pred_test_y

def multi_class_svm(train_x, train_y, test_x, **args):
    """
    Trains a linear SVM for multiclass classifciation using a one-vs-rest strategy

    Args:
        train_x - (n, d) NumPy array (n datapoints each with d features)
        train_y - (n, ) NumPy array containing the labels (int) for each training data point
        test_x - (m, d) NumPy array (m datapoints each with d features)
    Returns:
        pred_test_y - (m,) NumPy array containing the labels (int) for each test data point
    """
    clf=LinearSVC(C=0.1,random_state=0, **args)
    clf.fit(train_x,train_y)
    pred_test_y=clf.predict(test_x)
    return pred_test_y
    raise NotImplementedError


def compute_test_error_svm(test_y, pred_test_y):
    return 1 - np.mean(pred_test_y == test_y)

