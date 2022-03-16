import pickle
from pathlib import Path
from pms.config import settings

_model = None

def get_model():
    global _model
    if _model is None:
        _model = pickle.loads(Path(settings.REC_MODEL_PATH).read_bytes())
    return _model

def recommend_best_practices(pest_type: str, context: dict) -> list[dict]:
    model = get_model()
    features = {"pest_type": pest_type, **context}
    # The demo model uses an OHE pipeline; simulate predict_proba if not trained
    if hasattr(model, "predict_proba"):
        try:
            preds = model.predict_proba([features])[0]  # type: ignore
            labels = getattr(model, "classes_", ["practice_a","practice_b","practice_c"])
            pairs = zip(labels, preds)
        except Exception:
            pairs = [("manual removal", 0.7), ("targeted spraying", 0.3)]
    else:
        pairs = [("manual removal", 0.7), ("targeted spraying", 0.3)]
    return [{"practice": p, "score": float(s)} for p, s in sorted(pairs, key=lambda x: -x[1])][:5]
