# Setup Git + GitHub CLI And Push

Target GitHub account: <https://github.com/peteribmhk>  
Target repository: `peteribmhk/fcn-desk-workbench`  
Recommended visibility: **Private**

Run these commands in a normal Windows PowerShell terminal on your laptop, not inside Codex.

## 1. Install Git

```powershell
winget install --id Git.Git -e --source winget
```

If Windows asks for permission, approve it.

## 2. Install GitHub CLI

```powershell
winget install --id GitHub.cli -e --source winget
```

Close and reopen PowerShell after installation.

## 3. Verify Installation

```powershell
git --version
gh --version
```

Both commands should print version numbers.

## 4. Log In To GitHub

```powershell
gh auth login
```

Recommended choices:

- GitHub.com
- HTTPS
- Authenticate Git with GitHub credentials: Yes
- Login with a web browser

Follow the browser login and 2FA flow for the `peteribmhk` account.

Verify:

```powershell
gh auth status
```

## 5. Push This Project To A New Private Repo

```powershell
cd "C:\Users\ZhuanZ1\Documents\Codex\2026-06-07\i-am-a-securities-salesperson-in\outputs\fcn-desk-workbench"
git init
git branch -M main
git add .
git commit -m "Initial FCN desk workbench"
gh repo create peteribmhk/fcn-desk-workbench --private --source . --remote origin --push
```

## 6. If The Repo Already Exists

If GitHub says the repo already exists, use:

```powershell
cd "C:\Users\ZhuanZ1\Documents\Codex\2026-06-07\i-am-a-securities-salesperson-in\outputs\fcn-desk-workbench"
git init
git branch -M main
git add .
git commit -m "Initial FCN desk workbench"
git remote add origin https://github.com/peteribmhk/fcn-desk-workbench.git
git push -u origin main
```

If `git remote add origin` says the remote already exists:

```powershell
git remote set-url origin https://github.com/peteribmhk/fcn-desk-workbench.git
git push -u origin main
```

## 7. Verify On GitHub

Open:

```text
https://github.com/peteribmhk/fcn-desk-workbench
```

Check:

- The repo is private.
- `README.md` appears on the homepage.
- `templates/` and `samples/` are visible.
- No client names, account details, actual suitability records, or confidential issuer quotes were uploaded.

## 8. If Git Reports Dubious Ownership

If `git push` fails with:

```text
detected dubious ownership in repository
```

run:

```powershell
git config --global --add safe.directory "C:/Users/ZhuanZ1/Documents/Codex/2026-06-07/i-am-a-securities-salesperson-in/outputs/fcn-desk-workbench"
git push -u origin main
```

This is needed because Codex created the project files under a sandbox owner, while your normal PowerShell runs as your Windows user.

## 9. One-Command Push Script

From normal Windows PowerShell, run:

```powershell
& "C:\Users\ZhuanZ1\Documents\Codex\2026-06-07\i-am-a-securities-salesperson-in\outputs\fcn-desk-workbench\push-to-github.ps1"
```
