import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3, col4 = st.columns(4)
    fs = FewShotPosts()
    with col1:
        selected_tag = st.selectbox("Title", options=fs.get_tags())
    with col2:
        selected_length = st.selectbox("Length", options=length_options)
    with col3:
        selected_language = st.selectbox("Length", options=language_options)
    with col4:
        selected_influencer = st.selectbox("Influencer", options=fs.get_influencers())

    if st.button("Generate Post"):
        reference_posts = fs.get_posts_by_influencer(selected_influencer)
        post = generate_post(selected_length, selected_language, selected_tag, selected_influencer)
        st.write(post)


if __name__ == "__main__":
    main()