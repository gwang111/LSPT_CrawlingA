# The Best Greatest Yummy Delicious Cooking Book Website

## Technical Notes:

To create a symbolic link, use the command:
`ln -s /original/path /link/path`. 
This enables us to store the git repo for this in Documents/GitHub but then allows xampp to access through htdocs.

For example, I ran the command
`ln -s ~/Documents/GitHub/ITWS-Cooking-Site ./htdocs/cooking` from my xampp root.

Now ideally that would work. By default, xampp is set up to follow symbolic links, however on MacOS I keep getting 403 errors. I've stuck the whole directory in the htdocs folder. Makes me sad. Maybe it'll work on other platforms.

I have decided to call the root folder for this project `cooking` instead of `ITWS-Cooking-Site` because I decided the latter was too many characters :)

This modification can be made using a link or simply by renaming your local git folder. I renamed the folder locally.

Reminder that (on unix systems) the permissions for files might need to be changed. The easy command to fix this is `chmod 777 *` to fix permissions for all in the current directory, or `chmod -R 777 /folder/` to fix for a target folder and all children.

## Links:

[Link to proposal document (google doc)](https://docs.google.com/document/d/1qiWNtK0yyhVXeGzrAHUiPBq141aeGRWyzeDWMErTBik)

[Link to mockups (balsamiq project)](https://balsamiq.cloud/si5a00/pexvmn6)
