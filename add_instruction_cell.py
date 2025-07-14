import json, sys
cell_text = [
    "## Additional Learning Resources",
    "Refer to [scikit-learn documentation](https://scikit-learn.org/stable/) and the [Pandas user guide](https://pandas.pydata.org/docs/) for detailed explanations of the functions used in this notebook.",
    "For a quick refresher on splitting data:",
    "```python\nfrom sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n```"
]

for path in sys.argv[1:]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    new_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + '\n' for line in cell_text]
    }
    data['cells'].insert(0, new_cell)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1)
