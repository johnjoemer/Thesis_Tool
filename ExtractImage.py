from moviepy.editor import VideoFileClip
import os

def extract_frames(videoFile, times, sequencePath):
    if not os.path.exists(sequencePath):
        os.makedirs(sequencePath)

    clip = VideoFileClip(videoFile)
    original_filename = os.path.splitext(os.path.basename(videoFile))[0]

    for i, t in enumerate(times):
        frame_path = os.path.join(sequencePath, f'{original_filename}_frame{i+1}.jpg')
        clip.save_frame(frame_path, t)

# movie = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CASME2_compressed/sub01/EP02_01f.avi'
# sequencePath = '/Users/jj/Documents/COLLEGE_DOCS/CASME2/CASME2_compressed/sub01/Extracted'
# clip = VideoFileClip(movie)
# times = [i/clip.fps for i in range(int(clip.fps * clip.duration))]
# extract_frames(movie, times, sequencePath)