import json
import redis

class Blog:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

    def create_post(self, post_id, title, content):
        post = {'title': title, 'content': content}
        self.redis_client.set(f'post:{post_id}', json.dumps(post))
        print("Post created successfully.")

    def get_post(self, post_id):
        post_data = self.redis_client.get(f'post:{post_id}')
        if post_data:
            post = json.loads(post_data.decode('utf-8'))
            return post
        else:
            print("Post not found.")
            return None

    def delete_post(self, post_id):
        result = self.redis_client.delete(f'post:{post_id}')
        if result == 1:
            print("Post deleted successfully.")
        else:
            print("Post not found.")

if __name__ == "__main__":
    blog = Blog()

    while True:
        print("\n1. Create a new post\n2. View a post\n3. Delete a post\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            post_id = input("Enter post ID: ")
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            blog.create_post(post_id, title, content)
        elif choice == '2':
            post_id = input("Enter post ID to view: ")
            post = blog.get_post(post_id)
            if post:
                print(f"\nTitle: {post['title']}\nContent: {post['content']}")
        elif choice == '3':
            post_id = input("Enter post ID to delete: ")
            blog.delete_post(post_id)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
