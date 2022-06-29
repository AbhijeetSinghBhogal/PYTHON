import praw

username = "StarLord2098"
password = "@bhij33t#2098"

var = praw.Reddit(user_agent = "/u/" + username + " deleting all saved posts....")

var.login(username, password, disable_warning = True)

for saved in var.user.get_saved(limit = 1000):
    var.get_submission(str(saved.permalink)).unsave()
    
# Getting "MissingRequiredAttributeException: Required configuration setting 'client_id' missing"

# The error is caused from a missing client_id (which is your unique API key and secret for the Reddit API) in your praw.ini file or in your Python script.