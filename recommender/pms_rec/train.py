import argparse, pickle
import pandas as pd
from pathlib import Path
from .model import build_pipeline, TARGET

DATA = [
    {"pest_type": "weed", "habitat": "riparian", "season": "spring", "practice": "manual removal"},
    {"pest_type": "insect", "habitat": "forest", "season": "summer", "practice": "targeted spraying"},
]

parser = argparse.ArgumentParser()
parser.add_argument("--no-train", action="store_true")
parser.add_argument("--out", default="pms_rec/artifacts/best_practices_pipeline.pkl")

def main(args=None):
    args = parser.parse_args(args=args)
    df = pd.DataFrame(DATA)
    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    pipe = build_pipeline()
    if not args.no_train:
        pipe.fit(X, y)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_bytes(pickle.dumps(pipe))

if __name__ == "__main__":
    main()
