# EXECUTABLE — AERA fresh GitHub publication through Codex

**Author-approved task:** publish this self-contained, conversation-derived AERA High Fantasy Framework scaffold as the **initial commit** of `https://github.com/xApologies/AERA`, using the existing local directory `%USERPROFILE%\_AERA` (in the screenshot `C:\Users\rando\_AERA`). The GitHub repository has been created by the author. **Do not create another repository**. This is a fresh publish, not an upstream migration.

## 1. Safety and authority

- Read this file, `CONSTITUTION.md`, `README.md`, `FRAMEWORK_INDEX.md`, `provenance/SOURCE_REGISTER.md`, and `provenance/DECISION_LEDGER.md` before writing.
- Preserve exact current AERA terminology, all four separate classifications, World Clock L0–L4, and source status labels.
- This ZIP is the **only import source** for the first publication. Do **not** clone, fetch bulk content from, or vendor `_bricked`, Mk-147, MK231, MK157 or `_raeon`. Keep source URLs in the documentation for later inheritance.
- `_inbox` is a **strictly local transport folder**. Do not commit `_inbox`, any of its contents, or the source ZIP. Do not remove the folder.
- Do not invent missing mathematical derivations, license terms, mechanics, original prophetic verses or technical ER Foam specification.
- Never force push. Preserve any unexpected existing work and stop if it cannot be reconciled safely.

## 2. Intake and staging

1. Locate the ZIP under `%USERPROFILE%\_AERA\_inbox` (the author manually places it there). The ZIP name is `AERA_FRESH_PUBLISH_v0.3.0.zip`.
2. Open it safely in a temporary directory **outside the Git working tree**. Reject absolute paths, `..` traversal, symlinks, suspicious file types, and duplicate/conflicting case-insensitive paths. Do not run executable code from the ZIP. `Executable.md` is the instruction document, not a shell script.
3. Verify ZIP CRC, then verify each listed file against `SHA256SUMS.txt` and `MANIFEST.json`. Reject missing, extra, or modified content; manifest files themselves are not hashed by `SHA256SUMS.txt`.
4. Ensure the archive has `CONSTITUTION.md`, `AGENTS.md`, `README.md`, `FRAMEWORK_INDEX.md`, `WORLD_CLOCK.md`, `PROPHECIES.md`, all L0–L4 README files, and provenance documents. Preserve all current package files.

## 3. Local Git bootstrap

1. Set destination `%USERPROFILE%\_AERA`. It currently contains `_inbox`. Keep `_inbox` untouched and untracked.
2. Inspect local `.git` state and remote `https://github.com/xApologies/AERA` before doing anything. If Git already exists, preserve its HEAD and compare files. If remote has any commits, fetch and reconcile; **do not** overwrite, reset, or force push. If repository is truly empty, initialize Git on `main`.
3. Copy only verified payload files from staging to the destination. Do not copy a wrapper folder, original ZIP, staging directory, or `_inbox` into Git. Preserve `.gitignore` (contains `_inbox` ignore rule).
4. Set `origin` to `https://github.com/xApologies/AERA` if missing; if another origin exists, stop and report it. Use normal Git authentication available to Codex.
5. Inspect `git status --short`, `git diff --check`, and `git ls-files --others --exclude-standard`. Check that `_inbox` is not staged, that no unrelated existing files were deleted, and that source archives are not included.
6. Run semantic checks: root Constitution present and substantial; names Seven Realms, Unwritten, Borrowed Hours, Thousand Threads, Covenant Gardens, Living Art, Cartographers, Black Prophecy; 1/7…6/7 chromatic landmarks; separate six operational Transduction domains; lifecycle Conceive→Shape→Hold→Resolve→Manifest→Release; Alchemy Type 1–5; optional interfaces; World Clock five layers; ER Foam placeholder; links to source repositories. Do not change content just to satisfy string matching; report any discrepancy.
7. `git add` only package payload files (exclude `_inbox`, source ZIP, temporary data). Commit `AERA v0.3.0 — initial cumulative high fantasy framework and constitution`.
8. Push **normally** to `origin main`. Do not force push. If push fails due to unexpected remote history, stop and report instead of overriding.

## 4. Post-push verification and report

- Fetch/inspect the remote `main` SHA and verify it matches local `HEAD`.
- Confirm remote root `CONSTITUTION.md`, `Executable.md`, `README.md`, `FRAMEWORK_INDEX.md`, `PROPHECIES.md`, L0–L4 directories, and provenance exist.
- Confirm `_inbox` and all ZIPs are absent from tracked Git paths; local `_inbox` remains intact.
- Report remote commit SHA, number of committed files, SHA verification, semantic verification, branch, remote URL, clean/dirty working-tree status, and any discrepancies.
- Never report 'published' without a successful remote verification.

## 5. Scope of subsequent passes

Later, and only after author authorization, perform a full-source inheritance and semantic reverse diff from `_bricked`, MK147, MK231 and selective other sources. The current release intentionally contains only the cumulative AERA workshop material and links. Do not automatically migrate 3 GB of source mathematics today.
