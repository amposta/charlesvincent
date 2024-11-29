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

# Initialize session state for posts, logo, and profile picture
if 'posts' not in st.session_state:
    st.session_state.posts = []
if 'logo' not in st.session_state:
    st.session_state.logo = None
if 'profile_picture' not in st.session_state:
    st.session_state.profile_picture = None

# Logo upload or path
logo = st.file_uploader("Upload your logo (jpg, jpeg, png):", type=["jpg", "jpeg", "png"], key="logo_uploader")

# Profile picture upload
profile_picture = st.file_uploader("Upload your profile picture (jpg, jpeg, png):", type=["jpg", "jpeg", "png"], key="profile_uploader")

# Create columns for logo, title, and profile picture (adjusted layout)
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    # Display the logo if uploaded
    if logo is not None:
        st.image(logo, caption="Logo", use_column_width=True)
        st.session_state.logo = logo  # Save to session state

with col2:
    # Set the title of the application
    st.title("Welcome to My Blog")

with col3:
    # Display profile picture if uploaded
    if profile_picture is not None:
        st.image(profile_picture, caption="Profile Picture", use_column_width=True)
        st.session_state.profile_picture = profile_picture  # Save to session state

# Create columns for user input
col1, col2 = st.columns([3, 1])

with col1:
    st.header("Create a New Blog Post")
    title = st.text_input("Post Title:")
    content = st.text_area("Post Content:", help="Content of your blog post. (Minimum 50 characters)")
    author = st.text_input("Your Name:", value="Charles Vincent B. Amposta")
    tags = st.text_input("Tags (comma-separated):", help="Tags for your post, e.g., 'Tech, Python'")

    # Validate the title and content
    if content and len(content) < 50:
        st.warning("Content should be at least 50 characters long.")
    if not title:
        st.warning("Title is required.")

    # Submit button for creating a blog post
    if st.button("Submit Post"):
        if title and content and author and len(content) >= 50:
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
            st.error("Please fill in all required fields and ensure content is at least 50 characters.")

# Display the blog posts
display_blog_posts(st.session_state.posts)

# Reset functionality with confirmation
if st.button("Reset All Posts"):
    if st.session_state.posts:
        confirm_reset = st.checkbox("Are you sure you want to reset all blog posts?")
        if confirm_reset:
            st.session_state.posts = []  # Clear all posts
            st.session_state.logo = None  # Clear logo
            st.session_state.profile_picture = None  # Clear profile picture
            st.success("All posts have been reset.")
            st.experimental_rerun()  # Reload the app after reset
    else:
        st.warning("There are no blog posts to reset.")
