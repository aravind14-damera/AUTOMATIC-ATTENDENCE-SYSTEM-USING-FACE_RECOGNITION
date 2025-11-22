from supabase import create_client, Client

# Replace with your actual Supabase credentials
SUPABASE_URL ="https://zoykcfdrjmdvjdgdglwr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpveWtjZmRyam1kdmpkZ2RnbHdyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM4MjIyMTUsImV4cCI6MjA3OTM5ODIxNX0.fnRnSpt_dvDPspORRtBJQMnr_dJcB4D9p-J1weqKupA"# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ✅ Corrected Student Data (List of Dictionaries)
data = [
    {
        "registration_number": "AP23110011641",
        "name": "kilari Joshitha",
        "major": "Python",
        "starting_year": 2023,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2025-03-20 00:55:20"
    }
]

# ✅ Insert Data into Supabase
response = supabase.table("students").insert(data).execute()

# ✅ Check Response
if response.data:
    print("✅ Data inserted successfully:", response.data)
else:
    print("⚠️ Failed to insert data, Error:", response.error)
