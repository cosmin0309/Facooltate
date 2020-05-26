import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
from sklearn import svm
from sklearn import metrics
from sklearn import datasets
from sklearn.metrics import f1_score, classification_report
import pdb
import csv
import io
import tensorflow as tf
import seaborn as sn
from sklearn.metrics import confusion_matrix
import librosa
import pickle

print("Runnin'")


def normalize_data(train_data, test_data, type=None):
    #print("lennntraining:", len(train_data))

    #print("lennntest:", len(test_data))
    scaler = None
    if type == 'standard':
        scaler = preprocessing.StandardScaler()

    elif type == 'min_max':
        scaler = preprocessing.MinMaxScaler()

    elif type == 'l1':
        scaler = preprocessing.Normalizer(norm='l1')

    elif type == 'l2':
        scaler = preprocessing.Normalizer(norm='l2')

    if scaler is not None:
        scaler.fit(train_data)
        scaled_train_data = scaler.transform(train_data)
        scaled_test_data = scaler.transform(test_data)
        return (scaled_train_data, scaled_test_data)
    else:
        print("No scaling was performed. Raw data is returned.")
        return (train_data, test_data)


def compute_accuracy(gt_labels, predicted_labels):
    accuracy = np.sum(predicted_labels == gt_labels) / len(predicted_labels)
    return accuracy


def load_y_validation():
    y_valid = []
    data = pd.read_csv('validation.txt', header=None, usecols=[1])
    # print(data)
    for i in range(len(data)):
        #   print(i)
        y_valid.append(data[1][i])
    return y_valid


if __name__ == "__main__":

    data = pd.read_csv('train.txt', header=None, usecols=[0])
    audio_files = []

    x_train = []

    """"
    for i in range(len(data)):
        print(i)
        path = 'train/train/'
        # wave_file_name=100001 + i
        path = path + data[0][i]

        audio_time_series, sampling_rates = librosa.load(path)
        audio = librosa.feature.mfcc(n_mfcc=20,y=audio_time_series, sr=sampling_rates)
        #print("audio = ", audio)
        a = list([np.mean(i) for i in audio])
        #print("a = ",a)
        x_train.append(a)
        #print("xtrain before array",x_train)
    
    x_train = np.array(x_train)
    np.save("mfcc", x_train)
    """
    x_train = np.load('mfcc.npy')
    # print("x_train = ", x_train)

    data = pd.read_csv('validation.txt', header=None, usecols=[0])
    x_validation = []
    """
    for i in range(len(data)):
        print(i)
        path = 'validation/validation/'
        # wave_file_name=100001 + i
        path = path + data[0][i]

        audio_time_series, sampling_rates = librosa.load(path)
        audio = librosa.feature.mfcc(n_mfcc=20, y=audio_time_series, sr=sampling_rates)
        # print(type(audio))
        a = list([np.mean(i) for i in audio])
        x_validation.append(a)

    x_validation = np.array(x_validation)
    np.save("validation", x_validation)
    """
    x_validation = np.load("validation.npy")
    # audio_files.append(audio(data[0][i], audio))

    data = pd.read_csv('test.txt', header=None, usecols=[0])
    x_test = []
    """
    for i in range(len(data)):
        print(i)
        path = 'test/test/'
        # wave_file_name=100001 + i
        path = path + data[0][i]

        audio_time_series, sampling_rates = librosa.load(path)
        audio = librosa.feature.mfcc(n_mfcc=20, y=audio_time_series, sr=sampling_rates)
        # print(type(audio))
        a = list([np.mean(i) for i in audio])
        x_test.append(a)
    """
    # x_test = np.array(x_test)
    # np.save("test", x_test)

    x_test = np.load("test.npy")
    # audio_files.append(audio(data[0][i], audio))


    # x_train = np.load("audio.npy")
    y_train = np.load("masks.npy")
    # print(x_train)
    # x_test = np.load("audio_test.npy")

    # x_validation = np.load("audio_validation.npy")
    y_validaiton = np.load("y_validation.npy")
    #print("y_validation = ", y_validaiton)

    x_train2 = []
    x_test2 = []
    x_validation2 = []
    a = list([np.mean(i) for i in x_train])
    x_train2 += a
    x_train2 = np.array(x_train2)
    b = list([np.mean(i) for i in x_test])
    x_test2 += b
    x_test2 = np.array(x_test2)
    c = list([np.mean(i) for i in x_validation])
    x_validation2 += c
    x_validation2 = np.array(x_validation2)

    # print(x, '\n\n', y)
    # x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.4)

    scaled_training_data, scaled_test_data = normalize_data(x_train, x_test, type='l2')

    # print("x_train2 = ", x_train,'\n', "y_train = ", y_train)
    # y_validation = load_y_validation()
    # y_validation = np.array(y_validation)
    # np.save("y_validation", y_validation)
    # print("y_validation = ", y_validation)
    classes = ['mask_on' 'mask_off']
    y_train = np.load("masks.npy")
    # print("y_train = ", y_train)
    print("here")
    """
    #print(x_train2.shape, y_train.shape)
    clf = svm.SVC(C=100, kernel='linear')
    #print(scaled_training_data)
    print("here2")
    #x_train = fit_transform()
    #clf.transform(x_test)
    #clf.fit(x_train, y_train)
    clf.fit(scaled_training_data, y_train)
    with open("csvmodel.pickle", "wb") as f:
        pickle.dump(clf, f)
    """
    pickle_in = open("csvmodel.pickle", "rb")
    clf = pickle.load(pickle_in)

    print("here3")
    # y_pred = clf.predict(x_test)
    # print(len(scaled_test_data))
    y_pred = clf.predict(scaled_test_data)
    # print(y_pred)
    print("here4")
    data = np.genfromtxt(r'test.txt', encoding='utf-8', dtype=None, delimiter='\t', names=('col1', 'col2'),
                         comments=None)

    for i in range(len(y_pred)):
        print(str(data[i]) + "," + str(y_pred[i]))
    # acc = metrics.accuracy_score(y_test, y_pred)

    print(clf.score(x_test, y_pred))

    print("ACC:")
    # print(compute_accuracy(np.asarray(y_validation), y_pred))
    # print(len(y_pred))
    # print(str(data[3]))


    with open('rezultatuk.csv', 'w', newline='') as f:
        fieldnames = ['id', 'label']
        f = csv.DictWriter(f, fieldnames=fieldnames)

        f.writeheader()

        for i in range(0, len(y_pred)):
            f.writerow({'id': data[i], 'label': y_pred[i]})

    print("ACC:")
    # print(compute_accuracy(np.asarray(y_), y_pred))
    print(classification_report(clf.predict(x_validation), y_validaiton))
    # print('f1 score', f1_score(np.asarray(y_validaiton), y_pred))

    # print(confusion_matrix(np.asarray(y_validaiton), y_pred))

    """
    confusion_matrix(np.asarray(y_validation), y_pred)



    bz = confusion_matrix(np.asarray(y_validation), y_pred)
    plt.figure(figsize = (10,7))
    sn.heatmap(bz, annot = True)
    plt.xlabel('Predicted')
    plt.ylabel('Correct')
    plt.show()"""
