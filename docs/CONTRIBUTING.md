# Contributing to Amazon Web Scraping Project

First off, thank you for considering contributing to this project! This document provides guidelines and steps for contributing.

---

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

---

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report:

1. Check if the issue already exists in the [Issues](https://github.com/ArkanTsabit123/Amazon-Web-Scrapping/issues)
2. Make sure you are using the latest version
3. Collect information about the bug:
   - Error messages
   - Python version
   - Operating system
   - Steps to reproduce

When creating a bug report, include:

- **Title**: Clear and descriptive
- **Description**: What happened and what you expected
- **Steps to Reproduce**: Step-by-step instructions
- **Screenshots**: If applicable
- **Environment**: Python version, OS, dependencies

### Suggesting Enhancements

Feature requests are welcome! When suggesting an enhancement:

1. Check if the feature already exists or is planned
2. Describe the feature clearly
3. Explain why it would be useful
4. Provide examples if possible

### Pull Requests

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

---

## Development Setup

### Prerequisites

```bash
Python 3.9+
Git
```

### Setup Steps

```bash
# Clone the repository
git clone https://github.com/ArkanTsabit123/Amazon-Web-Scrapping.git
cd Amazon-Web-Scrapping

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Coding Standards

### Python Style Guide

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines:

- Use 4 spaces for indentation
- Maximum line length: 79 characters for code, 72 for docstrings
- Use descriptive variable names
- Add docstrings to all functions

### Example

```python
def extract_product_title(soup):
    """
    Extract product title from BeautifulSoup object.

    Args:
        soup (BeautifulSoup): Parsed HTML object

    Returns:
        str: Product title or empty string if not found
    """
    try:
        title = soup.find("span", attrs={"id": "productTitle"})
        return title.text.strip() if title else ""
    except AttributeError:
        return ""
```

### Jupyter Notebook Standards

- Include markdown cells explaining each section
- Keep code cells focused and well-organized
- Add comments for complex logic
- Test all cells before submitting

---

## Testing Guidelines

### Manual Testing

Before submitting changes:

1. Run the scraper with a test URL
2. Verify data is extracted correctly
3. Check CSV output format
4. Ensure no errors occur

### Test Commands

```bash
# Run the final scraper
jupyter notebook amazon_scrape_final.ipynb

# Test individual functions
python -c "from scraper import get_title; print('OK')"
```

---

## Documentation Guidelines

### README.md

Keep README up to date with:
- Project description
- Setup instructions
- Usage examples
- Screenshots

### Docstrings

Add docstrings to all functions:
- Brief description
- Args (parameters)
- Returns
- Raises (if applicable)

### Comments

- Explain complex logic
- Note any assumptions
- Reference sources if needed

---

## Commit Guidelines

### Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Code style changes |
| `refactor` | Code refactoring |
| `test` | Testing changes |
| `chore` | Maintenance tasks |

### Examples

```
feat: add multi-page scraping support

fix: update price selector for Amazon HTML change

docs: update README with new setup instructions
```

---

## Branch Naming

Use descriptive branch names:

| Branch Type | Naming | Example |
|-------------|--------|---------|
| Feature | `feature/description` | `feature/multi-page-scraping` |
| Bug Fix | `fix/description` | `fix/price-selector` |
| Documentation | `docs/description` | `docs/update-readme` |
| Refactor | `refactor/description` | `refactor/clean-code` |

---

## Review Process

1. Submit a pull request
2. Ensure all checks pass
3. Wait for review
4. Address feedback
5. Get approval
6. Merge

---

## Project Structure

```
Amazon-Web-Scrapping/
│
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── amazon_scrape_final.ipynb
├── amazon_web_scraping_tutorial.ipynb
├── amazon_data.csv
│
├── docs/
│   ├── blueprint.md
│   ├── cheatsheets.md
│   └── verification_checklist.md
│
├── images/
│   └── *.png
│
└── .ipynb_checkpoints/
```

---

## Getting Help

- Check [README.md](README.md) for setup instructions
- Review [docs/](docs/) for detailed documentation
- Open an issue for bugs or feature requests

---

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Project documentation

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

*Last Updated: 2026-07-20*