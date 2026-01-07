import matplotlib.pyplot as plt

def basic_eda(df):
    print(df.describe())

    df.hist(figsize=(10,8))
    plt.tight_layout()
    plt.savefig("reports/eda_visuals.png")
    plt.close()
