
# path = "F:/PaintTransformer-main/video/morax.mp4"

import cv2
import os
 
def video2frames(videofile, savepath):
    vcap = cv2.VideoCapture() # 生成读取视频对象
    vcap.open(videofile)
 
    n = 1
    frame_interval = 12 # 每隔frame_interval帧保存图像
    total_frames = int(vcap.get(cv2.CAP_PROP_FRAME_COUNT)) # 读取视频总帧率
    print(f'total frames: {total_frames}') # 267
 
    for i in range(total_frames):
        ret, frame = vcap.read() #  按帧读取视频
 
        if i % frame_interval == 0:
            filename = str(n) + '.jpg'
            print(filename)
 
            # 保存当前帧图像，以下两个方式都可以
            cv2.imencode('.jpg', frame)[1].tofile(os.path.join(savepath, filename))
            # cv2.imwrite(os.path.join(savepath, filename), frame)
            n += 1
 
    vcap.release()
 
 
if __name__ == '__main__':
    savepath = 'F:/PaintTransformer-main/convert/video2img/output'
    videofile = 'F:/PaintTransformer-main/convert/video2img/input/morax.mp4'
    video2frames(videofile, savepath)