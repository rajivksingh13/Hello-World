import streamlit as st

def main():
    st.title("Hello, World!")
    st.write("Welcome to your first Streamlit app.")
    
    # Add a text input widget
    user_input = st.text_input("Enter some text:")
    
    # Display the user input
    if user_input:
        st.write(f"You entered: {user_input}")

if __name__ == "__main__":
    main()
