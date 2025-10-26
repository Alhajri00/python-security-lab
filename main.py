import yaml

with open("config.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

for k, v in data.items():
    print(f"{k}: {v}")
