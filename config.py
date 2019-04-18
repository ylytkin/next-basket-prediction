from pathlib import Path

root_dir = Path(__file__).absolute().parent

data_dir = root_dir / 'data'

# raw data
raw_data_dir = data_dir / 'raw'
raw_data_zip_fpath = raw_data_dir / 'raiffeisen_data_anonymized.csv.zip'

# preprocessed data
x_train_fpath = data_dir / 'x_train.npy'
y_train_fpath = data_dir / 'y_train.npy'
x_test_fpath = data_dir / 'x_test.npy'
y_test_fpath = data_dir / 'y_test.npy'
mcc2id_fpath = data_dir / 'mcc2id.json'

# model
models_dir = root_dir / 'models'
models_dir.mkdir(exist_ok=True)

model_fpath = models_dir / 'model.hdf5'
