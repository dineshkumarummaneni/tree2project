# Folder Structure Creator

A Python utility that recreates an entire project directory structure from a tree-format text file.

The tool reads a folder structure specification, asks the user where it should be created, displays a preview, and then generates all directories and files exactly as defined.

---

## Features

* Create complete project structures from text files
* Interactive target directory selection
* Structure preview before creation
* Dry-run mode
* Automatic directory creation
* Skip existing files
* Validation of input paths
* Supports standard tree-style structures
* Suitable for AI agents and repository bootstrapping

---

## Supported Structure Format

Example structure file:

```text
gitops-agent/
├── pyproject.toml
├── README.md
├── LICENSE
│
├── gitops_agent/
│   ├── cli/
│   │   ├── app.py
│   │   └── commands/
│   │       ├── clone.py
│   │       ├── pull.py
│   │       └── push.py
│
│   ├── core/
│   │   ├── orchestrator.py
│   │   └── workflow.py
│
│   └── config/
│       └── settings.py
│
├── tests/
│   ├── unit/
│   └── integration/
│
└── examples/
```

---

## Installation

Clone or download the script.

Requirements:

```bash
python >= 3.9
```

No third-party dependencies are required.

---

## Usage

### Option 1: Provide Structure File as Argument

```bash
python main.py project_structure.txt
```

---

### Option 2: Interactive Mode

```bash
python main.py
```

The program will prompt:

```text
Enter structure file path:
>
```

---

## Target Directory Selection

After loading the structure file:

```text
Enter target directory where structure should be created:
>
```

Example:

```text
/home/dinesh/Desktop/projects
```

The generated structure will be created inside the specified directory.

---

## Preview Mode

Before creating files:

```text
Structure Preview
============================================================
[DIR ] /home/user/projects/gitops-agent
[FILE] /home/user/projects/gitops-agent/README.md
[DIR ] /home/user/projects/gitops-agent/gitops_agent
============================================================
```

---

## Confirmation

The tool asks for confirmation:

```text
Create this structure? [y/N]:
```

Only `y` proceeds with creation.

---

## Dry Run

Preview without creating files:

```bash
python main.py project_structure.txt --dry-run
```

Output:

```text
Structure Preview
...
Dry-run complete. No changes made.
```

---

## Example

Structure File:

```text
myapp/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
└── README.md
```

Target Directory:

```text
/home/user/projects
```

Result:

```text
/home/user/projects/myapp
/home/user/projects/myapp/src
/home/user/projects/myapp/src/main.py
/home/user/projects/myapp/src/utils.py
/home/user/projects/myapp/tests
/home/user/projects/myapp/README.md
```

---

## Existing Files

Behavior:

* Existing directories are reused
* Existing files are skipped
* New files are created as empty files

Example:

```text
SKIP : /home/user/projects/myapp/README.md
```

---

## Output Summary

After execution:

```text
Summary
============================================================
Directories created : 24
Files created       : 59
Files skipped       : 3
============================================================
```

---

## Use Cases

### AI Coding Agents

Generate project skeletons before code generation.

### Repository Bootstrapping

Create standardized project templates.

### Internal Frameworks

Provision company-specific repository layouts.

### Learning & Training

Quickly generate example projects and exercises.

---

## Limitations

Current version:

* Creates empty files only
* Does not overwrite existing files
* Does not generate file contents
* Assumes standard tree-format input

---

## Future Enhancements

Potential additions:

* Auto-generate `__init__.py`
* File content templates
* JSON/YAML structure support
* Overwrite mode
* Structure validation
* Export current repository structure
* Agent integration APIs
* Parallel file creation

---

## License

MIT License
