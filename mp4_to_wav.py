import glob
import os
import moviepy.editor as mp
extension_list = ('*.mp4', '*.flv')
os.chdir(r'C:\Users\egeme\Desktop\deneme')

count = 0

for extension in extension_list:
    
    for video in glob.glob(extension):
        count  += 1 
        clip = mp.VideoFileClip(video)
        # name_clip = os.path.splitext(os.path.basename(video))[0] + '.wav'
        name_clip = "trial" + str(count) + '.wav'
        clip.audio.write_audiofile(name_clip)
        
        
