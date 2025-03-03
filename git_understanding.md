# Learn Git

## Git Concepts: Staging vs. Committing, Branching & Team Collaboration

### Summary

**What is the difference between staging and committing?**

Staging is like setting changes aside before saving them. It prepares files for the next commit but doesn’t store them permanently. Committing takes a snapshot of the staged files and saves them in Git’s history, making the changes official.

**Why does Git separate these two steps?**

Git separates staging and committing to give you more control over what gets saved. This allows you to organize your changes, commit only specific files instead of everything at once, and review your work before making a permanent record.

**When would you want to stage changes without committing?**

You might stage changes without committing when working on multiple files but only want to commit some, when saving progress but aren’t ready to finalize, or when reviewing edits before making a structured commit.

### Reflection

**Why is pushing directly to main problematic?**

Pushing directly to main can cause issues because it immediately affects the main codebase. If there’s a bug or mistake, it could break everything for everyone. Keeping main stable is important, especially in team projects.

**How do branches help with reviewing code?**

Branches let developers work on new features or fixes separately without affecting the main branch. Before merging, team members can review the changes, test them, and make sure everything works properly.

**What happens if two people edit the same file on different branches?**

Git will try to merge the changes. If both people edited the same part of the file, Git won’t know which change to keep and will create a merge conflict. The team will have to manually fix it before merging.
