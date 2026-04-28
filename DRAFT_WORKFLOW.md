# Draft / Main Git Workflow

Use `main` as the clean thesis version.
Use `sandbox` as the sandbox branch for experiments.

## Switch Between Versions

```powershell
git switch main
git switch sandbox
```

## Work In The Sandbox

```powershell
git switch sandbox
```

Edit the appendix files, then save a checkpoint:

```powershell
git add .
git commit -m "Update appendix draft"
```

These changes stay in `sandbox` and do not affect `main`.

## Pull New Main Changes Into The Draft

Use this when `main` has newer thesis changes and you want them inside the sandbox:

```powershell
git switch sandbox
git merge main
```

## Bring Draft Changes Back Into Main

Use this only when you decide the draft changes are good enough for the real thesis:

```powershell
git switch main
git merge sandbox
```

## Take Only One Draft Commit Into Main

Use this when you want only one selected commit instead of all draft changes:

```powershell
git switch main
git cherry-pick COMMIT_ID
```

Find commit IDs with:

```powershell
git log --oneline
```

## Undo A Bad Draft Experiment

If you are on `sandbox` and want to throw away only uncommitted changes:

```powershell
git restore .
```

If the bad experiment was already committed, make a new commit that reverses it:

```powershell
git revert COMMIT_ID
```
