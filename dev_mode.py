import os
import time


def check_dev_mode():
    if os.getenv("LIFECORE_DEV_MODE") == "1":
        print("🔧 === LIFECORE DEVELOPMENT MODE ENABLED ===")
        print("⚠️  PHYSICAL HARDWARE DISABLED - TESTING ONLY")
        print("⚠️  No real motors or sensors active")
        print("========================================")
        # Add developer PIN check here if needed
        return True
    else:
        return False


# Example usage at startup
if __name__ == "__main__":
    if check_dev_mode():
        print("Running in safe simulation mode...")
        # Run tests here
    else:
        print("Production mode - checking physical safety...")
        # Normal production checks
