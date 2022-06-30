import praw

myUsername = ""
myPassword = ""

var = praw.Reddit(user_agent = "/u/" + myUsername + " deleting all saved posts....")

var.login(myUsername, myPassword, disable_warning = True)

for saved in var.user.get_saved(limit = 1000):
    var.get_submission(str(saved.permalink)).unsave()
    
# Getting "MissingRequiredAttributeException: Required configuration setting 'client_id' missing"

# The error is caused from a missing client_id (which is your unique API key and secret for the Reddit API) in your praw.ini file or in your Python script.