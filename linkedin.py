import streamlit.components.v1 as components

def linkedin_profiles(user1, user2, user3, user4):
    components.html(f"""
    <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
    <div style="display: flex; justify-content: center; align-items: center; margin: 20px;">
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="{user1}" data-version="v1"></div>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="{user2}" data-version="v1"></div>
    </div>
    <div style="display: flex; justify-content: center; align-items: center; margin: 20px;">
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="{user3}" data-version="v1"></div>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="{user4}" data-version="v1"></div>
    </div>
    """,
    height=540)