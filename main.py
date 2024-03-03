import pyotp

# 从输入框获取密钥列表
def get_secret_keys():
    keys = []
    while True:
        key = input("请输入密钥（输入 ' ' 完成输入）: ")
        if key.lower() == 'done':
            break
        keys.append(key)
    return keys

# 生成验证码
def generate_2fa_codes(secret_keys):
    totp_list = [pyotp.TOTP(key) for key in secret_keys]
    for index, totp in enumerate(totp_list):
        current_otp = totp.now()
        print(f" {index + 1}: {current_otp}")

# 主函数
def main():
    secret_keys = get_secret_keys()
    generate_2fa_codes(secret_keys)

if __name__ == "__main__":
    main()
