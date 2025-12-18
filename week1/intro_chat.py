import os
from dotenv import load_dotenv
from ollama import chat

# 1. 环境加载
# 虽然本地使用 Ollama 通常不需要 API Key，但使用 load_dotenv 是为了兼容多环境配置
load_dotenv()

def first_chat_demo():
    print("--- 正在启动你的第一次 Python LLM 对话 ---")
    
    # 2. 调用模型
    # 我们需要传递的关键内容：
    # - model: 你要使用的模型名称
    # - messages: 对话历史，由角色(role)和内容(content)组成的列表
    # - options: 额外的参数（如温度 temperature）
    response = chat(
        model="ministral-3:3b",
        messages=[
            {
                "role": "system", 
                "content": "你是一个友好的助教。请简洁地回答学生的问题。"
            },
            {
                "role": "user", 
                "content": "你好！请用一句话告诉我什么是提示词工程？"
            },
        ],
        options={
            "temperature": 0.7  # 控制输出的创造力
        }
    )

    # 如果你好奇 response 到底包含了什么，可以取消下面这行的注释看看：
    # print(response)

    # 3. 解析模型输出
    # 模型输出的对象包含很多信息，我们通常最关心消息的内容
    content = response.message.content
    print(f"\n模型回复：\n{content}")
    
    # 4. 了解更多输出元数据
    # 你可以查看模型运行的统计信息，比如处理时间等
    print(f"\n--- 对话统计 ---")
    print(f"使用的模型: {response.model}")
    print(f"总耗时: {response.total_duration / 1e9:.2f} 秒")

if __name__ == "__main__":
    first_chat_demo()
