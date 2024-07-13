subreddit = "funny" # exclude 'r/', you can combine multiple subreddits with '+'. Ex: "funny+cars"
database = 'database.txt' # local text database file that ensures no duplicate videos get processed.

# Additional setup information for authenticating with the Reddit API can be found in the Reddit API documentation.
# Check this video: https://youtu.be/NRgfgtzIhBQ?t=50

# Using this config file alone should be able to get you going without further modification.
reddit_login = {
	'client_id': 'YnYwz0znuWaZz15D3YS-0Q',
	'client_secret': '__kNNUSuPyQeWn54NSsTmNwX_0GAxw',
	'user_agent': 'Rahu',
	'username': 'The-Meme-Thief6969',
    'password': 'F0otball'
}


youtube = {
	'tags': '',
	'category': 23,  # has to be an int, more about category below
	'status': 'public'  # {public, private, unlisted}
}
# Note that by default, public isn't available unless you go through an audit. Checkout: https://support.google.com/youtube/contact/yt_api_form

video = {
	'dimensions': (1080, 1920),  # (horizontal, vertical) or None (not a string but literal) to upload the original clip as is.
	'blur': False  # blur non-perfect-fit clip
}

# for category: has to be an int, refer to YouTube Data 4 API's documentation, but as of Jan 2022,
# checkout https://techpostplus.com/youtube-video-categories-list-faqs-and-solutions/
