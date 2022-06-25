# Git Version Control Workshop
André Guerra  
June/2022  
andre.guerra@mail.mcgill.ca  

## Contents
1. Overview
2. Prep
3. Fundamentals

## Overview
This is a markdown file (.md). Here, we will discuss some of the features of git version control and how we can use them to manage a github repository. 

## Prep
In order for us to go throug this workshop, you will need to make yourself a GitHub account. Once that's done, you can access my GitHub account at [DReGuerra](https://github.com/DReGuerra). There, you will need to navigate to the main page of this repository at [git_workshop](https://github.com/DReGuerra/git_workshop). Click on `Code` and select the tab `SSH`. Copy the link in the box that appears. You will need this link to "clone" this repository locally on your computer.

## Fundamentals of git Version Control
Some key concepts before we start:  
- <b>remote repository:</b> this is the master repository that is hosted by a cloud service. In our case here, it is hosted by GitHub, but there are other services that can offer similar capabilities (e.g., Atlassian's Bitbucket). The remote repository arquives all versions of the collection of files that are being tracked (part of the repository). The remote repository is often just referred to as "remote" and that's how we'll be referring to it from now on. The remote is the place where we "pull" from and "push" to.
- <b>local repository:</b> in order to work on files in a repository and to maintain version control, the first thing we do is "clone" the remote repository locally. In the previous step (Prep) above, you accessed the remote repository of this workshop and you cloned yourself a copy of it locally. This made you a local copy of the remote. This is referred to as the "local".
- <b>fetch:</b>
- <b>pull:</b>
- <b>push:</b>
- <b>stage:</b>
- <b>commit:</b>

### Workflow

The overall workflow:  
fetch $\rightarrow$ pull $\rightarrow$ make changes to files $\rightarrow$ stage changes $\rightarrow$ commit changes (with a message) $\rightarrow$ push

1. <b>fetch:</b> 
    Before beginning to work on any of our local files we want to query the remote to see if they have been updatated since the last time we worked on them. In a multi-member project, someone else may have done some work on files while you were working on something else. So, we `fetch`:  
    `>> git fetch`  

    After fetching, our local repository now has information on whether the remote has changed, but we (the user) don't know what these changes were. So, we ask for the `status`:  
    `>> git status`  

    The return from this command will give you information on what the changes were (if there were any), and how many commits we are ahead or behind. 
2. <b>pull:</b> 
    If we are behind the remote, we want to `pull` these changes so that we can start working on the latest version of all files in the repository.  
    `>> git pull`  

3. <b>make changes:</b> 
    Now we are ready to make changes to the files.  

4. <b>stage changes:</b> 
    Once enough changes have been made that you are satisfied that the files are now in a state in which their version should be snapshot, then we need to commit thse changes. BUT before commiting anything, we need to `stage` the changes. We can stage multiple files at once (if we want to commit them to the same commit number):  
    `>> git add python_script.py 4_figures/plot.png markdown_file.md`  

5. <b>commit changes:</b> 
    Once our changed files have been staged, we can commit them. In every commit, we want to add a message that is descriptive of the changes that were made and/or the reasons for them. Commit messages tend to follow conventions that may be set by you if this is your own repository, or your project leader if the repository that you are working on is managed by someone else (or a company). We can make multiple commits as we work on the files. How often, how many files at a time, and other convention type questions are dependent on how you (or your group) want to manage the repository. It is advisable to stablish a convention if you don't have one yet, and then stick to it. Make your changing and commiting of files a structured process. This will lead to better results for your version history.  

6. <b>push:</b> 
    Once the desired number of commits have been made, you are ready to update the remote. So, we `push` our changes.
