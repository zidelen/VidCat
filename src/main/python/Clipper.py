from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys

def combine_videos(video1_path, video2_path, output_path):
    # Load clips
    clip1 = VideoFileClip(video1_path)
    clip2 = VideoFileClip(video2_path)

    # Concatenate the clips
    final_clip = concatenate_videoclips([clip1, clip2])

    # Write to file
    final_clip.write_videofile(output_path, codec='libx264')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python Clipper.py <video1_path> <video2_path> <output_path>")
        sys.exit(1)

    video1_path = sys.argv[1]
    video2_path = sys.argv[2]
    output_path = sys.argv[3]

    # Combine the videos
    combine_videos(video1_path, video2_path, output_path)

