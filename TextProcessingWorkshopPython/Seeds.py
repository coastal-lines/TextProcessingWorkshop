import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold

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

features, labels = load_dataset('seeds')
classifier = KNeighborsClassifier(n_neighbors=1)
kf = KFold(n_splits=5, shuffle=True)


means = []
for training,testing in kf.split(features):
    # We learn a model for this fold with `fit` and then apply it to the
    # testing data with `predict`:
    classifier.fit(features[training], labels[training])
    prediction = classifier.predict(features[testing])

    # np.mean on an array of booleans returns the fraction of correct decisions
    # for this fold:
    curmean = np.mean(prediction == labels[testing])
    means.append(curmean)
print('Result of cross-validation using KFold: {:.1%}'.format(np.mean(means)))