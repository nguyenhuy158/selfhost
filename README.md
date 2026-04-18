# selfhost

`selfhost` is a CLI tool that lists useful tools from your public GitHub repositories, presenting them in a clean, formatted table.

## How it Works

`selfhost` fetches your public GitHub repositories and identifies "tools" based on the following criteria:

1.  **Language/Topic**: The repository's primary language must be **Python** OR it must have a **python** topic.
2.  **Not a Fork**: Only original repositories are listed.
3.  **Description**: The repository must have a description set on GitHub.

## Installation

```bash
pip install .
```

## Usage

```bash
selfhost
```

To see the version:

```bash
selfhost --version
```
