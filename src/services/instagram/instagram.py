import instaloader

from logger.logger import LOG


def load_instagram_micro_influenceur():

    LOG.info("Loading instagram profiles ...")    
    
    
    L = instaloader.Instaloader()
    

    hashtag = "police"
    num_posts = 5  # Nombre de publications à examiner
    potential_influencers = []

    for post in L.get_hashtag_posts(hashtag):
        if num_posts <= 0:
            break
        
        profile = post.owner_profile

        # Ici, définissez vos critères pour un micro-influenceur.
        # Par exemple, vérifiez si le nombre d'abonnés est entre 1k et 50k :
        if 1000 <= profile.followers <= 50000:
            potential_influencers.append(profile)

        num_posts -= 1

    print(potential_influencers)