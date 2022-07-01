# Git Version Control Workshop
André Guerra  
June/2022  
andre.guerra@mail.mcgill.ca  

## Contents
1. Overview
2. Prep
3. Fundamentals
4. Workflow
5. Walk-through Exercise

## Overview
This is a markdown file (.md). Here, we will discuss some of the features of git version control and how we can use them to manage a github repository. All of the things we will look at here and more can be found in the official [git documentation](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control). Refer to the documentation for detailed descriptions that may be ommited here.

## Prep
In order for us to go throug this workshop, you will need to make yourself a GitHub account. Once that's done, you can access my GitHub account at [DReGuerra](https://github.com/DReGuerra). There, you will need to navigate to the main page of this repository at [git_workshop](https://github.com/DReGuerra/git_workshop). Click on `Code` and select the tab `SSH`. Copy the link in the box that appears. You will need this link to "clone" this repository locally on your computer. In your local computer, create a directory to hold all your repositories that you may be working on; you might call it `repos/`. In the terminal, navigate to that directory, and run the following command: \
`>> git clone git@github.com:DReGuerra/git_workshop.git`

The clone command will copy the entire contents of the remote repository (on GitHub) into a local folder called `git_workshop`. So, if you performed the clone command in the directory `repos/`, you you now have a local copy of the remote repository `git_workshop`, in the location `~/repos/git_workshop/`. You can make modifications to the files and practice git version control.

