import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score

def main():
    train_df = pd.read_csv("./train.tsv", sep='\t', header=None)
    std_scaler = StandardScaler()
    scaled_train_data = std_scaler.fit_transform(train_df)

    X_train = scaled_train_data[:, 0:-1]  # select columns 1 through end
    y_train = scaled_train_data[:, -1]   # select column 0, the stock price

    pca = PCA()
    pca.fit(X_train, y_train)
    print(pca.components_)
    print(pca.explained_variance_)
    return

    model = LinearRegression()
    model.fit(X_train, y_train)

    test_df = pd.read_csv("./test.tsv", sep='\t', header=None)
    test_data = test_df.to_numpy()
    X_test = test_data[:, 0:-1]  # select columns 1 through end
    y_predicted = model.predict(X_test)

if __name__ == "__main__":
    main()
