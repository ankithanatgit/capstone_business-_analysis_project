import matplotlib.pyplot as plt

def plot_predictions(y_test, preds):
    plt.scatter(y_test, preds)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.savefig("reports/predictions_vs_actual.png")
    plt.close()
