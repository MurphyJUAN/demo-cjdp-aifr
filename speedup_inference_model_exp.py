# %%
import torch
from transformers import BertModel, BertTokenizer
from model.MyJointBert import MyJointBert,  MyJointRoberta
import onnxruntime
import numpy as np
from opencc import OpenCC
cc = OpenCC('t2s')
import time
# %%
if torch.cuda.is_available():
        device = torch.device('cuda')
PRETRAINED_MODEL_NAME = "bert-base-chinese" 
NUM_LABELS = 3
EMB_MODEL_NAME = ""
batch_size = 4
MAX_LENGTH = 512
tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
# %%
def load_bert_model(model_path, PRETRAINED_MODEL_NAME, NUM_LABELS, EMB_MODEL_NAME):
    model = MyJointBert.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS, emb_name=EMB_MODEL_NAME)
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    return model
def load_roberta_model(model_path, PRETRAINED_MODEL_NAME, NUM_LABELS):
    model = MyJointRoberta(PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS)
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    return model
# %%
our_switch_model_path = './ckpt/new/our_switch_0.pt'
our_switch_model = load_bert_model(our_switch_model_path, PRETRAINED_MODEL_NAME, NUM_LABELS, EMB_MODEL_NAME)
our_switch_model.to(device)
our_switch_model.eval()
#%%
# our_switch_model = load_roberta_model('./ckpt/new/lawformer_switch_0.pt', "thunlp/Lawformer", NUM_LABELS)
# our_switch_model.to(device)
# our_switch_model.eval()
# %%
class MyModelWrapper(torch.nn.Module):
    def __init__(self, original_model):
        super(MyModelWrapper, self).__init__()
        self.original_model = original_model
    
    def forward(self, AA_input_ids, AA_token_type_ids, AA_attention_mask, 
                AD_input_ids, AD_token_type_ids, AD_attention_mask, 
                RA_input_ids, RA_token_type_ids, RA_attention_mask, 
                RD_input_ids, RD_token_type_ids, RD_attention_mask):
        # 组装AA, AD, RA, RD字典
        AA = {'input_ids': AA_input_ids, 'token_type_ids': AA_token_type_ids, 'attention_mask': AA_attention_mask}
        AD = {'input_ids': AD_input_ids, 'token_type_ids': AD_token_type_ids, 'attention_mask': AD_attention_mask}
        RA = {'input_ids': RA_input_ids, 'token_type_ids': RA_token_type_ids, 'attention_mask': RA_attention_mask}
        RD = {'input_ids': RD_input_ids, 'token_type_ids': RD_token_type_ids, 'attention_mask': RD_attention_mask}
        
        # 调用原始模型的forward方法
        return self.original_model(AA=AA, AD=AD, RA=RA, RD=RD)
model = MyModelWrapper(our_switch_model)
model.to(device)
# %%
text_1 = [cc.convert("當事人具有父母經濟等有利條件"), cc.convert(""), cc.convert(""), cc.convert("當事人具有親子感情等不利條件")]
text_2 = [cc.convert("當事人非常愛護小孩，並且和小孩的關係良好充滿信任"), cc.convert(""), cc.convert(""), cc.convert("當事人曾經在酗酒後毆打小孩，導致小孩非常害怕和當事人相處。")]  # 假設有四個相同的文本輸入
encoded_inputs = [tokenizer(text_1[i], text_2[i],  padding=True, max_length=MAX_LENGTH, truncation="longest_first",  return_tensors="pt") for i in range(4)]

# encoded_inputs = [tokenizer(text_1[i], text_2[i], padding="max_length", max_length=MAX_LENGTH, truncation="longest_first", return_tensors="pt") for i in range(4)]
input_dicts = [{key: val.to(device) for key, val in ei.items()} for ei in encoded_inputs]
# kwargs_for_onnx_export = {
#     'AA': input_dicts[0],
#     'AD': input_dicts[1],
#     'RA': input_dicts[2],
#     'RD': input_dicts[3],
#     # 'labels': 可选，如果你需要传递labels
# }

