import os
import sys
import google.generativeai as genai
from colorama import Fore, Style, init

# 初始化颜色库
init(autoreset=True)

def get_api_key():
    """尝试从本地 api_key.txt 读取密钥"""
    key_file = "api_key.txt"
    if not os.path.exists(key_file):
        print(Fore.RED + "❌ 错误: 找不到 api_key.txt")
        print(Fore.YELLOW + "请在项目根目录新建 api_key.txt，并将 Google API Key 粘贴进去。")
        return None
    
    try:
        with open(key_file, "r", encoding='utf-8') as f:
            # 读取内容并去除首尾空格/换行
            return f.read().strip()
    except Exception as e:
        print(Fore.RED + f"❌ 读取 api_key.txt 失败: {e}")
        return None

def load_file(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def main():
    # --- 安全加载 API KEY ---
    api_key = get_api_key()
    if not api_key:
        input("按回车键退出...")
        return

    # 配置 Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    print(Fore.CYAN + "=========================================")
    print(Fore.CYAN + "      ADSCOPY 智能编导系统")
    print(Fore.CYAN + "=========================================")
    
    # 1. 读取 Agent 系统设定
    system_prompt = load_file("Agent.md")
    if system_prompt:
        print(Fore.GREEN + f"[系统] 已加载系统设定: Agent.md")
    else:
        print(Fore.YELLOW + "[提示] 未找到 Agent.md，将使用默认设定")

    # 2. 列出所有 Skill
    if not os.path.exists("skills"):
        os.makedirs("skills") # 如果没有文件夹自动创建一个
        
    skills = [f for f in os.listdir("skills") if f.endswith(".txt")]
    
    if not skills:
        print(Fore.RED + "\n[警告] skills 文件夹是空的！请放入技能文件 (.txt)")
        input("按回车键退出...")
        return

    print(Fore.YELLOW + "\n可用技能 (Skill):")
    for idx, skill in enumerate(skills):
        print(f"{idx + 1}. {skill}")

    # 3. 选择技能
    choice = input(Fore.WHITE + "\n请选择技能编号: ")
    try:
        selected_skill_file = skills[int(choice) - 1]
        skill_content = load_file(os.path.join("skills", selected_skill_file))
        print(Fore.GREEN + f"[状态] 已激活技能: {selected_skill_file}")
    except:
        print(Fore.RED + "选择错误，退出。")
        input("按回车键退出...")
        return

    # 4. 开始交互
    print(Fore.CYAN + "\n-----------------------------------------")
    print(f"当前模式: {selected_skill_file}")
    print("请输入你的原始内容 (输入 'exit' 退出):")
    
    chat = model.start_chat(history=[])
    
    # 构建完整指令
    full_instruction = f"{system_prompt}\n\n当前任务技能要求:\n{skill_content}\n\n请等待用户输入内容并按此执行。"
    
    try:
        # 先发一条指令给 AI 设定人设，但不显示输出，假装是在“热身”
        chat.send_message(full_instruction)
    except Exception as e:
        print(Fore.RED + f"连接 API 失败，请检查网络或 Key: {e}")
        input("按回车键退出...")
        return

    while True:
        user_input = input(Fore.WHITE + "\n[我]: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        if not user_input.strip():
            continue
        
        print(Fore.YELLOW + "ADSCOPY 思考中...")
        try:
            response = chat.send_message(user_input)
            print(Fore.CYAN + f"[ADSCOPY]: \n{response.text}")
        except Exception as e:
            print(Fore.RED + f"发生错误: {e}")

if __name__ == "__main__":
    main()