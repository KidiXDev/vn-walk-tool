# Seiya-Saiga VN Walkthrough URL Tool

A simple Python tool to fetch and search vn walkthrough URLs from [seiya-saiga.com](https://seiya-saiga.com).

## Features

- List all available vn walkthroughs
- Search for specific vn titles
- Save results to a text file

## Installation

1. Clone this repository
2. Install required dependencies:

```bash
pip install requests
```

## Usage

### List all vn and save to file

```bash
python walk.py -o
```

### Search for a specific vn

```bash
python walk.py -s "VN Title"
```

### Search and save result to file

```bash
python walk.py -s "VN Title" -o
```

## Options

- `-s`, `--search`: Search for a specific vn title
- `-o`, `--output`: Save results to output.txt
- `-h`, `--help`: Show help message

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
