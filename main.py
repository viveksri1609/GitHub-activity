import sys
import requests

def get_activity(user:str):
    response = requests.get(f'https://api.github.com/users/{user}/events')
    return response.json()

def format_event(event):
    event_type = event["type"]
    repo = event["repo"]["name"]

    
    return f"{event_type} in {repo}"

def main():
    print(sys.argv)
    if len(sys.argv)!=2:
        print("Invalid Command")
        return 
    tasks = get_activity(sys.argv[1])
    print(f"\nRecent activity for {sys.argv[1]}:\n")

    for event in tasks[:10]:
        print("-", format_event(event))
    return

if __name__ == "__main__":
    main()