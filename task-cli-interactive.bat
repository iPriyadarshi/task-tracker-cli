@echo off
title Task Tracker CLI
cd /d "%~dp0"

:menu
cls
echo ================================
echo     Task Tracker CLI
echo ================================
echo.
echo 1. List all tasks
echo 2. List tasks by status
echo 3. Add a new task
echo 4. Update a task
echo 5. Delete a task
echo 6. Mark task as in-progress
echo 7. Mark task as done
echo 8. Run custom command
echo 9. Exit
echo.
set /p choice="Enter your choice (1-9): "

if "%choice%"=="1" goto list_all
if "%choice%"=="2" goto list_status
if "%choice%"=="3" goto add_task
if "%choice%"=="4" goto update_task
if "%choice%"=="5" goto delete_task
if "%choice%"=="6" goto mark_progress
if "%choice%"=="7" goto mark_done
if "%choice%"=="8" goto custom_command
if "%choice%"=="9" goto exit
goto invalid

:list_all
echo.
python task_cli.py list
echo.
pause
goto menu

:list_status
echo.
echo Available statuses: todo, in-progress, done
set /p status="Enter status to filter by: "
python task_cli.py list %status%
echo.
pause
goto menu

:add_task
echo.
set /p description="Enter task description: "
python task_cli.py add "%description%"
echo.
pause
goto menu

:update_task
echo.
python task_cli.py list
echo.
set /p id="Enter task ID to update: "
set /p description="Enter new description: "
python task_cli.py update %id% "%description%"
echo.
pause
goto menu

:delete_task
echo.
python task_cli.py list
echo.
set /p id="Enter task ID to delete: "
python task_cli.py delete %id%
echo.
pause
goto menu

:mark_progress
echo.
python task_cli.py list
echo.
set /p id="Enter task ID to mark as in-progress: "
python task_cli.py mark-in-progress %id%
echo.
pause
goto menu

:mark_done
echo.
python task_cli.py list
echo.
set /p id="Enter task ID to mark as done: "
python task_cli.py mark-done %id%
echo.
pause
goto menu

:custom_command
echo.
echo Enter a custom command (without 'python task_cli.py'):
echo Example: list done, add "Buy milk", update 1 "New description"
set /p cmd="Command: "
python task_cli.py %cmd%
echo.
pause
goto menu

:invalid
echo.
echo Invalid choice! Please enter a number between 1-9.
echo.
pause
goto menu

:exit
echo.
echo Thank you for using Task Tracker CLI!
pause
exit
