from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

data = load_iris()
features = data.data
feature_names = data.feature_names
target = data.target
targets_names = data.target_names

###      здесь находим как классифицировать Iris Setosa без ML       ###
#имена признаков
labels = targets_names[target]
#копируем длины лепестков - это второй признак
plenght = features[:,2]
#собираем массив булевых значений - Сетоса или нет
is_setosa = (labels == 'setosa')
#находим максимальное значение для этого признака
max_setosa = plenght[is_setosa].max()
#находим минимальное значение признака
min_non_setosa = plenght[~is_setosa].min()
print('Maximum of setosa: {0}.'.format(max_setosa))
print('Minimum of setosa: {0}.'.format(min_non_setosa))
#т.о. если длина лепестка меньше 2, то это Iris Setosa


###             ###
features = features[~is_setosa]
labels = labels[~is_setosa]
is_virginica = (labels == 'virginica')

def fit_model(features, labels):
    '''Learn a simple threshold model'''
    best_acc = -1.0
    # Loop over all the features:
    for fi in range(features.shape[1]):
        thresh = features[:, fi].copy()
        # test all feature values in order:
        thresh.sort()
        for t in thresh:
            pred = (features[:, fi] > t)

            # Measure the accuracy of this
            acc = (pred == labels).mean()

            rev_acc = (pred == ~labels).mean()
            if rev_acc > acc:
                acc = rev_acc
                reverse = True
            else:
                reverse = False
            if acc > best_acc:
                best_acc = acc
                best_fi = fi
                best_t = t
                best_reverse = reverse

    # A model is a threshold and an index
    return best_t, best_fi, best_reverse

best_t, best_fi, best_reverse = fit_model(features, is_virginica)
print(best_t)
print(best_fi)
print(best_reverse)