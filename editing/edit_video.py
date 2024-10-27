from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load video clips
clip1 = VideoFileClip("scenes/scene1.mp4")
clip2 = VideoFileClip("scenes/scene2.mp4")

# Concatenate clips
final_clip = concatenate_videoclips([clip1, clip2])

# Save the final edited video
final_clip.write_videofile("output/edited_film.mp4")
