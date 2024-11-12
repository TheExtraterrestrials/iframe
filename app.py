import streamlit as st
import validators

def main():
    # Set page config
    st.set_page_config(
        page_title="Website Viewer",
        page_icon="🌐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS to make iframe full height
    st.markdown("""
        <style>
        .stApp {
            margin: 0;
            padding: 0;
        }
        iframe {
            height: 85vh !important;
            width: 100%;
            border: none;
        }
        .warning {
            color: #ff4b4b;
            font-size: 14px;
            margin-top: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and description
    st.title("Website Viewer")
    
    # URL input
    url = st.text_input("Enter website URL (including https://)", key="url_input")
    
    # Display iframe when URL is provided
    if url:
        if not url.startswith(('http://', 'https://')):
            st.error("Please include http:// or https:// in the URL")
        elif not validators.url(url):
            st.error("Please enter a valid URL")
        else:
            try:
                # Create iframe HTML
                iframe_html = f'<iframe src="{url}" frameborder="0" allowfullscreen="true" width="100%"></iframe>'
                st.markdown(iframe_html, unsafe_allow_html=True)
                
                # Warning message
                st.markdown("""
                    <div class="warning">
                        Note: Some websites may not load due to iframe restrictions or security policies.
                    </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error loading website: {str(e)}")

if __name__ == "__main__":
    main()
