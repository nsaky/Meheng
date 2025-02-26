import customtkinter as ctk

from Frontend.setup_view_user_ids import setup_view_user_ids
from Frontend.setup_login_activities import setup_login_activities
from Frontend.setup_user_chat_history_for_admin import setup_user_chat_history_for_admin
from Frontend.setup_ban_user import setup_ban_user
from Frontend.setup_review_user import setup_review_user
from Frontend.setup_create_user_account import setup_create_user_account

def setup_manage_users(tab, admin_id):
    # Create a tabview inside the Manage Users tab
    manage_users_tabview = ctk.CTkTabview(tab)
    manage_users_tabview.pack(pady=10, fill="both", expand=True)

    # Add tabs for each functionality
    tab_view_user_ids = manage_users_tabview.add("View User IDs")
    tab_view_login_activities = manage_users_tabview.add("Login Activities")
    tab_view_user_chats = manage_users_tabview.add("User Chats")
    tab_review_user_accounts = manage_users_tabview.add("Review Accounts")
    tab_ban_user = manage_users_tabview.add("Ban User")
    tab_create_user = manage_users_tabview.add("Create User")

    # Setup for each tab, placeholder text for now

    setup_view_user_ids(tab_view_user_ids, admin_id)
    setup_login_activities(tab_view_login_activities, admin_id)
    setup_user_chat_history_for_admin(tab_view_user_chats, admin_id)
    setup_review_user(tab_review_user_accounts, admin_id)
    setup_ban_user(tab_ban_user,admin_id)
    setup_create_user_account(tab_create_user,admin_id)

