# Machine-Leaning-Gaze-Estimation
Utilizing UnityEyes, GAN, and TensorFlow to build a diverse training set for gaze estimation.

# Startup to visualize generated eyes:
1) Download UnityEyes_Linux from the UnityEyes website, extract.
2) chmod 7-- unityeyes.x86 (make it executable)
3) Run unityeyes.x86 with './unityeyes.x86'. Press 'r' to randomly change the eye environment, 
   's' to save an img. Generate several eye jpgs (json data will be created with them as well).
   Can also click start for random generation, will continue generating until you exit the exe.
4) Move visualize.py into the 'imgs' folder, execute it. Annotated versions of the eye jpgs will be created in the imgs folder.