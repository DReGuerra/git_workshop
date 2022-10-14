# Git Version Control Workshop
André Guerra \
June, 2022 \
andre.guerra@mail.mcgill.ca  

---
Description: \
This is repository contains a git version control workshop. The goal of this repo is to be a quick and easy way to get started using git version control. This will remain an open project where I will continue to add tips and information over time. So, this is by no mean an exhaustive reference (yet!).

---
*NOTE:* Let's try to keep the core body of the workshop intact!

Please do not make changes to `main.md`, `README.md`, or any other core components of the workshop. And if you do make any changes, just make sure you don't stage, commit, and then push these. You can also revert back to the last version in the remote if you want by running the command: \
`>> git reset --hard`

We have `python_sandbox.py` as an example file, and feel free to make any new files for you to practice with (.py, .sh, .md, etc.). These you can stage, commit, and push. 

If you would like to contribute to the core body of the workshop, please contact me and I will add you as a contributor.

**This is a temporary measure. We will soon handle this by introducing branches to this repository.

---
## Core Contents
1. `main.md` $\rightarrow$ a markdown file containing the main body of this workshop
2. Directory structure and purpose \
`1_data/` $\rightarrow$ raw data files (.csv mostly) \
`2_proc_data/` $\rightarrow$ processed data files (.csv mostly) \
`3_output/` $\rightarrow$ output data files (.csv, .xlsx, txt, etc.) \
`4_figures/` $\rightarrow$ figures produced by the script (.png, .eps, etc.)
3. python_sandbox.py \
This is a sample python script to be modified, staged, committed, and pushed to repository

## Branches
1. Main branch \
    The `main` branch contains the long term version of all our files. We will merge to this branch only to update versions of the workshop itself. So, a `dev` $\rightarrow$ `main` merge, should only be done by myself or an official contributor to the repository. 
2. Development branch \
    The `dev` branch is our working branch. It contains our latest version of the files in our repository. Users can make their user specific branches (`user_name`) from `dev`.
3. User-specific branch \
    The `user_name` branch is your own personal branch. In this branch you can make all the modifications you desire to practice the git version control commands and workflow. Note, however, that this branch level doesn't have to be named your name. This is just for the purposes of our workshop. Often, this level of branch will have a name of the task that you are trying to accomplish with your edits to the files. For example: `concentration_analysis`, `review_plt_format`, etc.
