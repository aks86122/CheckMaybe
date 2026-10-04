"""Clear footage with targeted masking: faces (YuNet, tracked), top/bottom UI bands (avatars, usernames, captions), extra brand boxes."""
import cv2, sys, json, glob, os
import numpy as np
def pix(img, x0, y0, x1, y1, k=28):
    h, w = img.shape[:2]; x0, y0, x1, y1 = max(0,int(x0)), max(0,int(y0)), min(w,int(x1)), min(h,int(y1))
    if x1 - x0 < 4 or y1 - y0 < 4: return
    r = img[y0:y1, x0:x1]
    s = cv2.resize(r, (max(1,(x1-x0)//k), max(1,(y1-y0)//k)), interpolation=cv2.INTER_LINEAR)
    img[y0:y1, x0:x1] = cv2.resize(s, (x1-x0, y1-y0), interpolation=cv2.INTER_NEAREST)
def run(frames_dir, extra, overlay, top=270):
    det = cv2.FaceDetectorYN.create("face.onnx", "", (1080, 1920), 0.6, 0.3, 50)
    ov = cv2.imread(overlay, cv2.IMREAD_UNCHANGED) if overlay else None
    last, miss = [], 0
    for f in sorted(glob.glob(f"{frames_dir}/*.png")):
        img = cv2.imread(f)
        det.setInputSize((img.shape[1], img.shape[0]))
        _, faces = det.detect(img)
        boxes = [] if faces is None else [tuple(map(float, fc[:4])) for fc in faces]
        if boxes: last, miss = boxes, 0
        elif miss < 12: boxes, miss = last, miss + 1
        for x, y, w, h in boxes:
            pix(img, x - .3*w, y - .2*h, x + 1.3*w, y + 1.25*h, 30)
        if top: pix(img, 0, 0, 1080, top, 22)        # top UI: avatars, usernames, other posts' captions
        pix(img, 0, 1740, 1080, 1920, 22)    # bottom UI: likes row, username caption
        for b in extra: pix(img, *b, 26)
        if ov is not None:
            a = ov[:, :, 3:4] / 255.0
            img = (img * (1 - a) + ov[:, :, :3] * a).astype(np.uint8)
        cv2.imwrite(f, img)
if __name__ == "__main__":
    run(sys.argv[1], json.loads(sys.argv[2]), sys.argv[3], int(sys.argv[4]))
