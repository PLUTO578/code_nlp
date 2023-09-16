import pandas as pd
import logging
import zhipuai

# your api key
zhipuai.api_key = "90779b30f8299535d7fe10b7e665751e.CRcENI5utT45TMsC"

# 日志配置
logging.basicConfig(level=logging.INFO)


# 定义调用模型API的函数
def invoke_model_api(unsegmented_text, prompt_text):
    try:
        full_content = prompt_text.format(content=unsegmented_text)
        response = zhipuai.model_api.invoke(
            model="chatglm_lite",
            prompt=[{"role": "user", "content": full_content}],
            top_p=0.7,
            temperature=0.1,
        )
        logging.info(f"Invoked API with content: {full_content}")
        valid_content = response['data']['choices'][0]['content'].strip('" ')
        return valid_content
    except Exception as e:
        logging.error(f"调用API时发生错误: {e}")


# 读取CSV文件
df = pd.read_csv('weibo_senti_100k.csv', encoding='utf-8')

# 读取提示文本
with open('prompt', 'r', encoding='utf-8') as file:
    prompt_text = file.read().strip()

length = 10

# 随机选择100行进行测试
df_sample = df.sample(n=length, random_state=1)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 初始化变量
true_labels = []
predicted_labels = []

# 遍历选中的100行
for index, row in df_sample.iterrows():
    label = row['label']
    review = row['review']

    # 调用模型API
    response_label = invoke_model_api(review, prompt_text)
    logging.info(f"Predicted label: {response_label}")

    # 将模型的响应与实际标签进行比较
    if response_label is not None:
        predicted_label = 1 if '正向' in response_label else 0
        predicted_labels.append(predicted_label)
        true_labels.append(label)

        if (predicted_label == 1 and label == 1) or (predicted_label == 0 and label == 0):
            logging.info(f"Index {index}: Predicted correctly")
        else:
            logging.info(f"Index {index}: Predicted incorrectly")

# 计算指标
acc = accuracy_score(true_labels, predicted_labels)
pre = precision_score(true_labels, predicted_labels)
recall = recall_score(true_labels, predicted_labels)
f1 = f1_score(true_labels, predicted_labels)

# 输出结果
logging.info(f"Accuracy: {acc}")
logging.info(f"Precision: {pre}")
logging.info(f"Recall: {recall}")
logging.info(f"F1 Score: {f1}")

