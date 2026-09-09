import json
import os
import pandas as pd
from scipy.stats import entropy
from collections import Counter

DATA_FOLDER = "data" #folder where all json files are stored

results = []

for filename in os.listdir(DATA_FOLDER):
    if filename.endswith(".json"):
        filepath = os.path.join(DATA_FOLDER, filename)

        with open(filepath, "r") as f: #had a textfile that broke and needed to see what was happening
            content = f.read().strip()
            if not content:
                print(f"Files that are being skipped: {filename}")
                continue
            try:
                session = json.loads(content)
            except Exception as e:
                print(f"ERROR in {filename}: {e}")
                continue

        #extract meta data from the runs
        browser = session["meta"]["browser"]
        mode = session["meta"]["mode"]
        session_num = session["meta"]["session"]

        #visitorid from 10 runs
        visitor_ids = [run["visitorId"] for run in session["runs"]]

        #most common visitorId across the 10 runs
        majority_id = Counter(visitor_ids).most_common(1)[0][0]
    
        #to see how visitorId has changed, if it has
        unique_ids = list(set(visitor_ids))
        stable = len(unique_ids) == 1

        results.append({
            "browser": browser,
            "mode": mode,
            "session": session_num,
            "majority_visitor_id": majority_id,
            "within_session_stable": stable,
            "unique_ids_in_session": len(unique_ids)
        })

        #dataframe

df = pd.DataFrame(results)

print("=== Within Session Stability ===")
print(df.groupby(["browser","mode"])["within_session_stable"].all())

print("\n === Majority voted visitor IDs per session ===")
print(df[["browser","mode","session","majority_visitor_id"]])

print("\n === Cross session re-identification ===")
for(browser, mode), group in df.groupby(["browser","mode"]): 
    ids = group["majority_visitor_id"].tolist()
    unique = list(set(ids))
    majority_id = Counter(ids).most_common(1)[0][0]
    rate = (ids.count(ids[0])/len(ids)) * 100 # to get a %
    print(f"{browser}({mode}): {len(unique)} unique IDs across 10 sessions with a re-identification rate of: {rate:.0f}%")

print("\n === Shannon entropy per browser ===")
for(browser, mode), group in df.groupby(["browser", "mode"]):
    ids = group["majority_visitor_id"].tolist()
    counts = list(Counter(ids).values())
    probs = [c / sum(counts) for c in counts]
    h = entropy(probs, base = 2)
    print(f"{browser} {(mode)}: entropy = {h:4f} bits")

