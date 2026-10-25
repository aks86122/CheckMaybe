# Export haywoodsloan/ai-image-detector-deploy (Apache-2.0) to ONNX, then int8 (about 199MB). Output files stay out of the repo.
import torch, os
from transformers import AutoModelForImageClassification
m=AutoModelForImageClassification.from_pretrained('haywoodsloan/ai-image-detector-deploy').eval()
class W(torch.nn.Module):
    def __init__(s,m): super().__init__(); s.m=m
    def forward(s,x): return s.m(pixel_values=x).logits.softmax(-1)
x=torch.randn(1,3,256,256)
torch.onnx.export(W(m),x,'det_fp32.onnx',input_names=['pixel_values'],output_names=['probs'],opset_version=17,dynamo=False)
from onnxruntime.quantization import quantize_dynamic, QuantType
quantize_dynamic('det_fp32.onnx','det_int8.onnx',weight_type=QuantType.QUInt8)
