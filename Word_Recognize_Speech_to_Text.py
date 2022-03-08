# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:22:36 2021

@author: H.Egemen Gulpinar 
@Title : Real Time Video Transcript
"""

import numpy as np
import speech_recognition as sr
import os 
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
offset_value = -8
import speech_recognition as sr
from pydub import AudioSegment

recognizer = sr.Recognizer()
count_wav = 0
multiply_t1 = 10
multiply_t2 = 10000
t1 = 1000
t2 = 15000
# recognized_wav = np.array([])
# result_array = np.array([])
# temp_result_array = np.array([])
# long_generate_select = np.array([])
# lenght_values = np.array([])
max_size = 0
max_index = 0
flag = False
count_files = 0
first_loop_flag = True
import time
while(True):
    count_files += 1
    count_wav = 0
    flag = False
    first_loop_flag = True
    t1 = 1000
    t2 = 15000
    recognized_wav = np.array([])
    result_array = np.array([])
    temp_result_array = np.array([])
    long_generate_select = np.array([])
    lenght_values = np.array([])
    while(first_loop_flag):
        count_wav = count_wav + 1
        
        
          #Works in milliseconds
         
        # newAudio = AudioSegment.from_wav("deneme2.wav") 
        print("birinci kısım count files --> ",count_files)
        
        newAudio = AudioSegment.from_wav(str("trial" + str(count_files) + '.wav'))
        newAudio = newAudio[t1:t2]
        audio_name = str("file" + str(count_files) + str(count_wav) + ".wav")
        newAudio.export(audio_name, format="wav")
        audio_file_ = sr.AudioFile(audio_name)
        offset_value = offset_value + 10
        print("ikinci kısım")
        for j in range(0,5):
            print(offset_value)
            with audio_file_ as source:
                try:
                  # offset_value = np.arange(0,100,10)[i]
                  if audio_file_.DURATION < 5:
                        flag = True
                        break
                  audio_file = recognizer.record(source,duration = 15)    
                  
                  result =  recognizer.recognize_wit(audio_data = audio_file, key = "IVLQNRDRDXFHMLO2SXZYSONF3VMFBN5G")
                  
                  print(result)
                  time.sleep(1)
                  # print(type(result))
                  long_generate_select = np.append(long_generate_select,result)
                  
                  
                  
                  
                  def loop_again(recognized_wav,temp_result_array):

                      for i in range(0,len(recognized_wav)):
                          audio_file_ = sr.AudioFile(recognized_wav[i])
                          with audio_file_ as source2:
                              try:
                                    print("-------loop again -------")
                                    # time.sleep(60)
                                    audio_file2 = recognizer.record(source2,duration = 2)       
                                    result_temp = recognizer.recognize_wit(audio_data = audio_file2, key = "IVLQNRDRDXFHMLO2SXZYSONF3VMFBN5G")
                                    print(result_temp)
                                    temp_result_array = np.append(temp_result_array,result_temp)
                                    
                            
                        # print(result2)
                              except Exception as e:
                                  print(e)
                                  print("Error ?")
                                  pass
                                  # loop_again()
                      return temp_result_array
                      
                
                except sr.UnknownValueError:
                    
                    
                    if audio_file_.DURATION < 5:
                        flag = True
                        break
                    recognized_wav = np.append(recognized_wav,audio_name)
                    print("HATA VAR || ERROR! Recorded Sound with an Exception -> ", audio_name)
                    
                    
                    # return_temp_result = loop_again(recognized_wav,temp_result_array)
                    
                    
               
                except  IndexError as o:
          
                    print("The .wav file does not include any voice")
                except sr.RequestError as e:
                    print("Could not request results from GSR service; {0}".format(e))
           
        try:     
            for i in range(0,len(long_generate_select)):
                lenght_values = np.append(lenght_values, len(long_generate_select[i]))
                if lenght_values[i] > max_size:
                    max_size = lenght_values[i]
                    max_index = i
                
            if flag == False:              ## While program getting end 
                lenght_values = np.array([])
                max_size = 0
                result_array = np.append(result_array,long_generate_select[max_index])
                print("result array --> ",result_array)
                print("----------")
                print("long generate_select ----->>>" , long_generate_select[max_index])
                long_generate_select = np.array([])
                
        except IndexError as u:
            print("The .wav file does not include any voice")
        except sr.IndexError as az:
            print("The .wav file does not include any voice")
           
                
        t1 = t2  - 2500
        t2 = t2 + 15000
        print("t1 value --> " , t1)
        print("t2 value --> " , t2)
        if flag == True:
            break
            
        
            
    file_name =  os.getcwd() + "\\"  + "trial" + str(count_files) + '.txt'
    txt_file = open(file_name, "w+")
    full_sentence = str(result_array[:])
    txt_file.writelines(full_sentence)
    txt_file = open(file_name,"w+")
    if count_files == 10:
            break
    # if  len(recognized_wav) > 0:
    #     time.sleep(60)
    #     return_temp_result = str(loop_again(recognized_wav,temp_result_array))
    #     print("New generated return result",return_temp_result)
    #     while len(return_temp_result) < 1:
    #         print("Error for less character size, it should be generate again " )
    #         # time.sleep(60)
    #         return_temp_result_final = str(loop_again(recognized_wav,temp_result_array))
    #         print("Fixed return result",return_temp_result_final)
        