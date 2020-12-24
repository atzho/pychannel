import os, random

print("Retrieving videos...")
videos = os.listdir("./Videos")
print("Successfully retrieved videos!")

print("Playing videos...")

recent = []
while True:
    video_name = random.choice(videos)
    video_path = os.path.abspath(os.path.join("Videos", video_name))

    if not video_name in recent:
        recent.append(video_name)
        if len(recent) > 3:
            recent.pop(0)
        print("Playing: " + video_name)
        os.system("ffplay -autoexit " + "\"" + video_path + "\"")