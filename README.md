# Ticket Analyzer CLI

A command-line application for analyzing customer support tickets from a CSV file.

## Features

- Load and validate ticket data from `data/tickets.csv`
- Show total ticket count
- Count unique clients
- Display ticket status distribution
- Search by client name or subject
- Filter tickets by date (month/year)
- Filter tickets by priority (e.g., high, medium, low)
- Colored CLI output using `colorama`
- Error handling and warnings for bad data

## CSV Format

Your `tickets.csv` should have the following columns:

```csv
ticket_id,client_name,subject,priority,status,date
1,John Smith,Login issue,High,Open,2024-04-01
2,Sarah Connor,Payment delay,Medium,Closed,2024-04-03
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name
   cd your-repo-name
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Requirements

- Python 3.8+
- colorama

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

## Author

Created by CraftSher – Freelance Python Developer
