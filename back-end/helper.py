import click
import re

def parse_time_estimate(input_str):
    input_str = input_str.strip().lower()

    # Handle minutes (e.g., 5m, 30m)
    if input_str.endswith("m"):
        try:
            minutes = float(input_str[:-1])
            return round(minutes / 60, 2)
        except ValueError:
            raise ValueError("Invalid minute format. Use '5m', '30m', etc.")

    # Handle hours (e.g., 1h, 1.5h)
    if input_str.endswith("h"):
        try:
            hours = float(input_str[:-1])
            return round(hours, 2)
        except ValueError:
            raise ValueError("Invalid hour format. Use '1h', '1.5h', etc.")

    # Fallback: allow just numbers (assumed to be hours)
    try:
        return round(float(input_str), 2)
    except ValueError:
        raise ValueError("Invalid time format. Use '1h', '90m', or '1.5'.")

def prompt_estimate_rounded():
    raw = click.prompt("Enter time estimate (e.g., 1h, 30m, 0.25)")
    try:
        parsed = parse_time_estimate(raw)
        rounded = round(parsed * 4) / 4  # round to nearest 0.25
        return rounded
    except ValueError:
        click.echo("Invalid time format. Use '1h', '30m', or '0.25'")
        return prompt_estimate_rounded()
def prompt_estimate_rounded():
    raw = click.prompt("Enter time estimate (e.g., 1.5 or 90m or 1:15)")
    try:
        parsed = parse_time_estimate(raw)
        rounded = round(parsed * 4) / 4  # round to nearest 0.25
        return rounded
    except ValueError:
        click.echo("Invalid time format. Try something like 1.5, 90m, or 1:15")
        return prompt_estimate_rounded()