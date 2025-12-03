
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
    return {"len": len(tokens)}

def aggregate_features(features_list):
    total = 0
    for f in features_list:
        total += f["len"]
    return {"total_len": total}

def train_model(features):
    return {"model": "dummy"}

def evaluate_model(model, features):
    return {"accuracy": 0.9}

def log_metrics(metrics):
    print(metrics)

def save_model(model):
    log_metrics({"saved": True})

def process_record(record):
    tokens = tokenize(record)
    tokens = clean_text(tokens)
    tokens = remove_stopwords(tokens)
    tokens = stem_tokens(tokens)
    feats = compute_features(tokens)
    return feats

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
    log_metrics(metrics)
    save_model(model)

def main():
    run_pipeline()
