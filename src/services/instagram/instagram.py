import instaloader

from logger.logger import LOG


def load_instagram_micro_influenceur():

    LOG.info("Loading instagram profiles ...")    
    
    
    L = instaloader.Instaloader()
    

    hashtag = "modeethique"
    num_posts = 5  
    potential_influencers = []

    for post in L.get_hashtag_posts(hashtag):
        if num_posts <= 0:
            break
        
        profile = post.owner_profile

        # 1k / 50k subs
        if 1000 <= profile.followers <= 50000:
            potential_influencers.append(profile)

        num_posts -= 1

    print(potential_influencers)