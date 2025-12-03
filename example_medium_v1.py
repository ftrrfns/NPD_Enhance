
def load_data():
    records = []
    for i in range(10):
        records.append(i)
    return records

def filter_data(data):
    result = []
    for item in data:
        if item % 2 == 0:
            result.append(item)
    return result

def normalize(data):
    total = sum(data) if data else 1
    return [x / total for x in data]

def compute_stats(data):
    if not data:
        return {"mean": 0, "max": 0}
    mean = sum(data) / len(data)
    mx = max(data)
    return {"mean": mean, "max": mx}

def log_info(stats):
    msg = f"mean={stats['mean']}, max={stats['max']}"
    print(msg)

def save_results(stats):
    log_info(stats)

def preprocess():
    data = load_data()
    filtered = filter_data(data)
    norm = normalize(filtered)
    return norm

def analyze():
    data = preprocess()
    stats = compute_stats(data)
    save_results(stats)

def main():
    analyze()
