EchoStyle: Let Your Words Paint Your World is a real-time video enhancement project
This system proposes to use neural style transfer to transform video backgrounds into dynamic, evolving digital art during video conferencing, offering a personalized and 
engaging visual experience that goes beyond traditional static filters. 
The current implementation includes modules for real-time camera access using tkinter and OpenCV (cv2); accurate background removal using MOG2 background subtraction
which learns the static background for 5 seconds and then cleans the mask using thresholding and morphological operations ; 
and a Voice-to-Text Converter using pyaudio and speech_recognition to capture audio and convert it to text, which will eventually trigger the background style changes
Future work will focus on integrating NLP for text/keyword recognition and combining modules to blend styles dynamically, ensuring the background visually matches the conversation's context, emotion, and topics.
Technology Stack (Libraries Used) are:-
tkinter: For building the graphical user interface (GUI).
cv2 (OpenCV): For video capture, frame processing, background subtraction, and image transformations.
PIL (Pillow): For converting OpenCV frames for display in Tkinter and image resizing.
numpy: For numerical operations, mask creation, and image array handling.
time: For adding necessary delays, such as for background learning.
speech_recognition: For converting speech-to-text using the Google Speech Recognition API.
pyaudio: For real-time microphone access and audio recordin
Voice-to-Text Conversion
The system captures live audio from the microphone using the pyaudio library. 
The speech_recognition library, utilizing the Google Speech Recognition API, is used to convert the speaker's voice into real-time transcribed text. 
This transcribed text is the trigger that will eventually be used to select and change the video background style dynamically.
To isolate the user, the system first learns the static background over a short period (5 seconds). 
It then uses the MOG2 background subtraction method to detect the person. The resulting mask is refined using techniques like thresholding, morphological operations, and blurring to reduce noise and smooth edges. 
Currently, the removed background is replaced with a solid gray color. The cv2 (OpenCV) and numpy libraries are critical for these frame-by-frame video and image processing tasks.
