项目 README 文件介绍：

本项目是自然语言处理课程作业项目，旨在通过修改提示词文件来提升模型性能。项目包含三个子任务：情绪分析（emotion）、分词（tokenization）、和翻译（translation）。每个子任务都有一个主运行脚本、提示词文件和环境需求文件。学生需要关注于调整prompt文件中的提示语，以提升模型的输出性能。以下是项目的详细介绍和使用说明：

### 文件结构
```
├── emotion
│   ├── emotion.py (主运行脚本)
│   ├── prompt (提示词文件)
│   └── requirement.txt (环境依赖文件)
├── tokenization
│   ├── tokenization.py (主运行脚本)
│   ├── prompt (提示词文件)
│   ├── pku_training.utf8 (数据集)
│   └── requirement.txt (环境依赖文件)
└── translation
    ├── translation.py (主运行脚本)
    ├── prompt (提示词文件)
    ├── news-commentary-v13.zh-en.en (翻译数据集)
    ├── news-commentary-v13.zh-en.zh (翻译数据集)
    └── requirement.txt (环境依赖文件)
```

### 环境配置
1. 将Python包源设置为清华源，以加速包的安装速度：
   ```
   pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
   ```
2. 根据各子任务的`requirement.txt`文件安装所需的Python包。例如，安装scikit-learn：
   ```
   pip install -r requirement.txt
   ```

### 任务执行步骤
当然，这里是各个任务的执行步骤，每个任务都包括了配置API_KEY的步骤：

### 1. 情绪分析任务（Emotion Task）

#### 步骤：

1. 访问 https://open.bigmodel.cn 以申请API_KEY。
2. 在`emotion.py`脚本中按照说明填写已获得的API_KEY。
3. 使用以下命令来运行情绪分析任务的脚本：
   ```
   python emotion.py
   ```
4. 适当修改`prompt`文件中的提示词，尝试提高模型的准确度。
5. （可选）更改`emotion.py`脚本中的模型参数或尝试使用不同类型的模型来实验提升性能。

#### 结果输出示例
![image](https://github.com/uglyghost/code_nlp/assets/15159177/48a32dd7-5645-4d45-ad62-b340dfc1c1d0)


### 2. 分词任务（Tokenization Task）

#### 步骤：

1. 访问 https://open.bigmodel.cn 以申请API_KEY。
2. 在`tokenization.py`脚本中按照说明填写已获得的API_KEY。
3. 使用以下命令来运行分词任务的脚本：
   ```
   python tokenization.py
   ```
4. 尝试修改`prompt`文件中的提示词，以提升模型的性能。
5. （可选）您可以更改`tokenization.py`脚本中的模型参数或尝试使用不同类型的模型进行实验。

#### 结果输出示例
![image](https://github.com/uglyghost/code_nlp/assets/15159177/1dc434e1-9056-4422-b7ff-632740017632)


### 3. 翻译任务（Translation Task）

#### 步骤：

1. 访问 https://open.bigmodel.cn 以申请API_KEY。
2. 在`translation.py`脚本中按照说明填写已获得的API_KEY。
3. 使用以下命令来运行翻译任务的脚本：
   ```
   python translation.py
   ```
4. 适当调整`prompt`文件中的提示词，尝试提升模型的性能。
5. （可选）您可以尝试更改`translation.py`脚本中的模型参数或使用不同类型的模型进行实验，以寻找最佳性能配置。

#### 结果输出示例
![image](https://github.com/uglyghost/code_nlp/assets/15159177/2f03f9aa-3589-426f-b675-c45cb7a66587)


### 作业目标
- 运行主脚本后，系统将输出模型的性能结果。同学们应尽可能调整提示词（prompt），或调整模型参数及更换模型来提高性能。

希望这份指南能够为同学们提供清晰和详细的步骤指导，祝您完成课程作业顺利！