kwargs_for_onnx_export = {
    "AA_input_ids": input_dicts[0]['input_ids'], 
    "AA_token_type_ids": input_dicts[0]['token_type_ids'], 
    "AA_attention_mask": input_dicts[0]['attention_mask'], 
    "AD_input_ids": input_dicts[1]['input_ids'],
    "AD_token_type_ids": input_dicts[1]['token_type_ids'], 
    "AD_attention_mask": input_dicts[1]['attention_mask'], 
    "RA_input_ids": input_dicts[2]['input_ids'], 
    "RA_token_type_ids": input_dicts[2]['token_type_ids'], 
    "RA_attention_mask": input_dicts[2]['attention_mask'], 
    "RD_input_ids": input_dicts[3]['input_ids'], 
    "RD_token_type_ids": input_dicts[3]['token_type_ids'], 
    "RD_attention_mask": input_dicts[3]['attention_mask']
}
# %%
start_time = time.time()
torch.onnx.export(model,
                  args=(kwargs_for_onnx_export,),  # 注意这里是一个元组，里面只有一个元素，即关键字参数字典
                do_constant_folding=True,
                  f="./speedup_ckpt/our_switch_0.onnx",
                  input_names=['AA_input_ids', 'AA_token_type_ids', 'AA_attention_mask', 'AD_input_ids', 'AD_token_type_ids', 'AD_attention_mask', 'RA_input_ids', 'RA_token_type_ids', 'RA_attention_mask','RD_input_ids',  'RD_token_type_ids', 'RD_attention_mask'],
                  output_names=['logits'],
                  dynamic_axes={'AA_input_ids': [0,1], 'AA_token_type_ids': [0,1], 'AA_attention_mask': [0,1], 'AD_input_ids': [0,1], 'AD_token_type_ids': [0,1], 'AD_attention_mask': [0,1], 'RA_input_ids': [0,1], 'RA_token_type_ids': [0,1], 'RA_attention_mask': [0,1], 'RD_input_ids': [0,1], 'RD_token_type_ids': [0,1], 'RD_attention_mask': [0,1], 'logits': {0: 'batch_size'}, 'sentence_emb': {0: 'batch_size'}}
                 )
elapsed_time = time.time() - start_time
# 25mins
print('轉換所需要的時間：', elapsed_time)

# %%
if 'CUDAExecutionProvider' in onnxruntime.get_available_providers():
    print("CUDA is available. Using GPU.")
    sess_options = onnxruntime.SessionOptions()
    sess = onnxruntime.InferenceSession("./speedup_ckpt/our_switch_0.onnx", sess_options, providers=['CUDAExecutionProvider'])
else:
    print("CUDA is not available. Using CPU.")
    sess = onnxruntime.InferenceSession("./onnx_ckpt/our_switch_0.onnx")

# %%
# 準備輸入數據
# text_1 = [cc.convert("當事人具有父母經濟等有利條件"), cc.convert(""), cc.convert(""), cc.convert("當事人具有親子感情等不利條件")]
# text_2 = [cc.convert("當事人非常愛護小孩，並且和小孩的關係良好充滿信任"), cc.convert(""), cc.convert(""), cc.convert("當事人曾經在酗酒後毆打小孩，導致小孩非常害怕和當事人相處。")]  # 假設有四個相同的文本輸入



text_1 = [cc.convert(""), cc.convert("當事人具有支持系統、親子感情等不利條件"), cc.convert("當事人具有親子感情等有利條件"), cc.convert("")]
text_2 = [cc.convert(""), cc.convert("當事人曾經在酗酒後毆打小孩，導致小孩非常害怕和當事人相處，並且目前其所有家人都居住在國外，在台灣沒有親友可以幫忙照顧小孩。"), cc.convert("當事人和小孩已經建立非常深厚的信任關係，相處融洽，也能負擔教養責任。"), cc.convert("")]  # 假設有四個相同的文本輸入
#%%
# encoded_inputs = [tokenizer(text_1[i], text_2[i], padding="max_length", max_length=MAX_LENGTH, truncation="longest_first", return_tensors="pt") for i in range(4)]

encoded_inputs = [tokenizer(text_1[i], text_2[i],  padding=True, max_length=MAX_LENGTH, truncation="longest_first",  return_tensors="pt") for i in range(4)]
# %%
# encoded_inputs = [tokenizer(text_2[i], return_tensors="pt") for i in range(4)]
input_dicts = [{key: val for key, val in ei.items()} for ei in encoded_inputs]
# %%
# 執行推理
model_inputs = {
    'AA_input_ids': input_dicts[0]['input_ids'].numpy(),
    'AA_token_type_ids': input_dicts[0]['token_type_ids'].numpy(),
    'AA_attention_mask': input_dicts[0]['attention_mask'].numpy(),
    'AD_input_ids': input_dicts[1]['input_ids'].numpy(),
    'AD_token_type_ids': input_dicts[1]['token_type_ids'].numpy(),
    'AD_attention_mask': input_dicts[1]['attention_mask'].numpy(),
    'RA_input_ids': input_dicts[2]['input_ids'].numpy(),
    'RA_token_type_ids': input_dicts[2]['token_type_ids'].numpy(),
    'RA_attention_mask': input_dicts[2]['attention_mask'].numpy(),
    'RD_input_ids': input_dicts[3]['input_ids'].numpy(),
    'RD_token_type_ids': input_dicts[3]['token_type_ids'].numpy(),
    'RD_attention_mask': input_dicts[3]['attention_mask'].numpy(),
}
# %%
# 执行模型推理
repetitions = 100
start_time = time.time()
for _ in range(repetitions):
    outputs = sess.run(None, model_inputs)
