import customtkinter as ctk
from Backend.admin_view_chats import admin_view_chats
from Backend.establish_backend import establish_backend
import tkinter.messagebox as messagebox

# Global variables for date entry fields
start_date_entry = None
end_date_entry = None

def setup_admin_chat_history(tab, admin_id):
    global start_date_entry, end_date_entry  # Declare global variables here

    # Create TabView for "All Chats" and "By Date"
    tabview_chat_history = ctk.CTkTabview(tab)
    tabview_chat_history.pack(pady=20, padx=20, fill="both", expand=True)

    # Add tabs for "All Chats" and "By Date"
    tab_all_chats = tabview_chat_history.add("All Chats")
    tab_by_date = tabview_chat_history.add("By Date") 

    # Display "All Chats" initially
    fetch_chats(admin_id, tab_all_chats, "all")

    # Setup "By Date" tab with date inputs and reset functionality
    setup_by_date_tab(tab_by_date, admin_id)

# Function to setup the "By Date" tab with input fields
def setup_by_date_tab(tab, admin_id):
    for widget in tab.winfo_children():
        widget.destroy()
    global start_date_entry, end_date_entry  # Declare global variables here

    # Label and inputs for date range
    start_date_label = ctk.CTkLabel(tab, text="Start Date (YYYY-MM-DD):")
    start_date_label.pack(pady=5)
    start_date_entry = ctk.CTkEntry(tab)  # Initialize the global variable
    start_date_entry.pack(pady=5)

    end_date_label = ctk.CTkLabel(tab, text="End Date (YYYY-MM-DD):")
    end_date_label.pack(pady=5)
    end_date_entry = ctk.CTkEntry(tab)  # Initialize the global variable
    end_date_entry.pack(pady=5)

    # Submit button to fetch chats by date
    fetch_button = ctk.CTkButton(tab, text="Fetch Chats", command=lambda: fetch_chats(admin_id, tab, "date", start_date_entry.get(), end_date_entry.get()))
    fetch_button.pack(pady=10)

    # Add a reset button to clear the date inputs
    reset_button = ctk.CTkButton(tab, text="Reset Dates", command=lambda: reset_date_inputs())
    reset_button.pack(pady=5)

# Function to reset date entries in "By Date" tab
def reset_date_inputs():
    start_date_entry.delete(0, 'end')  # Clear the start date input
    end_date_entry.delete(0, 'end')  # Clear the end date input

# Function to fetch and display chats
def fetch_chats(admin_id, tab, filter_type, start_date=None, end_date=None):
    # Clear previous chat table (if any)
    for widget in tab.winfo_children():
        widget.destroy()

    conn, cursor = establish_backend()
    if not conn or not cursor:
        messagebox.showerror("Database Error", "Failed to connect to database.")
        return

    try:
        if filter_type == "all":
            chats=admin_view_chats(admin_id)
        elif filter_type == "date" and start_date and end_date:
            chats=admin_view_chats(admin_id,start_date,end_date)

        if chats:
            # Create table structure with headers
            table_frame = ctk.CTkFrame(tab)
            table_frame.pack(fill="both", expand=True)

            # Create scrollable frame
            scroll_frame = ctk.CTkScrollableFrame(table_frame, height=400)  # Set height to limit scrolling area
            scroll_frame.pack(fill="both", expand=True)

            # Table headers using grid layout for proper alignment
            header_frame = ctk.CTkFrame(scroll_frame)
            header_frame.grid(row=0, column=0, sticky="w")

            headers = ["S.No.", "Date & Time", "Query", "Response"]
            header_widths = [50, 150, 300, 300]  # Set width for each column
            for col, (header, width) in enumerate(zip(headers, header_widths)):
                label_header = ctk.CTkLabel(header_frame, text=header, font=ctk.CTkFont(size=14, weight="bold"))
                label_header.grid(row=0, column=col, padx=10, pady=10)
                header_frame.columnconfigure(col, weight=1)  # Ensure equal weight for alignment

            # Populate chat history in grid format for proper alignment
            for i, chat in enumerate(chats, start=1):
                query, response, log_time = chat
                log_time = log_time.strftime('%Y-%m-%d %H:%M:%S')

                # Display in multiline format with grid layout
                label_sno = ctk.CTkLabel(scroll_frame, text=str(i))
                label_sno.grid(row=i, column=0, padx=10, pady=10)

                label_log_time = ctk.CTkLabel(scroll_frame, text=log_time)
                label_log_time.grid(row=i, column=1, padx=10, pady=10)

                label_query = ctk.CTkLabel(scroll_frame, text=query, wraplength=280, justify="left")
                label_query.grid(row=i, column=2, padx=10, pady=10, sticky="w")

                label_response = ctk.CTkLabel(scroll_frame, text=response, wraplength=280, justify="left")
                label_response.grid(row=i, column=3, padx=10, pady=10, sticky="w")
            
            if start_date and end_date:
                # Add a button to allow reselecting the dates after fetching chats
                reselect_button = ctk.CTkButton(tab, text="Reselect Dates", command=lambda: setup_by_date_tab(tab, admin_id))
                reselect_button.pack(pady=10)

        else:
            messagebox.showinfo("No Chats", "No chat history found for the given filters.")
            setup_by_date_tab(tab, admin_id)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while fetching chat history: {e}")

    finally:
        conn.close()
