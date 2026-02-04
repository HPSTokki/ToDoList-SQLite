# To Do List with FastAPI and SQLite

----------

## How to Install Python and UV

### 1. Install [Python](https://www.python.org/downloads/) (Latest Version: 3.14)

- **Check if Python is installed:**

```powershell
python --version
> should output 3.xx.x

pip --version
> should output 25.xx.x
```
### 2. Install [UV](https://docs.astral.sh/uv/#installation)

- Install through official link above or by copying this code and paste it on terminal(Powershell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
- Check if UV is installed:
```powershell
uv --version
> should output u 0.x.xx
```
----------

## How to install Git

1. Install [Git](https://git-scm.com/install/windows)
- Verify Installation, Open any terminal
```powershell
git --version
```

----------

## Clone This Repo

1. Open a terminal and navigate to the folder where you want to clone the repo:

```powershell
cd path/to/your/folder
```
2. Clone the repo:
```powershell
git clone https://github.com/HPSTokki/ToDoList-SQLite.git
```
3. Open it in VSCode

----------

## How to Run

1. Create a virtual environment in the project root:
```python
uv venv
or
python -m venv venv
```
2. Activate Virtual Environment:
- On **Windows Command Prompt**:
```terminal
venv/Scripts(or bin)/activate
```
- Or in **Windows Powershell**:
```powershell
./venv/Scripts(or bin)/Activate.ps1
```
if you get an error in **powershell**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
**IMPORTANT**: Always remember to activate the virtual environment before running your project.

2. Verify Python is running locally by checking the Python path:
```powershell
where python
> should output your project directory
```

3. Once verified that Python is running locally to project, install the packages with:
```powershell
uv sync
```

4. And sync it with lockfile always(everytime a package is added, you must sync and lock):
```powershell
uv lock
```

5. Run the FastAPI Project:
```powershell
uv run fastapi dev main2.py
```

6. If success, open a browser and paste the port in terminal:
```
localhost:8000
or
Use localhost:8000/docs
```



    