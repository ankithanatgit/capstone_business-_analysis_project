from sklearn.metrics import r2_score, mean_squared_error

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    r2 = r2_score(y_test, preds)
    mse = mean_squared_error(y_test, preds)

    with open("reports/model_evaluation_report.md", "w") as f:
        f.write(f"R2 Score: {r2}\nMSE: {mse}")
