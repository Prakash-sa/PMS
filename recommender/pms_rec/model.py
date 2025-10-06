from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

CATEGORICAL = ["pest_type", "habitat", "season"]
TARGET = "practice"

def build_pipeline():
    pre = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL)
    ])
    clf = LogisticRegression(max_iter=500)
    return Pipeline(steps=[("pre", pre), ("clf", clf)])
