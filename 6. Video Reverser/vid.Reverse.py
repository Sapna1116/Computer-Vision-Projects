import cv2

print("Do you want to reverse a new video?: (y/Y)")
if input().lower()=='y':
    cap = cv2.VideoCapture(0) 
    
    h = int((cap.get(cv2.CAP_PROP_FRAME_HEIGHT))*0.5)
    w = int((cap.get(cv2.CAP_PROP_FRAME_WIDTH))*0.5)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    inPath = 'AI\\11.vidReverse\\InputVid2.mp4'
    inVid = cv2.VideoWriter(inPath, fourcc, fps, (w,h))

    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (w,h))
        if not ret:
            break
        cv2.imshow("Video", frame)
        inVid.write(frame)
        if cv2.waitKey(1)==27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

else:
    inPath = r'AI\11.vidReverse\InputVid.mp4'


cap = cv2.VideoCapture(inPath)

h = int((cap.get(cv2.CAP_PROP_FRAME_HEIGHT))*0.5)
w = int((cap.get(cv2.CAP_PROP_FRAME_WIDTH))*0.5)
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

noOfFramesInVid = cap.get(cv2.CAP_PROP_FRAME_COUNT)
idxOfLastFrame = noOfFramesInVid-1

outPath = 'AI\\11.vidReverse\\OutputVideo2.mp4'
out = cv2.VideoWriter(outPath, fourcc, fps, (w,h))

if(cap.isOpened()):
    print("Entered")
    while(idxOfLastFrame != 0):
        # To set current frame's position to last fram index
        cap.set(cv2.CAP_PROP_POS_FRAMES, idxOfLastFrame)

        ret, frame = cap.read()
        frame = cv2.resize(frame, (w,h))
        if(ret):
            out.write(frame)
            idxOfLastFrame -= 1
            #Printing the progress
            if(idxOfLastFrame%100==0):
                print(idxOfLastFrame)
    print("processing done")
    out.release()
    
cap.release()
cv2.destroyAllWindows()