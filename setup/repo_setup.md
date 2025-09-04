# Repository Setup Guide

This guide will help you setup the tutorial repository that we will use submitting and reviewing of assignments

---

## 1. Clone Repository

- Select a location where all the tutorial files will be added. We will call this $LEARN_SPACE in this doc
- Open Cmd prompt and traverse to learn space by running `cd <$LEARN_SPACE>`
- Run Cmd: `git clone git@github.com:Anshuman04/ScraPY.git`

You will see a new folder created inside `$LEARN_SPACE`, which is named `ScraPy`

## 2. Open Project in VS Code

- Open VS Code
- Click on `File` -> `Open Folder` from top left corner
- Browse to `$LEARN_SPACE/ScraPY`
- Trust the authors, if asked

Now from here, any command that needs to be run on cmd promopt will be run on VS Code Terminal.
VS Code Terminal can be found on top left `Terminal` -> `New Terminal`

## 3. Create github account

- Goto [Github](https://github.com/)
- Sign up for an account using personal gmail account

## 4. Create SSH API Keys
**Dont try to understand this section. This is required for authentication & authorization**

- Open VS Code terminal if not open
- Run `git config user.name "<github_username>"`. Put your actual github username in place of <...>
- Run `git config user.email "<github_email_id>"`. Put your actual gmail account used while sign up in place of <...>
- Get User profile
    - **Windows**: Run `$env:USERPROFILE`. Copy the output and use it in place of `$USER`
    - **MacOS**: Run `echo $HOME`. Copy the output and use it in place of `$USER`
- Create SSH Keys
    - **Windows**: Run `ssh-keygen -t ed25519 -C "github_email_id" -f $USER\.ssh\id_ed25519_github`. Press Enter 3 times here. You will see some random encryption characters on your screen
    - **MacOS**: Run `ssh-keygen -t ed25519 -C "<github_email_id>" -f $USER/.ssh/id_ed25519_github`. Press Enter 3 times here. You will see some random encryption characters on your screen
- Print and copy public keys
    - **Windows**: Run `Get-Content $USER\.ssh\id_ed25519_github.pub` and copy the content. **Remember to replace $USER**
    - **MacOS**: Run `cat $USER\.ssh\id_ed25519_github.pub` and copy the content. **Remember to replace $USER**

## 5. Add SSH keys to your github account

- Goto [Github](https://github.com/) and login
- From Top right corner, Click on `Profile` -> `Settings`
- From left Menu, click on `SSH and GPG keys` from `Access` section
- Click green button that says `New SSH Key`
- Put anything in Title
- Paste the SSH keys copied in Step #4 in `Key`
- Click green button `Add SSH Key`

## 6. Edit SSH Config

- Open SSH Config 
    - **Windows**: Run `code $USER\.ssh\.config`. Replace `$USER`
    - **MacOS**: Run `code $USER/.ssh/.config`. Replace `$USER`
- Add below lines to the file that just opened. **Note:** If your file is empty, that is fine just copy paste below lines. But if your file has already some content make sure you paste at the end of file. **PITFALL:** Make sure the indentation stays as it is
```python
Host github.com
  HostName github.com
  User git
  IdentityFile $USER\.ssh\id_ed25519_github
  IdentitiesOnly yes
```
**Remember to replace $USER**
**Remember to change orientation of slach for MacOS**
- Save (Ctrl+S) and close te file now

## 7. Test the E2E setup

- Run `ssh -T git@github.com`
You should see below output or similar
```bash
Hi <Username>! You've successfully authenticated, but GitHub does not provide shell access.
```

**Congratulations!! Your repository is now fully setup.**
