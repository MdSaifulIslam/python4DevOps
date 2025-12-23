# Python for DevOps - Learning Journey

A comprehensive learning repository documenting my journey through Python programming with a focus on DevOps practices and automation.

## Overview

This repository contains hands-on examples, exercises, and practical implementations covering essential Python concepts and DevOps-specific skills. The content is structured to progressively build from Python fundamentals to advanced DevOps automation techniques.

## Project Structure

### 1. Python Fundamentals ([python-fundamentals/](python-fundamentals/))
Core Python concepts essential for DevOps automation:
- **Variables & Data Types**: Numbers, strings, type conversion
- **Collections**: Lists, tuples, sets, and dictionaries
- **Control Flow**: Conditionals, loops, and lazy iteration
- **Functions**: Regular functions, lambda functions, args/kwargs
- **List Comprehensions**: Efficient data transformations
- **Object-Oriented Programming**: Classes and object design

### 2. Error Handling ([error-handling/](error-handling/))
Robust error management for production-ready scripts:
- Built-in exceptions and custom exception classes
- Try-except-finally patterns
- Context managers for resource management
- Custom context manager implementation
- Exception raising and propagation

### 3. Interacting with OS ([interacting-with-os/](interacting-with-os/))
System-level operations for automation:
- Environment variables management
- Filesystem operations (create, read, update, delete)
- Subprocess execution and command-line integration
- Temporary files and directories
- Error handling in system operations

### 4. Files, Regex & Data Formats ([files-regex-data-formats/](files-regex-data-formats/))
Data manipulation and configuration management:
- File I/O operations (read/write modes)
- Filesystem path handling with `pathlib`
- Regular expressions for pattern matching
- CSV file processing
- JSON configuration handling
- YAML parsing (Docker Compose, Kubernetes configs)

### 5. HTTP Requests ([http-requests/](http-requests/))
API interactions and web automation:
- Making HTTP requests with `requests` and `httpx`
- Authentication methods (Basic, Bearer tokens, API keys)
- Error handling and status code management
- Retry strategies and timeout configuration
- REST API integration

### 6. Logging ([logging/](logging/))
Production-ready logging practices:
- Log levels and their usage
- File-based logging with rotation
- Structured logging with JSON format
- Declarative configuration
- Best practices for DevOps logging

### 7. Generators & Decorators ([generators-decorators/](generators-decorators/))
Advanced patterns for efficient code:
- Functions as first-class citizens
- Generator functions and lazy evaluation
- Return vs yield semantics
- Decorator fundamentals and patterns
- Decorators with arguments
- Stacking decorators
- `functools.wraps` for proper decorator implementation
- Lazy pipelines for large dataset processing

### 8. Type Hints ([typing/](typing/))
Type safety for maintainable codebases:
- Basic type annotations
- Common types (List, Dict, Optional, Union)
- TypedDict for structured dictionaries
- Generic types
- Type hints for generators and decorators
- Class type annotations

### 9. Automated Testing ([automated-testing/](automated-testing/))
Testing strategies using pytest:
- Test assertions and patterns
- Fixtures for test setup/teardown
- Test parametrization
- Test markers for organization
- Mocking fundamentals
- Advanced mocking techniques
- Conftest configuration

### 10. Multi-File Projects ([multi-file-projects/](multi-file-projects/))
Project organization and structure:
- Python modules and packages
- Subpackages organization
- Running scripts and entry points
- `pyproject.toml` configuration
- Adding and running tests

### 11. Virtual Environments ([virtual-envs/](virtual-envs/))
Dependency management and isolation:
- Virtual environment setup and activation
- Requirements management
- Package installation and version control

## Technologies & Libraries

Key dependencies used in this learning project:
- **HTTP Clients**: `requests`, `httpx`
- **Testing**: `pytest`, `pytest-mock`
- **Data Processing**: `beautifulsoup4`, `PyYAML`
- **Type Checking**: `mypy`
- **Environment Management**: `python-dotenv`
- **Development Tools**: `ipykernel`, `jupyterlab`
- **System Interaction**: `psutil`


1. Clone the repository:
```bash
git clone <repository-url>
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Examples

Most examples are in Jupyter notebook format (`.ipynb`) and can be run using:
```bash
jupyter lab
```
