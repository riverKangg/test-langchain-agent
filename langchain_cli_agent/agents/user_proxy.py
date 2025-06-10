from autogen import UserProxyAgent

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",  # 또는 "TERMINAL"로 수동 승인
    max_consecutive_auto_reply=10,
)
