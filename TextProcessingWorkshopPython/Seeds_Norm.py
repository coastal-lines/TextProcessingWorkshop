import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def load_dataset(dataset_name):
    '''
    data,labels = load_dataset(dataset_name)
    Load a given dataset
    Returns
    -------
    data : numpy ndarray
    labels : list of str
    '''
    data = []
    labels = []
    with open('C:\Temp\!my\Luis\seeds.tsv'.format(dataset_name)) as ifile:
        for line in ifile:
            tokens = line.strip().split('\t')
            data.append([float(tk) for tk in tokens[:-1]])
            labels.append(tokens[-1])
    data = np.array(data)
    labels = np.array(labels)
    return data, labels

#загружаем признаки и метки
features, labels = load_dataset('seeds')
#создаем классификатор с числом соседей = 1
classifier = KNeighborsClassifier(n_neighbors=1)
classifier = Pipeline([('norm', StandardScaler()), ('knn', classifier)])
#создаем кроссвалидацию из 5 групп
kf = KFold(n_splits=5, shuffle=True)

#массив для значений оценок моделей
means = []
#для каждой из 5 групп проводим обучение и тестирование модели
for training,testing in kf.split(features):
    # We learn a model for this fold with `fit` and then apply it to the
    #обучаем модель
    classifier.fit(features[training], labels[training])

    # testing data with `predict`:
    #тестируем модель
    prediction = classifier.predict(features[testing])

    # np.mean on an array of booleans returns the fraction of correct decisions
    # for this fold:
    curmean = np.mean(prediction == labels[testing])
    means.append(curmean)
print('Result of cross-validation using KFold: {:.1%}'.format(np.mean(means)))