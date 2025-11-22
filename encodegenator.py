import cv2
import face_recognition
import pickle
import os
import requests

# Supabase credentials (replace with your actual values)
SUPABASE_URL = "https://zoykcfdrjmdvjdgdglwr.supabase.co"
SUPABASE_SERVICE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpveWtjZmRyam1kdmpkZ2RnbHdyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM4MjIyMTUsImV4cCI6MjA3OTM5ODIxNX0.fnRnSpt_dvDPspORRtBJQMnr_dJcB4D9p-J1weqKupA"
  # Ensure this matches your bucket name

# Importing student images
folderPath = 'photos'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []

for path in pathList:
    img_path = os.path.join(folderPath, path)
    imgList.append(cv2.imread(img_path))
    studentIds.append(os.path.splitext(path)[0])

    

print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

with open("EncodeFile.p", 'wb') as file:
    pickle.dump(encodeListKnownWithIds, file)
print("File Saved")
