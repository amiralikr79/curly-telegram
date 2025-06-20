import json
import argparse


def load_data(path):
    with open(path) as f:
        return json.load(f)


def summarize(data):
    assets_total = sum(acc["balance"] for acc in data.get("accounts", []) if acc.get("type") == "asset")
    liabilities_total = sum(acc["balance"] for acc in data.get("accounts", []) if acc.get("type") == "liability")
    net_worth = assets_total - liabilities_total

    income_total = sum(item["amount"] for item in data.get("income", []))
    expenses_total = sum(item["amount"] for item in data.get("expenses", []))
    cash_flow = income_total - expenses_total

    return {
        "assets": assets_total,
        "liabilities": liabilities_total,
        "net_worth": net_worth,
        "income": income_total,
        "expenses": expenses_total,
        "cash_flow": cash_flow,
    }


def display_summary(summary):
    print("===== Financial Snapshot =====")
    print(f"Total Assets:     ${summary['assets']:.2f}")
    print(f"Total Liabilities:${summary['liabilities']:.2f}")
    print(f"Net Worth:        ${summary['net_worth']:.2f}\n")
    print(f"Monthly Income:   ${summary['income']:.2f}")
    print(f"Monthly Expenses: ${summary['expenses']:.2f}")
    print(f"Monthly Cash Flow:${summary['cash_flow']:.2f}")
    print("==============================")


def main():
    parser = argparse.ArgumentParser(description="Simple financial snapshot")
    parser.add_argument(
        "-f",
        "--file",
        default="data/sample_financial_data.json",
        help="Path to financial data JSON",
    )
    args = parser.parse_args()

    data = load_data(args.file)
    summary = summarize(data)
    display_summary(summary)


if __name__ == "__main__":
    main()
