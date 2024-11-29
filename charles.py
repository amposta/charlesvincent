import streamlit as st
from datetime import datetime

# Function to display all blog posts
def display_blog_posts(posts):
    if posts:
        st.write("### Blog Posts:")
        for i, post in enumerate(posts):
            st.write(f"**Post {i + 1}:**")
            st.write(f"**Title:** {post['title']}")
            st.write(f"**Content:** {post['content']}")
            st.write(f"**Author:** {post['author']}")
            st.write(f"**Date:** {post['date']}")
            if post['tags']:
                st.write(f"**Tags:** {', '.join(post['tags'])}")
            st.write("---")
    else:
        st.write("No blog posts available.")

# Initialize session state for posts
if 'posts' not in st.session_state:
    st.session_state.posts = []

# Logo upload or path
logo = st.file_uploader("Upload your logo (jpg, jpeg, png):", type=["jpg", "jpeg", "png"], key="logo_uploader")

# Create columns for logo, title, and profile picture
col1, col2, col3 = st.columns([3, 6, 4])

with col1:
    # Display the logo if uploaded
    if logo is not None:
        st.image(logo, caption="Logo", use_column_width=True)

with col2:
    # Set the title of the application
    st.title("Welcome to My Blog")

with col3:
    # Profile picture upload
    st.header("Profile Picture")
    profile_picture = st.file_uploader("Upload your profile picture (jpg, jpeg, png):", type=["jpg", "jpeg", "png"])

    if profile_picture is not None:
        st.image(profile_picture, caption="Profile Picture", use_column_width=True)

# Create columns for user input
col1, col2 = st.columns([3, 1])

with col1:
    st.header("Create a New Blog Post")
    title = st.text_input("Post Title:")
    content = st.text_area("Post Content:")
    author = st.text_input("Your Name:", value="Charles Vincent B. Amposta")
    tags = st.text_input("Tags (comma-separated):")  # New field for tags

    # Submit button for creating a blog post
    if st.button("Submit Post"):
        if title and content and author:
            # Create a new blog post
            new_post = {
                'title': title,
                'content': content,
                'author': author,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'tags': [tag.strip() for tag in tags.split(',')] if tags else []  # Handle tags
            }
            st.session_state.posts.append(new_post)  # Add the new post to the session state
            st.success("Blog post submitted successfully!")
        else:
            st.error("Please fill in all fields before submitting.")

# Display the blog posts
display_blog_posts(st.session_state.posts)

# Reset functionality
if st.button("Reset"):
    st.session_state.posts = []  # Clear all posts
    st.session_state.logo = None  # Clear logo
    st.session_state.profile_picture = None  # Clear profile picture
    st.rerun()  
