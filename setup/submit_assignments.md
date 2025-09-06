# Submission Guide

This guide will provide you details on how to submit the assignments

All commands must be run from ScraPY folder (on the terminal).

---

## 1. Checkout main
- Run Cmd `git branch`. This will tell you your current active branch
- If you see `* main` in your output, goto step #2
- Else, Run below commands:
    - `git reset --hard`
    - `git checkout main`
    - `git branch`. You will see `* main` in output this time.

## 2. Sync your repo with github
- Run Cmd: `git pull`

## 3. Create a new local branch for your assignment
- Decide a name for your local branch and use that name for the next command. It must start with your name and then explanation separated by hyphens
    - Ex: `agaharwar-intro-ass-1`. Choose your own name for every assignment and replace `agaharwar-intro-ass-1` for below commands
- Run `git checkout -b agaharwar-intro-ass-1`. **Remember to replace branch name**

## 4. Do your assignment
- Create new file
- Do assignment in that file
- Run `git status` to see the list of files you created
    - Sample output
    ```bash
    Untracked files:
        (use "git add <file>..." to include in what will be committed)
                setup/submit_assignments.md
    ```

## 5. Upload your assignment
- Run `git status` and copy the output 
- Add your files with the following command:
    - `git add setup/submit_assignments.md` 
    If you have multiple files in an assignment, you can upload them by separating the file names with spaces. So use the following commands for that: 
    - `git add setup/submit_assignments.md file2.py`
    - **NOTE:** File Paths are relative. You can copy paste from `git status` output
- Choose a one line message describing the assignment
- Run `git commit -m "Introduction Assignment"`. **Remember to choose your own message**
- Run `git push origin agaharwar-intro-ass-1`. **Remember to replace branch name**

## 6. Request review for your assignment
- Goto github on Chrome
- You must see a pop up on top saying new change
- Click on `Compare and Pull Request`
- Click on `Create Pull Request`

=========================================================

## How to fix problems in your assignment?

- Run `git branch`
- If your assignment branch is not selected, Run `git checkout <branch_name>`
- Do the changes
- Add using `git add file1.py file2.py`. Put your actual files here
- Run `git commit --amend --no-edit`
- Run `git push origin branch_name`

=========================================================

## What to do after assignment is merged?

- Run `git checkout main`
- Run `git branch -D branch_name`. **Remember to replace your actual branch_name**
