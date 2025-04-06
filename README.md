# OHCE Kata

## Description

OHCE (reversed echo) is a programming kata that implements a console application with specific behaviors:

- Reverses the text you input
- Detects palindromes and responds with "¡Bonita palabra!" (Beautiful word!)
- Greets you differently based on the time of day
- Ends when you type "Stop!"

This implementation has been rigorously developed following the Test-Driven Development (TDD) methodology in Python, where each functionality has gone through the three phases: Red (failing test), Green (minimal code to pass), and Refactor (code improvement).

## Requirements

- Python 3.6 or higher
- Pytest

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd ohce_kata
```

### 2. Create and activate a virtual environment (recommended)

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the tests

To run all project tests:

```bash
python -m pytest
```

To run tests with verbose details:

```bash
python -m pytest -v
```

To run a specific test file:

```bash
python -m pytest tests/test_ohce.py
```

To run a specific test:

```bash
python -m pytest tests/test_ohce.py::test_palindrome_detection
```

## Running the application

```bash
python -m main
```

## Features

### 1. Text reversal

The application reverses the text you enter:

```
> hola
aloh
```

### 2. Palindrome detection

When you enter a palindrome, the application recognizes it:

```
> oto
oto
¡Bonita palabra!
```

### 3. Time-based greetings

The application greets you differently based on the time of day:

- Morning (6-12h): "¡Buenos días \<name\>!"
- Afternoon (12-20h): "¡Buenas tardes \<name\>!"
- Night (20-6h): "¡Buenas noches \<name\>!"

### 4. Stop command

To end the application, type "Stop!":

```
> Stop!
Adios <name>
```

## Development approach (TDD)

This project has been developed strictly following the TDD methodology:

1. **Red**: Write a failing test for the new functionality
2. **Green**: Implement the minimal code necessary to make the test pass
3. **Refactor**: Improve the code while keeping the tests green

Each commit in the repository history corresponds to a specific phase of the TDD cycle, allowing you to follow the development step by step.

## Project structure

```
ohce_kata/
├── __init__.py      # Makes the directory a Python package
├── ohce.py          # Main implementation of the Ohce class
├── main.py          # Main script for user interaction
├── tests/           # Tests directory
│   ├── __init__.py  # Makes tests a package
│   ├── test_ohce.py # Tests for the Ohce class
│   └── test_main.py # Tests for the main script
├── requirements.txt # Project dependencies
└── README.md        # This file
```

## Patterns and best practices used

- **Test Doubles**: Mock objects (like MockClock) are used to control dependencies in tests
- **Dependency Injection**: The clock is injected to facilitate testing
- **Comprehensive docstrings**: Detailed documentation of classes and methods
- **Encapsulation**: Private attributes with "\_" prefix
- **Constants**: Use of constants for significant values
