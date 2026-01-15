import requests

def main():
    BASE_URL = 'https://jsonplaceholder.typicode.com/todos'

    # 1) Get the 200 most recent TODOs
    try: 
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        
        if isinstance(data, list):
            first_200 = data[:200]
            print(f'First 200 TODOs: {first_200}')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        
    print()
        
    # 2) Create a todo
    try:
        todo = {
            'title': 'Complete coding test',
            'completed': False 
        }
        
        response = requests.post(BASE_URL, json=todo)
        response.raise_for_status()
        print('POST Request submitted succesfully!')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    print()
    
    # 3) Delete a TODO given an ID
    try:
        todo_id = input('Enter ID to DELETE: ')
        if not todo_id.isdigit():
            print("Error: Invalid ID provided")
        
        response = requests.delete(f"{BASE_URL}/{todo_id}")
        response.raise_for_status()
        print('DELETE Request submitted succesfully!')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()