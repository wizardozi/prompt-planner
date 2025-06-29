import click
import re

def parse_time_estimate(input_str):
    input_str = input_str.strip().lower()

    # HH:MM format
    if ':' in input_str:
        try:
            hours, minutes = map(int, input_str.split(':'))
            return round(hours + minutes / 60, 2)
        except:
            raise ValueError("Invalid time format. Use '1.5', '1h', '90m', or '1:30'.")

    # 90m format
    if 'm' in input_str:
        minutes = int(re.sub(r'[^\d]', '', input_str))
        return round(minutes / 60, 2)

    # 1h or plain decimal
    input_str = re.sub(r'[^\d\.]', '', input_str)
    return round(float(input_str), 2)

def prompt_estimate_rounded():
    raw = click.prompt("Enter time estimate (e.g., 1.5 or 90m or 1:15)")
    try:
        parsed = parse_time_estimate(raw)
        rounded = round(parsed * 4) / 4  # round to nearest 0.25
        return rounded
    except ValueError:
        click.echo("Invalid time format. Try something like 1.5, 90m, or 1:15")
        return prompt_estimate_rounded()