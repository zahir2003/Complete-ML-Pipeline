---

# ⚙️ End-to-End ML Project with Git & DVC Pipeline Integration

This repository demonstrates a complete **Machine Learning pipeline** built with **modular components**, integrated using **Git**, **DVC**, and **AWS S3** for reproducible experimentation, scalable data versioning, and automated pipelines.

---

## 🚀 Tools & Technologies

- Python 🐍
- Git & GitHub 🗂️
- DVC (Data Version Control) 🔁
- AWS S3 ☁️
- dvclive 📈
- VS Code 🧩

---

## 🧱 Project Structure

```

project/
├── .gitignore
├── dvc.yaml
├── params.yaml
├── src/
│   ├── Data\_injestion.py
│   ├── Feature\_Engineering.py
│   ├── Model\_Building.py
│   └── Model\_Evaluation.py
├── data/
├── models/
├── reports/
└── ...

````

---

## 🏗️ Building the Pipeline

### ✅ Step 1: Initialize Git Repository

```bash
git init
git remote add origin https://github.com/your-username/repo-name.git
````

### ✅ Step 2: Add Initial Structure

* Add `src/` folder with components like:

  * `Data_injestion.py`
  * `Feature_Engineering.py`
  * `Model_Building.py`
  * `Model_Evaluation.py`

### ✅ Step 3: Ignore Unnecessary Files

Update `.gitignore`:

```
data/
models/
reports/
```

### ✅ Step 4: Push to GitHub

```bash
git add .
git commit -m "Initial pipeline setup"
git push origin main
```

---

## 🌀 Setting Up DVC Pipeline (Without Params)

### ✅ Step 5: Create `dvc.yaml`

Manually or via `dvc stage add`.

### ✅ Step 6: Initialize & Reproduce

```bash
dvc init
dvc repro
dvc dag
```

> `dvc dag` visualizes the pipeline dependency graph.

### ✅ Step 7: Push with Git

```bash
git add .
git commit -m "Add initial DVC pipeline"
git push
```

---

## 🧠 Setting Up DVC Pipeline (With Params)

### ✅ Step 8: Create `params.yaml`

```yaml
Data_injestion:
  test_size: 0.2

Feature_Engineering:
  max_features: 1000

Model_Building:
  n_estimators: 100
  random_state: 42
```

### ✅ Step 9: Access Params in Code

```python
import yaml

def load_parmas(params_path: str) -> dict:
    with open(params_path, 'r') as file:
        return yaml.safe_load(file)

# Data Ingestion
params = load_parmas('params.yaml')
test_size = params['Data_injestion']['test_size']

# Feature Engineering
max_features = params['Feature_Engineering']['max_features']

# Model Building
n_estimators = params["Model_Building"]["n_estimators"]
random_state = params["Model_Building"]["random_state"]

model_params = {
    "n_estimators": n_estimators,
    "random_state": random_state
}
```

### ✅ Step 10: Run DVC Again

```bash
dvc repro
```

### ✅ Step 11: Git Commit

```bash
git add .
git commit -m "Integrate params.yaml with pipeline"
git push
```

---

## 🔬 Experiment Tracking with DVC

### ✅ Step 12: Install dvclive

```bash
pip install dvclive
```

### ✅ Step 13: Log Metrics and Params

In `Model_Evaluation.py`:

```python
from dvclive import Live

with Live(save_dvc_exp=True) as live:
    live.log_metric('accuracy', accuracy_score(y_test, y_pred))
    live.log_metric('precision', precision_score(y_test, y_pred))
    live.log_metric('recall', recall_score(y_test, y_pred))
    live.log_params(params)
```

### ✅ Step 14–18: Run & Track Experiments

```bash
dvc exp run
dvc exp show
# Optional
dvc exp apply <exp_name>
dvc exp remove <exp_name>
```

Change `params.yaml` and re-run to generate new experiments.

```bash
git add .
git commit -m "Tracked new DVC experiment"
git push
```

---

## ☁️ Adding AWS S3 Remote to DVC

### ✅ Step 19–21: AWS Setup

* Create IAM user
* Create S3 bucket with unique name

### ✅ Step 22–24: Install & Configure

```bash
pip install "dvc[s3]"
pip install awscli
aws configure
```

### ✅ Step 25: Add Remote Storage

```bash
dvc remote add -d dvcstore s3://your-bucket-name
```

### ✅ Step 26–27: Push to Remote + Git

```bash
dvc push
git add .
git commit -m "Push DVC data to S3"
git push
```

---

## ➕ Bonus: Add DVC Stage (Example)

```bash
dvc stage add -n Data_injestion -d src/Data_injestion.py -o data/raw python src/Data_injestion.py
```

---

## 🌐 Author

**Sk Mahiduzzaman**
📫 [Email](mailto:mohiduz03@gmail.com)
💼 [LinkedIn](https://www.linkedin.com/in/sk-mahiduzzaman)

---

## 💡 Key Highlights

* ✅ Modular ML codebase with pipeline stages
* ✅ DVC for reproducibility, tracking, and versioning
* ✅ Experimentation logged using dvclive
* ✅ Remote S3 integration for scalable storage
* ✅ Clean Git-based CI with tracked params and artifacts

> ⚡ *Make your ML pipelines robust, reproducible, and production-ready!*

