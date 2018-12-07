from moviepy.editor import *
import sys

def main():
    num_copies = 10
    sync_point = 134
    delay = 1
    base_clip = VideoFileClip('input.webm', buffer_all=True)
    clips = []
    for i in range(num_copies):

        # We want the clip to reach sync_point
        # after sync_point seconds have passed
        # (to make it sync up with the first clip)

        # sync_point = (sync_point * speed) - delay
        # solve for 'speed'

        # When delay is 0, speed will be 1, which corresponds
        # to playing at normal speed
        speed = (sync_point + (i * delay)) / sync_point
        clip = base_clip\
                .set_start(delay * i)\
                .fx(vfx.speedx, speed)

        clips.append(clip)

    print(clips)
    final_clip = clips_array([clips])
    final_clip.write_videofile(sys.argv[1], threads=6, progress_bar=True)

if __name__ == "__main__":
    main()
