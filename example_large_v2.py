
def load_csv():
    data = []
    return data

def parse_row(row):
    return row.strip().split(",")

def clean_text(tokens):
    return [t.lower() for t in tokens]

def tokenize(record):
    return record.split()

def remove_stopwords(tokens):
    return [t for t in tokens if len(t) > 2]

def stem_tokens(tokens):
    return [t[:-1] if len(t) > 4 else t for t in tokens]

def compute_features(tokens):
    return {"len": len(tokens), "unique": len(set(tokens))}

def aggregate_features(features_list):
    total = 0
    uniq = 0
    for f in features_list:
        total += f["len"]
        uniq += f["unique"]
    return {"total_len": total, "total_unique": uniq}

def train_model(features):
    model = {"model": "dummy"}
    log_debug("training", features)
    return model

def evaluate_model(model, features):
    scores = compute_scores(features)
    log_debug("scores", scores)
    return {"accuracy": scores["acc"]}

def compute_scores(features):
    return {"acc": 0.9, "f1": 0.8}

def log_metrics(metrics):
    log_debug("metrics", metrics)
    print(metrics)

def log_debug(tag, payload):
    msg = f"[{tag}] {payload}"
    print(msg)

def save_model(model):
    log_metrics({"saved": True})
    log_debug("model_saved", model)

def process_record(record):
    tokens = tokenize(record)
    tokens = clean_text(tokens)
    tokens = remove_stopwords(tokens)
    tokens = stem_tokens(tokens)
    feats = compute_features(tokens)
    return feats

def summarize_results(metrics):
    log_debug("summary", metrics)
    log_metrics({"summary": True})

def run_pipeline():
    data = load_csv()
    feats_list = []
    for row in data:
        parsed = parse_row(row)
        for rec in parsed:
            feats = process_record(rec)
            feats_list.append(feats)
    agg = aggregate_features(feats_list)
    model = train_model(agg)
    metrics = evaluate_model(model, agg)
    summarize_results(metrics)
    log_metrics(metrics)
    save_model(model)

def main():
    run_pipeline()
