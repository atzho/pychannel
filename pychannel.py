import os, random

print("Retrieving videos...")
videos = os.listdir("./Videos")
print("Successfully retrieved videos!")

print("Playing videos...")

recent = []
keep_playing = True
while keep_playing:
    video_name = random.choice(videos)
    video_path = os.path.abspath(os.path.join("Videos", video_name))

    if not video_name in recent:
        recent.append(video_name)
        if len(recent) > 3:
            recent.pop(0)
        print("Playing: " + video_name)
        keep_playing = 0 == os.system("ffplay -autoexit -fs " + "\"" + video_path + "\"")