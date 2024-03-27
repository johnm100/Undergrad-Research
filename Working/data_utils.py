import pandas as pd
import numpy as np
import pickle
import os
from keras.utils import to_categorical

def convert_to_pickle_file(path, image_files, feature_files, label_files, event_files, class_dict, output_file):
    x_img = np.genfromtxt(path+f'{image_files[0]}', delimiter=',')[0:-1,0:-1].astype('float32').reshape(-1,5,5,1)
    x_fea = np.genfromtxt(path+f'{feature_files[0]}', delimiter=',')[0:-1,:].astype('float32')
    y_lab = to_categorical(np.genfromtxt(path + f'{label_files[0]}', delimiter=',')[0:-1], num_classes=2)
    x_evt = np.genfromtxt(path+f'{event_files[0]}', delimiter=',')[0:-1].astype('int32')

    gev_str = image_files[0].split('_')[2]
    gev_str = gev_str.split('gev')[0]
    gev_range = [gev_str for i in range(len(x_evt))]
    y_lab_str = []
    for i in range(len(x_evt)):
        for key, value in class_dict.items():
                if np.array_equal(y_lab[i], value):
                    y_lab_str.append(key)
                    break

    for i in range(1, len(image_files)):
        x_img2 = np.genfromtxt(path+f'{image_files[i]}', delimiter=',')[0:-1,0:-1].astype('float32').reshape(-1,5,5,1)
        x_fea2 = np.genfromtxt(path+f'{feature_files[i]}', delimiter=',')[0:-1,:].astype('float32')
        y_lab2 = to_categorical(np.genfromtxt(path + f'{label_files[i]}', delimiter=',')[0:-1], num_classes=2)
        x_evt2 = np.genfromtxt(path+f'{event_files[i]}', delimiter=',')[0:-1].astype('int32')
        gev_str = image_files[i].split('_')[2]
        gev_str = gev_str.split('gev')[0]
        gev_range2 = [gev_str for i in range(len(x_evt2))]
        y_lab_str2 = []
        for i in range(len(x_evt2)):
            for key, value in class_dict.items():
                if np.array_equal(y_lab2[i], value):
                    y_lab_str2.append(key)
                    break

        x_img = np.concatenate((x_img, x_img2))
        x_fea = np.concatenate((x_fea, x_fea2))
        y_lab = np.concatenate((y_lab, y_lab2))
        x_evt = np.concatenate((x_evt, x_evt2))
        gev_range = np.concatenate((gev_range, gev_range2))
        y_lab_str = np.concatenate((y_lab_str, y_lab_str2))
    
    labels = ['Momentum Range (GeV)','Event ID',
               'Class Name', 'One-Hot Label',
               'Energy (GeV)', 'Phi', 'Eta', 'C2', 'C3', 'C4', 'Probability',
                 'Image (5x5)']
    index = np.arange(0, len(x_evt), 1)

    # create a DataFrame
    df = pd.DataFrame(list(zip(gev_range, x_evt, y_lab_str, y_lab, 
                               x_fea[:,0], x_fea[:,1], x_fea[:,2], x_fea[:,3], x_fea[:,4], x_fea[:,5], x_fea[:,6],
                                 x_img)), columns =labels, index=index)
    df.head()

    # save to pickle
    df.to_pickle(output_file)

def load_pickle_file(file):
    df = pd.read_pickle(file)
    return df

def create_config_file(config_file, path):
    config_dict = {
        'path' :str(path),
        'class_dict' : {'Merged': [0,1], 'Isolated': [1,0]},
        'image_files': ['fimg_pi0_10-15gev.csv', 'fimg_pi0_20-25gev_1.csv'],
        'feature_files': ['ffea_pi0_10-15gev.csv', 'ffea_pi0_20-25gev_1.csv'],
        'label_files': ['fcls_pi0_10-15gev.csv', 'fcls_pi0_20-25gev_1.csv'],
        'event_files': ['fevt_pi0_10-15gev.csv', 'fevt_pi0_20-25gev_1.csv'],
        'data_file': str(path)+'all_data.pkl'
    }

    with open(config_file, 'wb') as f:
        pickle.dump(config_dict, f)

def convert_to_np_array(df):
    x_img = np.array(df['Image (5x5)'].tolist())
    x_fea = np.array(df[['Energy (GeV)', 'Phi', 'Eta', 'C2', 'C3', 'C4', 'Probability']].values)
    y_lab = np.array(df['One-Hot Label'].tolist())
    y_lab_str = np.array(df['Class Name'].tolist())
    return x_img, x_fea, y_lab, y_lab_str

def get_class_dict():

    current_dir = os.getcwd()
    config_file_path = os.path.join(current_dir, "configs/config.pkl")
    if not os.path.exists(config_file_path):
        create_config_file(config_file_path, current_dir)

    config = pickle.load(open(config_file_path, 'rb'))
    return config['class_dict']

def load_data_frame():
    
    # get current directory
    current_dir = os.getcwd()

    data_path = os.path.join(current_dir, "data/")
    print("Data path: ", data_path)
    if not os.path.exists(data_path):
        # exit 
        print("Data path does not exist")
        return None

    config_file_path = os.path.join(current_dir, "configs/config.pkl")
    
    create_config_file(config_file_path, data_path)
    
    config = pickle.load(open(config_file_path, 'rb'))

    convert_to_pickle_file(path = str(data_path),
                                image_files = config['image_files'],
                                feature_files = config['feature_files'],
                                label_files = config['label_files'],
                                event_files = config['event_files'],
                                class_dict = config['class_dict'],
                                output_file = config['data_file'])

    df = load_pickle_file(config['data_file'])
    return df