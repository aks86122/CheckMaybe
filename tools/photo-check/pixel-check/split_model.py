# Split the int8 ONNX model into parts under Cloudflare Pages' 25 MiB file limit and write manifest.json.
# Usage: python split_model.py det_int8.onnx out_dir/
import hashlib, json, os, sys
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
CHUNK = 24 * 1024 * 1024
data = open(src, "rb").read()
parts = []
for i in range(0, len(data), CHUNK):
    b = data[i:i + CHUNK]; name = "det-int8.part%02d" % (i // CHUNK)
    open(os.path.join(out, name), "wb").write(b)
    parts.append({"name": name, "size": len(b), "sha256": hashlib.sha256(b).hexdigest()})
m = {"model": "haywoodsloan/ai-image-detector-deploy (Apache-2.0), ONNX int8", "version": 1, "total": len(data),
     "sha256": hashlib.sha256(data).hexdigest(), "input": [1, 3, 256, 256], "parts": parts}
json.dump(m, open(os.path.join(out, "manifest.json"), "w"), indent=1)
print(len(parts), "parts,", len(data), "bytes")
