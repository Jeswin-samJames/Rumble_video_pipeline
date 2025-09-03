import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path

def run_notebook(notebook_path):
    print(f"Running notebook: {notebook_path}")
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": str(Path(notebook_path).parent)}})

def main():
    run_notebook("scripts/bronze.ipynb")
    run_notebook("scripts/silver.ipynb")
    run_notebook("scripts/gold.ipynb")
    print("All layers executed successfully!")

if __name__ == "__main__":
    main()
