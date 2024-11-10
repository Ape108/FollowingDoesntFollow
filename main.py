import os

def pullUsernames(lines:list) -> list:
    usernames = []
    for line in lines[:]:
        if "profile picture" in line:
            split_line = line.split("'")
            username = split_line[0]
            usernames.append(username)
    return usernames



if __name__ == "__main__":

    followers_filename = "followers.txt"
    followers_count = int(input("How many followers do you have?\n"))
    following_filename = "following.txt"
    following_count = int(input("How many people are you following?\n"))

    try:
        followers = open(followers_filename, "r")
        following = open(following_filename, "r")

        followers_lines = followers.readlines()
        following_lines = following.readlines()
        followers_usernames = pullUsernames(followers_lines)
        following_usernames = pullUsernames(following_lines)

        print(f"{len(followers_usernames)} / {followers_count} Followers Retrieved")
        print(f"{len(following_usernames)} / {following_count} Following Retrieved")

        with open("dont-follow-back.txt", "r") as outfile1:
            if os.stat("dont-follow-back.txt").st_size == 0:
                doesntfollow = set()
            else:
                doesntfollow = set(outfile1.readlines())
            for user in following_usernames:
                if (user not in followers_usernames) and (user not in doesntfollow):
                    doesntfollow.add(user + "\n")
            print(f"Length of list: {len(doesntfollow)}")
        with open("dont-follow-back.txt", "w") as outfile1:
                dflist = list(doesntfollow)
                dflist.sort()
                outfile1.writelines(dflist)
                print(f"Follower data successfully uploaded to {outfile1.name}.")   

    except (FileNotFoundError, IOError) as e:
        print(f"{e} : Please Try Again.")
    except:
        print("Unknown Error. Please Try Again.")
    finally:
        followers.close()
        following.close()

    except (FileNotFoundError, IOError) as e:
        print(f"{e} : Please Try Again.")
    #except:
        #print("Unknown Error. Please Try Again.")
    
