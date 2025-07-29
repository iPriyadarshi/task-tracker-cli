#!/usr/bin/env python3
"""
Task Tracker CLI - A simple command-line task management tool
Usage: python task_cli.py <command> [arguments]
"""

import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional


class TaskManager:
    def __init__(self, json_file: str = "tasks.json"):
        self.json_file = json_file
        self.tasks = self.load_tasks()

    def load_tasks(self) -> List[Dict]:
        """Load tasks from JSON file. Create file if it doesn't exist."""
        if not os.path.exists(self.json_file):
            return []
        
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading tasks file: {e}")
            return []

    def save_tasks(self) -> None:
        """Save tasks to JSON file."""
        try:
            with open(self.json_file, 'w', encoding='utf-8') as file:
                json.dump(self.tasks, file, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving tasks: {e}")
            sys.exit(1)

    def get_next_id(self) -> int:
        """Get the next available task ID."""
        if not self.tasks:
            return 1
        return max(task['id'] for task in self.tasks) + 1

    def find_task_by_id(self, task_id: int) -> Optional[Dict]:
        """Find a task by its ID."""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None

    def add_task(self, description: str) -> None:
        """Add a new task."""
        if not description.strip():
            print("Error: Task description cannot be empty")
            return

        task_id = self.get_next_id()
        current_time = datetime.now().isoformat()
        
        new_task = {
            'id': task_id,
            'description': description.strip(),
            'status': 'todo',
            'createdAt': current_time,
            'updatedAt': current_time
        }
        
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task_id})")

    def update_task(self, task_id: int, new_description: str) -> None:
        """Update a task's description."""
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return

        if not new_description.strip():
            print("Error: Task description cannot be empty")
            return

        task['description'] = new_description.strip()
        task['updatedAt'] = datetime.now().isoformat()
        self.save_tasks()
        print(f"Task {task_id} updated successfully")

    def delete_task(self, task_id: int) -> None:
        """Delete a task."""
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return

        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        self.save_tasks()
        print(f"Task {task_id} deleted successfully")

    def mark_task_status(self, task_id: int, status: str) -> None:
        """Mark a task with a specific status."""
        valid_statuses = ['todo', 'in-progress', 'done']
        if status not in valid_statuses:
            print(f"Error: Invalid status. Valid statuses are: {', '.join(valid_statuses)}")
            return

        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return

        task['status'] = status
        task['updatedAt'] = datetime.now().isoformat()
        self.save_tasks()
        print(f"Task {task_id} marked as {status}")

    def list_tasks(self, status_filter: Optional[str] = None) -> None:
        """List tasks, optionally filtered by status."""
        if not self.tasks:
            print("No tasks found")
            return

        filtered_tasks = self.tasks
        if status_filter:
            valid_statuses = ['todo', 'in-progress', 'done']
            if status_filter not in valid_statuses:
                print(f"Error: Invalid status filter. Valid statuses are: {', '.join(valid_statuses)}")
                return
            filtered_tasks = [task for task in self.tasks if task['status'] == status_filter]

        if not filtered_tasks:
            status_msg = f" with status '{status_filter}'" if status_filter else ""
            print(f"No tasks found{status_msg}")
            return

        # Sort tasks by ID for consistent output
        filtered_tasks.sort(key=lambda x: x['id'])

        print(f"{'ID':<4} {'Status':<12} {'Description':<50} {'Created':<20} {'Updated':<20}")
        print("-" * 108)
        
        for task in filtered_tasks:
            created_date = datetime.fromisoformat(task['createdAt']).strftime('%Y-%m-%d %H:%M')
            updated_date = datetime.fromisoformat(task['updatedAt']).strftime('%Y-%m-%d %H:%M')
            
            print(f"{task['id']:<4} {task['status']:<12} {task['description']:<50} {created_date:<20} {updated_date:<20}")


def print_usage():
    """Print usage information."""
    usage = """
Task Tracker CLI

Usage:
    python task_cli.py add "<description>"           - Add a new task
    python task_cli.py update <id> "<description>"   - Update a task
    python task_cli.py delete <id>                   - Delete a task
    python task_cli.py mark-in-progress <id>         - Mark task as in progress
    python task_cli.py mark-done <id>                - Mark task as done
    python task_cli.py list                          - List all tasks
    python task_cli.py list done                     - List completed tasks
    python task_cli.py list todo                     - List pending tasks
    python task_cli.py list in-progress              - List tasks in progress

Examples:
    python task_cli.py add "Buy groceries"
    python task_cli.py update 1 "Buy groceries and cook dinner"
    python task_cli.py mark-done 1
    python task_cli.py list done
    """
    print(usage)


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    task_manager = TaskManager()
    command = sys.argv[1].lower()

    try:
        if command == "add":
            if len(sys.argv) != 3:
                print("Error: 'add' command requires a task description")
                print("Usage: python task_cli.py add \"<description>\"")
                sys.exit(1)
            task_manager.add_task(sys.argv[2])

        elif command == "update":
            if len(sys.argv) != 4:
                print("Error: 'update' command requires task ID and new description")
                print("Usage: python task_cli.py update <id> \"<description>\"")
                sys.exit(1)
            try:
                task_id = int(sys.argv[2])
                task_manager.update_task(task_id, sys.argv[3])
            except ValueError:
                print("Error: Task ID must be a number")
                sys.exit(1)

        elif command == "delete":
            if len(sys.argv) != 3:
                print("Error: 'delete' command requires a task ID")
                print("Usage: python task_cli.py delete <id>")
                sys.exit(1)
            try:
                task_id = int(sys.argv[2])
                task_manager.delete_task(task_id)
            except ValueError:
                print("Error: Task ID must be a number")
                sys.exit(1)

        elif command == "mark-in-progress":
            if len(sys.argv) != 3:
                print("Error: 'mark-in-progress' command requires a task ID")
                print("Usage: python task_cli.py mark-in-progress <id>")
                sys.exit(1)
            try:
                task_id = int(sys.argv[2])
                task_manager.mark_task_status(task_id, 'in-progress')
            except ValueError:
                print("Error: Task ID must be a number")
                sys.exit(1)

        elif command == "mark-done":
            if len(sys.argv) != 3:
                print("Error: 'mark-done' command requires a task ID")
                print("Usage: python task_cli.py mark-done <id>")
                sys.exit(1)
            try:
                task_id = int(sys.argv[2])
                task_manager.mark_task_status(task_id, 'done')
            except ValueError:
                print("Error: Task ID must be a number")
                sys.exit(1)

        elif command == "list":
            if len(sys.argv) == 2:
                task_manager.list_tasks()
            elif len(sys.argv) == 3:
                status_filter = sys.argv[2].lower()
                task_manager.list_tasks(status_filter)
            else:
                print("Error: 'list' command takes at most one argument")
                print("Usage: python task_cli.py list [done|todo|in-progress]")
                sys.exit(1)

        else:
            print(f"Error: Unknown command '{command}'")
            print_usage()
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