elapsed_time = time.time() - start_time
print('>>>>轉換後的模型所需要的時間')
print(outputs)
print(elapsed_time)

# %%
input_dicts = [{key: val.to(device) for key, val in ei.items()} for ei in encoded_inputs]
our_switch_model.eval()
start_time = time.time()
with torch.no_grad():   
    for _ in range(repetitions):
        real_outputs = our_switch_model(AA=input_dicts[0], AD=input_dicts[1], RA=input_dicts[2], RD=input_dicts[3])
elapsed_time = time.time() - start_time
print('>>>>原本的模型所需要的時間：')
print(real_outputs)
print(elapsed_time)
# %%
# Try TensorRT
import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np

def build_engine(onnx_file_path):
    TRT_LOGGER = trt.Logger(trt.Logger.WARNING)
    builder = trt.Builder(TRT_LOGGER)
    network = builder.create_network(1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH))
    config = builder.create_builder_config()
    config.set_memory_pool_limit(trt.MemoryPoolType.WORKSPACE, 8 << 30)  # 1GB

    parser = trt.OnnxParser(network, TRT_LOGGER)
    with open(onnx_file_path, 'rb') as model:
        if not parser.parse(model.read()):
            print('ERROR: Failed to parse the ONNX file.')
            for error in range(parser.num_errors):
                print(parser.get_error(error))
            return None
    
    # 添加优化配置文件
    profile = builder.create_optimization_profile()

    # 为动态输入定义最小、最优和最大尺寸
    # 假设最小批次为1，最小序列长度为10；最优批次和序列长度为4和128；最大批次和序列长度为8和256
    min_shape = (1, 10)
    optimal_shape = (4, 128)
    max_shape = (32, 512)

    # 对于你的每个输入，你需要添加相应的配置
    inputs = ['AA_input_ids', 'AA_token_type_ids', 'AA_attention_mask', 'AD_input_ids', 'AD_token_type_ids', 
              'AD_attention_mask', 'RA_input_ids', 'RA_token_type_ids', 'RA_attention_mask', 
              'RD_input_ids', 'RD_token_type_ids', 'RD_attention_mask']
    for input_name in inputs:
        profile.set_shape(input_name, min_shape, optimal_shape, max_shape)

    config.add_optimization_profile(profile)
    
    # 使用新的序列化构建方法
    engine = builder.build_engine(network, config)
    if engine is None:
        print("Failed to create TensorRT engine")
        return None
    return engine

def allocate_buffers(engine):
    inputs = []
    outputs = []
    bindings = []
    stream = cuda.Stream()
    for binding in engine:
        size = trt.volume(engine.get_binding_shape(binding)) * engine.max_batch_size
        dtype = trt.nptype(engine.get_binding_dtype(binding))
        print(f"Allocating buffer for binding {binding}, Size: {size}, Dtype: {dtype}")

        try:
            host_mem = cuda.pagelocked_empty(size, dtype)
            device_mem = cuda.mem_alloc(host_mem.nbytes)
            bindings.append(int(device_mem))
            if engine.binding_is_input(binding):
                inputs.append({'host': host_mem, 'device': device_mem})
            else:
                outputs.append({'host': host_mem, 'device': device_mem})
        except cuda.MemoryError as e:
            print(f"Failed to allocate memory for binding {binding}: {e}")
            raise

    return inputs, outputs, bindings, stream

def do_inference(context, bindings, inputs, outputs, stream, batch_size=1):
    """执行推理，并返回输出数据"""
    [cuda.memcpy_htod_async(inp['device'], inp['host'], stream) for inp in inputs]
    context.execute_async(batch_size=batch_size, bindings=bindings, stream_handle=stream.handle)
    [cuda.memcpy_dtoh_async(out['host'], out['device'], stream) for out in outputs]
    stream.synchronize()
    return [out['host'] for out in outputs]
# %%
# 构建引擎
engine = build_engine('./speedup_ckpt/our_switch_0.onnx')
# %%
# 分配缓冲区
inputs, outputs, bindings, stream = allocate_buffers(engine)

# 准备输入数据
for input, data in zip(inputs, list(model_inputs.values())):
    np.copyto(input['host'], data.ravel())

# 创建推理上下文并执行推理
with engine.create_execution_context() as context:
    results = do_inference(context, bindings=bindings, inputs=inputs, outputs=outputs, stream=stream, batch_size=1)

print('TensorRT推理结果:', results)
# %%
