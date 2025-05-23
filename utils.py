import csv
import re
from collections import Counter
from datetime import datetime
from colorama import Fore

def load_tickets(file='data/tickets.csv'):
    """
    Загружает данные билетов из CSV-файла.
    Возвращает список словарей или пустой список при ошибке.
    """
    data_tickets = []
    try:
        with open(file, 'r', encoding= 'utf-8') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
            except StopIteration:
                raise ValueError(f"Error: File '{file}' is empty.")

            seen_ids = set()
            for row in reader:
                if len(row) != 6:
                    print(Fore.YELLOW + f"Warning: Skipping row (expected 6 columns): {row}")
                    continue

                try:
                    ticket_id = int(row[0])
                    if ticket_id in seen_ids:
                        print(Fore.YELLOW + f"Warning: Duplicate order_id {ticket_id}")
                        continue
                    seen_ids.add(ticket_id)
                    ticket_date = datetime.strptime(row[5], '%Y-%m-%d').date()

                    data_tickets.append({
                        'ticket_id': ticket_id,
                        'client_name': row[1],
                        'subject': row[2],
                        'priority': row[3],
                        'status': row[4],
                        'date': ticket_date
                    })
                except ValueError as e:
                    print(Fore.YELLOW + f"Warning: Skipping row {row} — {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file}' not found.")
    return data_tickets


def get_tickets_count(tickets):
    return len(tickets)

def get_unique_clients(tickets):
    return len({t['client_name'] for t in tickets})

def get_status_count(tickets):
    return Counter(t['status'] for t in tickets)

def search_by_client_subject(tickets, query):
    """Ищет билеты по клиентам или теме."""
    query = query.lower()
    return [
        t for t in tickets
        if query in t['client_name'].lower() or query in t['subject'].lower()
    ]

def filter_publication_date(tickets, year_month):
    """Фильтрует билеты по году и месяцу (формат YYYY-MM)."""
    if not re.match(r'^\d{4}-\d{2}$', year_month):  # Строгая проверка формата
        return []

    try:
        year, month = map(int, year_month.split('-'))
        if not (1 <= month <= 12):
            return []
    except ValueError:
        return []

    return [
        t for t in tickets
        if t['date'].year == year and t['date'].month == month
    ]

def filter_priority(tickets, priority):
    priority = priority.lower()
    return [
        t for t in tickets
        if priority in t['priority'].lower()]