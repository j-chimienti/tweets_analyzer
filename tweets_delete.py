from tweepy import Cursor
from lib.tweepy import twitter_api


def delete_tweet(_id):
    try:
        twitter_api.destroy_status(_id)
        print("Deleted:", _id)
    except:
        print("Failed to delete:", _id)


def main():

    for status in Cursor(twitter_api.user_timeline).items():
        delete_tweet(status.id)


if __name__ == '__main__':
    main()
