from moviepy.editor import *
from random import choice
import os
import argparse


def get_random_file(directory):
    res = []
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            res.append(path)
    if len(res) == 0:
        raise Exception(f'no files in the folder {directory}')
    else:
        return choice(res)


def unite_and_cut(path1, path2, start, video_len):
    video_1 = VideoFileClip(f'{path1}/{get_random_file(path1)}').subclip(start,start+video_len)
    video_2 = VideoFileClip(f'{path2}/{get_random_file(path2)}').subclip(start,start+video_len)
    united_clip = concatenate_videoclips([video_1, video_2], method="compose")
    return united_clip


def add_music(video: VideoFileClip, music_path, start, video_len):
    audioclip = AudioFileClip(f'{music_path}/{get_random_file(music_path)}').subclip(start,start+video_len)
    video.audio = audioclip
    return video


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f1")
    parser.add_argument("-f2")
    parser.add_argument("-m")
    args = parser.parse_args()
    video = unite_and_cut(args.f1, args.f2 , 0, 2)  # files/videos1/ files/videos2/
    video = add_music(video, args.m, 0, 4)  # files/music/
    video.write_videofile("processed.mp4")

