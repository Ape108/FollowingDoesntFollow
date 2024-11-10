
def pullUsernames(lines:list) -> list:
    usernames = []
    for line in lines[:]:
        if "profile picture" in line:
            split_line = line.split("'")
            username = split_line[0]
            usernames.append(username)
    return usernames



if __name__ == "__main__":
    followers_filename = input("What is the name of the file containing your followers?\n")
    following_filename = input("What is the name of the file containing your following?\n")
    try:
        followers = open(followers_filename, "r")
        following = open(following_filename, "r")
        
        followers_lines = followers.readlines()
        following_lines = following.readlines()

        followers_usernames = pullUsernames(followers_lines)
        following_usernames = pullUsernames(following_lines)

        with open("dont-follow-back.txt", "w") as outfile1:
            doesntfollow = []
            for user in following_usernames:
                if user not in followers_usernames:
                    doesntfollow.append(user + "\n")
            outfile1.write("These users do not follow you back:\n\n")
            outfile1.writelines(doesntfollow)
            print(f"Follower data successfully uploaded to {outfile1.name}.")   
        
        followers.close()
        following.close()

    except (FileNotFoundError, IOError) as e:
        print(f"{e} : Please Try Again.")
    #except:
        #print("Unknown Error. Please Try Again.")
    
