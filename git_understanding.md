# Learn Git

## Git Concepts: Staging vs. Committing

### Summary

**What is the difference between staging and committing?**

Staging is like setting changes aside before saving them. It prepares files for the next commit but doesn’t store them permanently. Committing takes a snapshot of the staged files and saves them in Git’s history, making the changes official.

**Why does Git separate these two steps?**

Git separates staging and committing to give you more control over what gets saved. This allows you to organize your changes, commit only specific files instead of everything at once, and review your work before making a permanent record.

**When would you want to stage changes without committing?**

You might stage changes without committing when working on multiple files but only want to commit some, when saving progress but aren’t ready to finalize, or when reviewing edits before making a structured commit.

## Branching & Team Collaboration

### Reflection

**Why is pushing directly to main problematic?**

Pushing directly to main can cause issues because it immediately affects the main codebase. If there’s a bug or mistake, it could break everything for everyone. Keeping main stable is important, especially in team projects.

**How do branches help with reviewing code?**

Branches let developers work on new features or fixes separately without affecting the main branch. Before merging, team members can review the changes, test them, and make sure everything works properly.

**What happens if two people edit the same file on different branches?**

Git will try to merge the changes. If both people edited the same part of the file, Git won’t know which change to keep and will create a merge conflict. The team will have to manually fix it before merging.

## Advanced Git Commands & When to Use Them

### Reflection

**What does each command do?**

`git checkout main -- <file>` restores a specific file from main without affecting other changes. `git cherry-pick <commit>` lets you apply just one commit from another branch instead of merging everything. `git log` shows the commit history, helping track who changed what and when. `git blame <file>` shows who last modified each line in a file and when they did it.

**When would you use it in a real project?**

You’d use `git checkout main -- <file>` if you accidentally changed a file and want to get the original version back. `git cherry-pick` is useful if a fix or feature exists in another branch but you don’t want to merge the whole thing. `git log` is helpful when tracking project changes and understanding past commits. `git blame` is great for debugging or checking who last edited a specific part of a file, so you know who to ask about it.

**What surprised you while testing these commands?**

I was surprised by how useful `git cherry-pick` is, it’s like grabbing only the parts you need from another branch.

## Understand Git bisect

### Reflection

**What does `git bisect` do?**

`git bisect` helps find which commit introduced a bug by automatically checking commits between a good and bad state.

**When would you use it in a real-world debugging situation?**

You’d use `git bisect` when a bug appears but you’re not sure which commit caused it. Instead of guessing, `git bisect` helps track down the exact commit where things went wrong.

**How does it compare to manually reviewing commits?**

Manually checking commits can be slow and frustrating, especially if there are many commits. `git bisect` speeds up the process by automatically finding the problem commit in just a few steps.
