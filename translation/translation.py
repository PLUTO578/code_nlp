import logging
from nltk.translate.bleu_score import sentence_bleu
import jieba
import zhipuai

# 同学们申请的智谱API_KEY: https://open.bigmodel.cn
zhipuai.api_key = ""

# 配置日志记录
logging.basicConfig(level=logging.INFO)

# 读取文档的长度设置
length = 100

# 1. 读取文本
with open('news-commentary-v13.zh-en.en', 'r', encoding='utf-8') as e_file, \
        open('news-commentary-v13.zh-en.zh', 'r', encoding='utf-8') as c_file, \
        open('prompt', 'r', encoding='utf-8') as p_file:
    english_sentences = e_file.readlines()[:length]
    chinese_references = [sentence.split() for sentence in c_file.readlines()[:length]]
    prompt = p_file.read().strip()


# 2. 调用大模型API进行翻译
def translate_with_prompt(sentence, prompt):
    full_content = prompt.format(content=sentence)
    try:
        response = zhipuai.model_api.invoke(
            model="chatglm_pro",
            prompt=[{"role": "user", "content": full_content}],
            top_p=0.7,
            temperature=0.1,
        )
        logging.info(f"Invoked API with content: {full_content}")
        translation = response['data']['choices'][0]['content'].strip('" ')
        logging.info(translation+'\n\n')
        return list(jieba.cut(translation))
    except Exception as e:
        logging.error(f"调用API时发生错误: {e}")


translated_sentences = [translate_with_prompt(sentence, prompt) for sentence in english_sentences]

# 3. 使用BLEU计算质量并计算平均值
bleu_scores = []
for reference, candidate in zip(chinese_references, translated_sentences):
    reference = list(jieba.cut(reference[0]))
    bleu_score = sentence_bleu([reference], candidate, weights=(0, 1, 0, 0))
    bleu_scores.append(bleu_score)
    print(f"Reference: {' '.join(reference)}")
    print(f"Candidate: {' '.join(candidate)}")
    print(f"BLEU Score: {bleu_score:.4f}\n")

# 输出BLEU分数的平均值
print(f"平均BLEU得分: {sum(bleu_scores) / len(bleu_scores):.4f}")