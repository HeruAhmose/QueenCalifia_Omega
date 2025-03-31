
def upload_to_drive(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
        print("✅ Log file ready for sync:", len(lines), "entries")
        return "✅ Synced successfully (simulated)."
    except Exception as e:
        return f"❌ Sync failed: {str(e)}"
