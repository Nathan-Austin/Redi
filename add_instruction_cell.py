import json, sys

cell_text = [
    "## Additional Learning Resources",
    "Refer to [scikit-learn documentation](https://scikit-learn.org/stable/) and the [Pandas user guide](https://pandas.pydata.org/docs/) for detailed explanations of the functions used in this notebook.",
    "For a quick refresher on splitting data:",
    "```python\nfrom sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n```",
]

practice_comment = "# Practice: implement the steps discussed above\n"

for path in sys.argv[1:]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Check if an Additional Learning Resources cell already exists
    existing_idx = next(
        (i for i, c in enumerate(data.get("cells", []))
         if c.get("cell_type") == "markdown" and "Additional Learning Resources" in "".join(c.get("source", ""))),
        None
    )

    insert_idx = 1 if (
        data.get("cells") and
        data["cells"][0].get("cell_type") == "markdown" and
        data["cells"][0].get("source", [""])[0].lstrip().startswith("#")
    ) else 0

    if existing_idx is None:
        # Insert a new Additional Learning Resources cell
        new_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in cell_text],
        }
        data["cells"].insert(insert_idx, new_cell)
    else:
        # Move existing resources cell to correct position
        if existing_idx != insert_idx:
            cell = data["cells"].pop(existing_idx)
            data["cells"].insert(insert_idx, cell)

    # Replace empty code cells with practice prompt
    for cell in data.get("cells", []):
        if cell.get("cell_type") == "code" and not "".join(cell.get("source", [])).strip():
            cell["source"] = [practice_comment]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1)

