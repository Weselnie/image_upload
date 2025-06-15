import schedule
import time

from drive_to_git import download_images, generate_image_index, git_commit_and_push

def run_pipeline():
    print("Running image sync...")
    download_images()
    generate_image_index('images', 'images.json')
    git_commit_and_push()
    print("Pipeline completed.")

# Schedule it to run every 10 minutes
schedule.every(10).minutes.do(run_pipeline)

print("Scheduler started. Running every 10 minutes.")
while True:
    schedule.run_pending()
    time.sleep(1)
