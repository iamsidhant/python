
from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.kcq4zop.mongodb.net/")

print(client)


def add_videos():
    pass

def list_videos():
    pass

def update_video():
    pass

def delete_video():
    pass


def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. delete video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to update: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()        