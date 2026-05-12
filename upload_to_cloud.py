import cloudinary
import cloudinary.uploader
import os

# --- CONFIGURATION ---
# Replace these with your actual keys from settings.py
cloudinary.config(
    cloud_name="dmxziek2g",
    api_key="663921886894229",
    api_secret="3LWsKOby2pOtlZc3bLWnCE35SWI"
)

# Replace with the actual path to your APK on your laptop
# Note: Use forward slashes / even on Windows
APK_PATH = "C:/Users/ephia/stock/stock_app/build/app/outputs/flutter-apk/Jackal POS.apk"

def upload_apk():
    if not os.path.exists(APK_PATH):
        print(f"Error: File not found at {APK_PATH}")
        return

    print(f"🚀 Starting upload for: {os.path.basename(APK_PATH)}")
    
    try:
        # We specify resource_type="raw" so Cloudinary doesn't treat it as an image
        response = cloudinary.uploader.upload(
            APK_PATH,
            resource_type="raw",
            use_filename=True,
            unique_filename=False
        )
        
        print("\n✅ UPLOAD SUCCESSFUL!")
        print(f"Direct Download URL: {response['secure_url']}")
        print("\nCopy the URL above and paste it into your apk_url field in Django Admin.")

    except Exception as e:
        print(f"❌ Upload failed: {str(e)}")

if __name__ == "__main__":
    upload_apk()