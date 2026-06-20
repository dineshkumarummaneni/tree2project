# tree2project

Create complete project directory structures from tree-format text files.

`tree2project` allows developers, DevOps engineers, and AI agents to quickly scaffold projects using a simple tree representation.

---

## Installation

```bash
pip install tree2project
```

---

## Features

* Create project structures from tree files
* Export existing project structures
* Validate generated structures
* Dry-run support
* Interactive target directory selection
* Cross-platform
* Lightweight and dependency-friendly

---

## Example Structure File

```text
gitops-agent/
├── pyproject.toml
├── README.md
├── src/
│   ├── main.py
│   └── utils/
│       └── helpers.py
└── tests/
```

---

## Create Project Structure

```bash
tree2project create structure.txt
```

Specify target directory:

```bash
tree2project create structure.txt --target ~/projects
```

Preview without creating files:

```bash
tree2project create structure.txt --dry-run
```

---

## Export Existing Structure

Export project structure:

```bash
tree2project export ./my_project
```

Save output:

```bash
tree2project export ./my_project --output structure.txt
```

---

## Validate Structure

Validate project against a structure specification:

```bash
tree2project validate structure.txt --target ./my_project
```

Example output:

```text
Structure valid
```

or

```text
Missing paths:
./my_project/src/main.py
```

---

## Usage Examples

### Generate New Project

```bash
tree2project create project_structure.txt
```

### Export Existing Repository

```bash
tree2project export ./repository
```

### Verify Generated Project

```bash
tree2project validate project_structure.txt --target ./repository
```

---

## Supported Format

Example:

```text
project/
├── README.md
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
└── requirements.txt
```

---

## Use Cases

### AI Coding Agents

Generate repository skeletons before code generation.

### Project Bootstrapping

Create standard project layouts instantly.

### Development Teams

Share project templates across teams.

### Education

Create exercises and sample projects.

---

## Roadmap

### v0.2.0

* JSON support
* YAML support
* Structure diff command
* Template generation

### v0.3.0

* Automatic `__init__.py`
* GitHub repository templates
* Framework templates

### v1.0.0

* Plugin system
* Interactive TUI
* Advanced validation engine

---

## Development

Clone repository:

```bash
git clone https://github.com/yourusername/tree2project.git
```

Install locally:

```bash
pip install -e .
```

Run tests:

```bash
pytest
```

---

## License

MIT License

---

## PyPI

https://pypi.org/project/tree2project/
