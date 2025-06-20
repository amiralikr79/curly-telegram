# Curly Telegram

This repository contains a simple command-line tool for viewing a personal financial snapshot.

## Setup

1. Ensure you have Python 3 installed.
2. Clone the repository or download the files.

## Usage

Run the script from the project root:

```bash
python financial_snapshot.py
```

By default it reads data from `data/sample_financial_data.json`. You can provide your own JSON file with the `-f` option:

```bash
python financial_snapshot.py -f path/to/your_data.json
```

The script will display totals for assets, liabilities, net worth, income, expenses, and cash flow.

## Data Format

The JSON file should contain keys for `accounts`, `income`, and `expenses` similar to the sample file in the `data/` folder.

