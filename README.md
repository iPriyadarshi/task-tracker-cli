# Task Tracker CLI

A simple, efficient command-line interface (CLI) application for managing tasks. Built with Python, this tool allows you to add, update, delete, and organize tasks directly from the command line, with persistent storage in JSON format.

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- ✅ Add new tasks
- ✅ Update existing tasks
- ✅ Delete tasks
- ✅ Mark tasks as in-progress or done
- ✅ List all tasks
- ✅ Filter tasks by status (todo, in-progress, done)
- ✅ Persistent storage using JSON
- ✅ Error handling and input validation
- ✅ Windows batch file wrappers for easier usage
- ✅ Interactive menu interface
- ✅ Cross-platform compatibility

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/iPriyadarshi/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. **Ensure Python 3.6+ is installed**
   ```bash
   python --version
   ```

3. **Start using the CLI**
   ```bash
   python task_cli.py add "My first task"
   python task_cli.py list
   ```

## 📖 Usage

There are several ways to use the Task Tracker CLI:

### Method 1: Direct Python Command (Recommended)
```
python task_cli.py <command> [arguments]
```

### Method 2: Using Batch Files (Windows Only)

#### Simple Batch File
Use `task-cli.bat` for quick commands:
```cmd
task-cli.bat list
task-cli.bat add "New task"
task-cli.bat mark-done 1
```

#### Interactive Menu
Double-click `task-cli-interactive.bat` or run it from command prompt for a user-friendly menu interface with options like:
- List all tasks
- Add/update/delete tasks
- Mark tasks with different statuses
- Filter tasks by status

**Note**: If the batch file window closes immediately, make sure to run it from Command Prompt rather than double-clicking.

## 🎯 Commands

### Adding a new task
```bash
python task_cli.py add "Buy groceries"
```
**Output:** `Task added successfully (ID: 1)`

### Updating a task
```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```
**Output:** `Task 1 updated successfully`

### Deleting a task
```bash
python task_cli.py delete 1
```
**Output:** `Task 1 deleted successfully`

### Marking a task as in progress
```bash
python task_cli.py mark-in-progress 1
```
**Output:** `Task 1 marked as in-progress`

### Marking a task as done
```bash
python task_cli.py mark-done 1
```
**Output:** `Task 1 marked as done`

### Listing all tasks
```bash
python task_cli.py list
```

### Listing tasks by status
```bash
# List completed tasks
python task_cli.py list done

# List pending tasks
python task_cli.py list todo

# List tasks in progress
python task_cli.py list in-progress
```

## 📋 Task Properties

Each task contains the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | Integer | Unique identifier (auto-generated) |
| `description` | String | Task description |
| `status` | String | Current status: `todo`, `in-progress`, `done` |
| `createdAt` | String | Creation timestamp (ISO format) |
| `updatedAt` | String | Last update timestamp (ISO format) |

## 💾 Data Storage

Tasks are automatically saved to a `tasks.json` file in the project directory. The file is created when you add your first task.

**Example JSON structure:**
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2024-01-15T10:30:00.123456",
    "updatedAt": "2024-01-15T10:30:00.123456"
  },
  {
    "id": 2,
    "description": "Walk the dog",
    "status": "done",
    "createdAt": "2024-01-15T11:00:00.654321",
    "updatedAt": "2024-01-15T12:00:00.789012"
  }
]
```

## Error Handling

The application includes comprehensive error handling for:

- Invalid command arguments
- Non-existent task IDs
- Empty task descriptions
- Invalid status values
- File I/O errors
- JSON parsing errors

## Examples

Here's a complete example workflow:

### Using Python directly:
```bash
# Add some tasks
python task_cli.py add "Buy groceries"
python task_cli.py add "Walk the dog"
python task_cli.py add "Finish project report"

# List all tasks
python task_cli.py list

# Mark a task as in progress
python task_cli.py mark-in-progress 1

# Update a task description
python task_cli.py update 3 "Finish and submit project report"

# Mark a task as done
python task_cli.py mark-done 2

# List only completed tasks
python task_cli.py list done

# List tasks that are in progress
python task_cli.py list in-progress

# Delete a task
python task_cli.py delete 1
```

### Using Windows batch files:
```cmd
# Using simple batch wrapper
task-cli.bat add "Buy groceries"
task-cli.bat list
task-cli.bat mark-done 1

# Using interactive menu
task-cli-interactive.bat
# Then follow the on-screen menu options
```

## 📁 Project Structure

```
task-tracker-cli/
├── task_cli.py                    # Main application file
├── task-cli.bat                   # Simple Windows batch wrapper
├── task-cli-interactive.bat       # Interactive menu for Windows
├── tasks.json                     # Task data storage (created automatically)
├── README.md                      # Project documentation
└── .gitignore                     # Git ignore file
```

## Batch File Usage Details

### task-cli.bat
This is a simple wrapper that allows you to run commands without typing `python` each time:
- From Command Prompt: `task-cli.bat add "Buy groceries"`
- The window will pause after execution so you can see the output

### task-cli-interactive.bat
This provides a menu-driven interface:
- Double-click the file to open an interactive menu
- Choose from numbered options to perform different actions
- Automatically shows current tasks when relevant
- User-friendly prompts for input

## Troubleshooting

### Batch File Issues
- **Window closes immediately**: Run the batch file from Command Prompt instead of double-clicking
- **"Python not found" error**: Make sure Python is installed and added to your system PATH
- **Permission errors**: Run Command Prompt as Administrator if needed

### Common Issues
- **Empty task description**: Make sure to wrap descriptions in quotes when they contain spaces
- **Task not found**: Use `python task_cli.py list` to see current task IDs
- **JSON file corruption**: Delete `tasks.json` to start fresh (this will lose all tasks)

## 🛠️ Development

The project follows these principles:

- **Zero dependencies**: Uses only Python standard library
- **Clean architecture**: Separation of concerns with a TaskManager class
- **Robust error handling**: Graceful handling of edge cases and errors
- **User-friendly interface**: Clear error messages and usage instructions
- **Cross-platform compatibility**: Works on Windows, macOS, and Linux
- **Multiple interfaces**: Command-line and interactive menu options
- **Data integrity**: Proper JSON handling and file operations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## ⭐ Show your support

Give a ⭐️ if this project helped you!

## Project Link: https://roadmap.sh/projects/task-tracker
---

<p align="center">Made with ❤️ for productivity enthusiasts</p>
