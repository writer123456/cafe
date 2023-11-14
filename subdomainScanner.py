# importing module
import requests
import time


# function for scanning subdomains
def domain_scanner(domain_name,sub_domnames):
    

    # loop for getting URL's
    for subdomain in sub_domnames:

    # making url by putting subdomain one by one
        url = f"http://{subdomain}.{domain_name}"
    # using try catch block to avoid crash of the
    # program
    
        print('----URL after scanning subdomains----')
        try:
            # sending get request to the url
            requests.get(url)
            print("|Subdomain |"+(20*""+url+20*"")[:25]+"|is up|")
            # if after putting subdomain one by one url 
            # is valid then printing the url

            # if url is invalid then print down
        except requests.ConnectionError:
            #pass
            print("|Subdomain |"+(20*""+url+20*"")[:25]+"|is down|")
        

# main function
if __name__ == '__main__':

    # inputting the domain name
    dom_name = 'awesomeweb'
    # subdomains
    sub_dom=['menu','about','services','contactus','photos']
    # calling the function for scanning the subdomains every minute
    # and getting the url
    while True:
        print("*******************************")
        domain_scanner(dom_name,sub_dom)
        time.sleep(60)
	
