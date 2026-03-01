# CourtReach

Local run instructions

1. Create and activate your Python virtualenv, install Python deps (assumes .venv exists):

```powershell
# activate venv on Windows PowerShell
& ".\.venv\Scripts\Activate.ps1"
pip install -r requirements.txt
```

2. Install npm dev dependencies and build Tailwind CSS. On Windows PowerShell, prefer `npm.cmd` if `npm` scripts are blocked by execution policy:

```powershell
# from project root
npm.cmd install
npm.cmd run build:css
# or, watch during development
npm.cmd run watch:css
```

If using Command Prompt (cmd.exe) you can run `npm install` normally.

3. Run Django dev server:

```powershell
python manage.py runserver
```

Notes:
- Tailwind output is `static/css/tailwind.css` which is referenced in `core/templates/core/base.html`.
- If PowerShell blocks `npm`, either use `npm.cmd` or run in cmd.exe. You can also temporarily change execution policy (administrative) if you prefer.
