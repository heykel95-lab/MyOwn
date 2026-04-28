# Git Quick Guide

## See Your Commit History

```bash
git log --oneline --graph --decorate
```

Each line is one checkpoint. The short code at the start, such as `26b0334`, is the commit hash.

## Go Back Temporarily

Use this when you only want to look at an older version:

```bash
git switch --detach HEAD~1
```

`HEAD~1` means "one commit before the current one". You can use `HEAD~2` to go back two commits.

To go forward again to the newest version on `main`:

```bash
git switch main
```

## Go To A Specific Commit

```bash
git switch --detach <commit-hash>
```

Example:

```bash
git switch --detach 26b0334
```

To return to the latest version:

```bash
git switch main
```

## Undo A Commit Safely

Use `revert` when you want Git to make a new commit that undoes an old commit:

```bash
git revert <commit-hash>
```

This is safest when the history may already be shared online.

## Move The Branch Back

This rewinds the branch itself. Save or commit anything important first.

Keep the file changes in your working folder:

```bash
git reset --soft HEAD~1
```

Discard the last commit and its file changes:

```bash
git reset --hard HEAD~1
```

## Push Online

This repository is local until you connect it to GitHub, GitLab, or another remote.

```bash
git remote add origin <remote-url>
git push -u origin main
```

After that, normal pushes are:

```bash
git push
```
