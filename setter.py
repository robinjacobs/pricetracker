#import argparse

#parser =  argparse.ArgumentParser(description='Set website to track price')
from prompt import Prompt

URLS_FILE_PATH = 'pricetrack/price_urls.txt'

def show_all_tracked_websites():
    with open(URLS_FILE_PATH) as f :
        all_urls = f.readlines()
    number_urls = len(all_urls)
    print(f"Number of websites : {number_urls} ")
    print("The following websites are currently tracked :")
    print("----------------------------------------------")
    for url in all_urls :
        print(url)

def add_new_price_to_track():
    print("Enter the website url of the price to track :")
    website_url = input("Url :")
    print("Enter xpath")
    print("Not yet implemented")
    with open(URLS_FILE_PATH,'a') as f :
        f.write(website_url + '\n')
    print("Saved")


if __name__ == "__main__":
    print('Launching Setter Method')
    print('What do you want to do ?')

    all_tracked_websites_node =  Prompt(prompt_calling_str='Show all tracked websites', prompt_question='Show all websites currently tracked',action=show_all_tracked_websites)
    new_price_tracker_node = Prompt(prompt_calling_str='Add new price to track', prompt_question='Add new website to track',action=add_new_price_to_track)

    start_node = Prompt(children_nodes= [all_tracked_websites_node, new_price_tracker_node], prompt_calling_str='Launched setter method for pice tracker', prompt_question="Choose your action")
    start_node()
    


