#!/usr/bin/env python3

import yaml
import csv
from pathlib import Path
from rich.progress import Progress

YAML_INPUT = "yaml"
CSV_OUTPUT = "csv"

yaml_file_names = sorted(Path(YAML_INPUT).glob("*.yaml"))


def parse_yaml(progress: Progress, file_name: Path):
    data = None
    task = None
    columns = set()
    rows_to_write = list()
    with open(file_name) as file:
        data = yaml.safe_load(file)
        if data:
            out_file = Path(f"{CSV_OUTPUT}/{file_name.stem}.csv")
            task = progress.add_task(str(out_file), total=len(data) + 1)
            for item in data:
                columns = columns.union(set(item.keys()))
                rows_to_write.append({key: item[key] for key in columns if key in item})
                progress.advance(task)

            with open(out_file, "w", newline="") as csvfile:
                csv_writer = csv.DictWriter(csvfile, sorted(columns))
                csv_writer.writeheader()
                csv_writer.writerows(rows_to_write)
            progress.advance(task)


with Progress() as progress:
    for file_name in yaml_file_names:
        progress.console.print(f"Processing file {file_name}")
        parse_yaml(progress, file_name)
