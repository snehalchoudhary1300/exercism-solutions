
"""Format ledger entries for American and Dutch locales."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class LedgerEntry:
    """Store the date, description, and amount of a ledger entry."""

    date: datetime
    description: str
    change: int


def create_entry(date, description, change):
    """Create a ledger entry from the supplied values."""
    return LedgerEntry(
        date=datetime.strptime(date, "%Y-%m-%d"),
        description=description,
        change=change,
    )


def format_entries(currency, locale, entries):
    """Format and return all ledger entries as a string."""
    if locale == "en_US":
        header = "Date       | Description               | Change       "
    else:
        header = "Datum      | Omschrijving              | Verandering  "

    sorted_entries = sorted(
        entries,
        key=lambda entry: (
            entry.date,
            entry.change,
            entry.description,
        ),
    )

    formatted_rows = [
        format_entry(entry, currency, locale)
        for entry in sorted_entries
    ]

    return "\n".join([header] + formatted_rows)


def format_entry(entry, currency, locale):
    """Format one ledger entry."""
    date_string = format_date(entry.date, locale)
    description = format_description(entry.description)
    amount = format_amount(entry.change, currency, locale)

    return f"{date_string} | {description} | {amount}"


def format_date(entry_date, locale):
    """Format the date according to the selected locale."""
    if locale == "en_US":
        return entry_date.strftime("%m/%d/%Y")

    return entry_date.strftime("%d-%m-%Y")


def format_description(description):
    """Truncate long descriptions and pad them to 25 characters."""
    if len(description) > 25:
        return description[:22] + "..."

    return f"{description:<25}"


def format_amount(change, currency, locale):
    """Format the amount according to currency and locale."""
    symbol = "$" if currency == "USD" else "€"
    absolute_change = abs(change)
    whole_units = absolute_change // 100
    cents = absolute_change % 100

    if locale == "en_US":
        number = f"{whole_units:,}.{cents:02d}"
        amount = (
            f"({symbol}{number})"
            if change < 0
            else f"{symbol}{number} "
        )
    else:
        number = f"{whole_units:,}.{cents:02d}"
        number = (
            number.replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
        sign = "-" if change < 0 else ""
        amount = f"{symbol} {sign}{number} "

    return f"{amount:>13}"
