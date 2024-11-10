This is a python script that takes two input files (one with followers and one with your following) 
and outputs a file containing a list of the people who you follow that don't follow you back.

The script takes advantage of the fact that when you highlight more than one follower at a time
in the browser, the profile picture is captured. When you go to paste the followers, there will be
entries that read "username's profile picture" because it got picked up while you were selecting
the user with your cursor. This solves the problem of having to differentiate between usernames
and display names, as the username is connected to the profile picture.

To use the script, open instagram on the web and highlight all of your followers, from bottom to top, 
ensuring you highlight all of the profile pictures. Paste this into a .txt file that you'll create 
in the same folder as the script. Do the same for your following, in a different .txt file.

Then, you're ready to run the script. It will write a new .txt file with the output data. There, 
you'll see the list of users who don't follow you back.
