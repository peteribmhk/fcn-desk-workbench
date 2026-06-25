# GitHub Upload Steps

Target account: <https://github.com/peteribmhk>  
Recommended repository name: `fcn-desk-workbench`  
Current visibility: **Public**  
Recommended rule: keep this public repo free of client data, actual issuer quotes, and firm-confidential materials.

## Step 1: Create The Repository

1. Log in to GitHub with the `peteribmhk` account.
2. Open <https://github.com/new>.
3. Set **Repository name** to `fcn-desk-workbench`.
4. Set **Visibility** based on intended use:
   - **Public** only for sanitized workflow templates and educational methodology.
   - **Private** if you will store internal desk notes, actual quotes, or client-specific context.
5. Do not add README, `.gitignore`, or license on GitHub, because this project already contains those files.
6. Click **Create repository**.

## Step 2: Upload Files

1. On the empty repository page, click **uploading an existing file**.
2. Open the local project folder:

   ```text
   C:\Users\ZhuanZ1\Documents\Codex\2026-06-07\i-am-a-securities-salesperson-in\outputs\fcn-desk-workbench
   ```

3. Drag all project files and folders into GitHub:
   - `README.md`
   - `methodology.md`
   - `watchlist.csv`
   - `.gitignore`
   - `github-upload-steps.md`
   - `templates/`
   - `samples/`

4. Commit message:

   ```text
   Initial FCN desk workbench
   ```

5. Click **Commit changes**.

## Step 3: Verify

After upload, check:

- `README.md` displays on the repo homepage.
- `templates/` and `samples/` folders are visible.
- The repo visibility matches the intended use.
- No client names, account details, actual suitability records, or firm-confidential issuer quotes were uploaded.

## Step 4: Daily Use

Use this prompt in Codex:

```text
Refresh FCN market data using my fcn-desk-workbench project. Screen the watchlist for RFQ candidates, use public listed-options data only as a vol/liquidity proxy, normalize any real issuer quotes by RO/KO/KI/strike/tenor before ranking value, suggest tenor/KI/KO/airbag positioning, prepare issuer RFQ wording, and draft client explanation. Label everything indicative only.
```

## If You Later Install Git

If Git or GitHub Desktop becomes available, this project can be pushed by command line instead of web upload. Until then, GitHub web upload is the simplest reliable path.