## Fundamentals of git Version Control
Let's start with two key terms that version control revolves around: 
- <b>remote repository:</b> this is the master repository that is hosted by a cloud service. In our case here, it is hosted by GitHub, but there are other services that can offer similar capabilities (e.g., Atlassian's Bitbucket). The remote repository arquives all versions of the collection of files that are being tracked (part of the repository). The remote repository is often just referred to as "remote" and that's how we'll be referring to it from now on. The remote is the place where we "pull" from and "push" to.
- <b>local repository:</b> in order to work on files in a repository and to maintain version control, the first thing we do is "clone" the remote repository locally. In the previous step (Prep) above, you accessed the remote repository of this workshop and you cloned yourself a copy of it locally. This made you a local copy of the remote. This is referred to as the "local".

OK, now let's define some of the more specific technical terms (these are also git commands) that version control uses:
- <b>fetch:</b> query the remote for latest version of the repository.
- <b>pull:</b> "pulls from remote" - gets the latest verison from the remote to the local.
- <b>stage:</b> Before committing a file, it must be added to the Staging Environment using the command `add` 
- <b>commit:</b> The `commit` command creates a commit ID number and saves the current state of the repo to that commit number. This commit number is always available through git version control, and so you can revert your work back to any previous commit by checking out that commit ID.
- <b>push:</b> "pushes to remote" - sends the updated version that you have in your local (after you've made committed changes) to the remote.

`.gitignore`: this file is in located in the highest level directory of repo. It specifies all exceptions - files that git should ignore and NOT track for version control. \
`.gitconfig`: this file is located in your home directory and it contains global configurations for your git. You can see [here](https://git-scm.com/docs/git-config) how to add aliases and custom options to your `.gitconfig` file. Below is an example `.gitconfig` that might get you started.
```
[user]
	name = first last
    useConfigOnly = true
	email = firstlast@email.com
	username = 
	password = 

[core]
    editor = 'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin
    whitespace = blank-at-eol,tab-in-indent,blank-at-eof,-space-before-tab
    quotepath = off
    fileMode = false
    autocrlf = false
    eol = lf

[push]
    default = simple

[status]
    submodulesummary = true

[alias]
    br = branch
    bra = branch -a
    cm = commit -m
    cam = commit -am
    co = checkout
    cob = checkout -b
    fe = fetch --all
    fep = fetch --prune
    gr = log --oneline --graph --decorate --first-parent --all origin/master dev
    gra = log --oneline --graph --decorate --all
    grf = log --oneline --graph --decorate --first-parent
    grc = log --oneline --graph --decorate --simplify-by-decoration --all
    grs = log --oneline --graph --decorate --simplify-by-decoration --all --decorate-refs-exclude=refs/tags
    gs = !git fetch --prune && git log --oneline --graph --decorate --simplify-by-decoration --all --decorate-refs-exclude=refs/tags
    grss = log --oneline --graph --decorate --simplify-by-decoration --sparse --all
    ph = push
    pl = pull
    rmc = rm --cached
    rmrc = rm -r --cached
    rs = reset
    rsh = reset --hard
    sh = stash
    sha = stash apply
    shp = stash pop
    shl = stash list
    st = status -bs
    std = status
    size = count-objects -H


[color]
    showbranch = always
    status = always

```

## Workflow

The overall workflow:  
fetch $\rightarrow$ pull $\rightarrow$ make changes to files $\rightarrow$ stage changes $\rightarrow$ commit changes (with a message) $\rightarrow$ push

1. <b>Fetch:</b> \
    Before beginning to work on any of our local files we want to query the remote to see if they have been updatated since the last time we worked on them. In a multi-member project, someone else may have done some work on files while you were working on something else. So, we `fetch`:  
    `>> git fetch`  

    After fetching, our local repository now has information on whether the remote has changed, but we (the user) don't know what these changes were. So, we ask for the `status`:  
    `>> git status`
    ```
    Your branch is up to date with 'origin/main'.

    Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
            modified:   README.md
            modified:   main.md
    ```
    The return from this command will give you information on what the changes were (if there were any), and how many commits we are ahead or behind. 

2. <b>Pull:</b> \
    If we are behind the remote, we want to `pull` these changes so that we can start working on the latest version of all files in the repository.  
    `>> git pull`  

3. <b>Make changes:</b> \
    Now we are ready to make changes to the files.  

4. <b>Stage changes:</b> \
    Once enough changes have been made that you are satisfied that the files are now in a state in which their version should be snapshot, then we need to commit thse changes. BUT before committing anything, we need to `stage` the changes. We can stage multiple files at once (if we want to commit them to the same commit number):  
    `>> git add python_script.py 4_figures/plot.png markdown_file.md`  

5. <b>Commit changes:</b> \
    Once our changed files have been staged, we can commit them. In every commit, we want to add a message that is descriptive of the changes that were made and/or the reasons for them. Commit messages tend to follow conventions that may be set by you if this is your own repository, or your project leader if the repository that you are working on is managed by someone else (or a company). We can make multiple commits as we work on the files. How often, how many files at a time, and other convention type questions are dependent on how you (or your group) want to manage the repository. It is advisable to stablish a convention if you don't have one yet, and then stick to it. Make your changing and committing of files a structured process. This will lead to better results for your version history.  

6. <b>Push:</b>  \
    Once the desired number of commits have been made, you are ready to update the remote. So, we `push` our changes.

## Walk-through Exercise
### One iteration of the workflow
The goal of this section is to walk you through one iteration (from `fetch` to `push`) of the workflow to give you a better idea of the order of operations, the returns you see from git, and how to progress all the way to pushing a commit to the remote.

`>> git fetch`

`>> git pull`

`>> git status`
```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

`>> echo "# This is an empty Markdown file" > my_markdown.md`

`>> git status` \
The return from git tells us what branch we are on, and whether we are up to date with the origin (the remote repository), it also gives us a list of all untracked files. Our new file is not yet being tracked. We need to add it to the Staging Environment, and then commit it.
```
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        my_markdown.md

no changes added to commit (use "git add" and/or "git commit -a")
```
`>> git add my_markdown.md`
`>> git status`
```
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   my_markdown.md
```
`>> git commit -m "i created a new markdown file to practice committing and pushing"` \
Git informs us with the changes that have been made in this commit by returning:
```
[main f0431d9] i created a new markdown file to practice committing and pushing
 1 file changed, 1 insertion(+)
 create mode 100644 my_markdown.md
```
 
`>> git status` \
Git now tells us we are ahead of the origin (the remote) by 1 commit (the commit we just made). Now we need to update the remote by pushing our local committed changes.
```
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

no changes added to commit (use "git add" and/or "git commit -a")
```
`>> git push` \
Git gives us some information on how we have changed the remote. The last section shows the progression between the last commit `09301a4` to the new commit `c3a378b`, and which branches were involved (here just the `main` branch).
```
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.10 KiB | 1.10 MiB/s, done.
Total 6 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 2 local objects.
To github.com:DReGuerra/git_workshop.git
   09301a4..c3a378b  main -> main
```

