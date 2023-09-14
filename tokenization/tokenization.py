import logging
import time

from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import precision_score, recall_score, f1_score
import zhipuai

# your api key
zhipuai.api_key = "90779b30f8299535d7fe10b7e665751e.CRcENI5utT45TMsC"

# 配置日志记录
logging.basicConfig(level=logging.INFO)

# 读取prompt文件中的内容
try:
    with open('prompt', 'r', encoding='utf-8') as f:
        prompt_text = f.read()
    logging.info("成功读取prompt文件")
except Exception as e:
    logging.error(f"读取prompt文件时发生错误: {e}")

# 读取主文件的内容
try:
    with open('pku_training.utf8', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    logging.info("成功读取主文件")
except Exception as e:
    logging.error(f"读取主文件时发生错误: {e}")

# 初始化一个空列表来存储处理后的items
result_list = []

# 初始化列表来存储真实标签和预测标签
true_labels = []
predicted_labels = []

length = 100
# total_lines = len(lines)
total_lines = length


for index, line in enumerate(lines[:length]):
    # 移除行尾的换行符
    line = line.strip()

    # 使用空格来分割分词的文本
    segmented_words = line.split(' ')

    # 将分词的文本重新组合为未分词的文本
    unsegmented_text = ''.join(segmented_words)

    # 准备输入到语言模型的内容
    full_content = unsegmented_text + prompt_text

    # 调用语言模型API
    try:
        response = zhipuai.model_api.invoke(
            model="chatglm_lite",
            prompt=[{"role": "user", "content": full_content}],
            top_p=0.7,
            temperature=0.1,
        )
        logging.info(f"Invoked API with content: {full_content}")
        valid_content = response['data']['choices'][0]['content'].strip('" ')
    except Exception as e:
        logging.error(f"调用API时发生错误: {e}")
        continue

    # 获取模型的分词结果
    model_segmented_words = valid_content.split('/')

    # 添加真实标签和预测标签到列表中
    true_labels.append(segmented_words)
    predicted_labels.append(model_segmented_words)

    # 将新的文本添加到结果列表中
    logging.info(f"大模型分词结果: {model_segmented_words}")

    time.sleep(5)

    # 显示处理进度
    if index % 10 == 0:  # 每处理100行，显示一次进度
        logging.info(f"处理进度: {index}/{total_lines}")

# 初始化MultiLabelBinarizer
mlb = MultiLabelBinarizer()

# 使用MultiLabelBinarizer转换真实标签和预测标签
true_labels_binarized = mlb.fit_transform(true_labels)
predicted_labels_binarized = mlb.transform(predicted_labels)

# 计算评估指标
precision = precision_score(true_labels_binarized, predicted_labels_binarized, average='micro')
recall = recall_score(true_labels_binarized, predicted_labels_binarized, average='micro')
f1 = f1_score(true_labels_binarized, predicted_labels_binarized, average='micro')

logging.info(f"Precision: {precision}")
logging.info(f"Recall: {recall}")
logging.info(f"F1 Score: {f1}")
