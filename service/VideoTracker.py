'''
Multi-Object Tracker:

This program was created for the purpose of tracking multiple objects on video.
To achieve the task, the OpenCV library was used.
'''

#Import libraries
import argparse
import cv2
import sys
import json

def MultiTracker(video_path, json_path, output_path, model, frames):
    
    #Load Video
    video = cv2.VideoCapture(video_path)
    
    success, frame = video.read()
    
    #Load initial Bboxes from json
    with open(json_path, 'r') as j:
        contents = json.load(j)
        
    bboxes = []
    for i in range(len(contents)):
        bboxes.append(contents[i]['coordinates'])
        
    multiTracker = cv2.legacy.MultiTracker_create()
    
    #Initialize the trackers using Initial Bboxes and first frame
    for bbox in bboxes:
        multiTracker.add(model.create(), frame, bbox)
    
    #Set the parameters of the output video
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = video.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(output_path, fourcc, fps, (int(width),int(height)))
    
    #Frame length and frame counter
    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    num = int(video.get(cv2.CAP_PROP_POS_FRAMES))

    #Loop over frames
    while num < length:
        success, frame = video.read()
        num = int(video.get(cv2.CAP_PROP_POS_FRAMES))
        success, boxes = multiTracker.update(frame)
        
        if frames:
            if num%30==0:
                print('the tracker has processed {} frames'.format(num))

        # draw tracked objects
        for i, newbox in enumerate(boxes):
            p1 = (int(newbox[0]), int(newbox[1]))
            p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
            cv2.rectangle(frame, p1, p2, (0,0,255), 2, 1)
            
        #Write frame to output
        out.write(frame)
        
    out.release()
    video.release()
    cv2.destroyAllWindows()
    
    print('the tracked video was successfully generated in: {}'.format(output_path))
    
    return
    
    
#parser    
if __name__ == "__main__":
    epilog = """\
    USAGE:
    python VideoTracker.py --output=./output.avi\
    --pathjson=./development_assets/initial_conditions.json\
    --pathvideo=./development_assets/input.mkv\n
    """
    parser = argparse.ArgumentParser(
        description="Video Tracker",
        add_help=True,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=epilog)
    parser.add_argument(
        '--pathvideo',
        help="Path to video",
        type=str,
        default="../development_assets/input.mkv")
    parser.add_argument(
            '--output',
            help="Path to save tracked video",
            type=str,
            default='../output.avi')
    parser.add_argument(
            '--pathjson',
            help="Path to initial condition json",
            type=str,
            default='../development_assets/initial_conditions.json')
    parser.add_argument(
            '--trackmodel',
            help="Model for tracking",
            type=str,
            default='csrt',
            choices=['csrt', 'kcf', 'boosting',
                'mil', 'tld', 'medianflow','mosse'])
    parser.add_argument(
            '--processframe',
            help="processed frames",
            action='store_true')
    args = parser.parse_args()
    
    #Dict of available tracking models
    TrDict = {'csrt': cv2.legacy.TrackerCSRT,
     'kcf' : cv2.legacy.TrackerKCF,
     'boosting' : cv2.legacy.TrackerBoosting,
     'mil': cv2.legacy.TrackerMIL,
     'tld': cv2.legacy.TrackerTLD,
     'medianflow': cv2.legacy.TrackerMedianFlow,
     'mosse':cv2.legacy.TrackerMOSSE}
    
    tracker = TrDict[args.trackmodel]
    
    print('the model to use is {}'.format(args.trackmodel))
    
    MultiTracker(args.pathvideo, args.pathjson, args.output, tracker, args.processframe)
    

        
    

    
    
