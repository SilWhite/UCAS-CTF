judge_str = "jU5t_a_sna_3lpm18g947_u_4_m9r54f"
# 密码验证
# public boolean checkPassword(String password) {
#     if (password.length() != 32) {
#         return false;
#     }
#     char[] buffer = new char[32];
#     int i;
#     for (i = 0; i < 8; i++) {
#         buffer[i] = password.charAt(i);
#     }
#     for (; i < 16; i++) {
#         buffer[i] = password.charAt(23 - i);
#     }
#     for (; i < 32; i += 2) {
#         buffer[i] = password.charAt(46 - i);
#     }
#     for (i = 31; i >= 17; i -= 2) {
#         buffer[i] = password.charAt(i);
#     }
#     String s = new String(buffer);
#     return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
# }
pwd = [""] * 32

for i in range(8):
    pwd[i] = judge_str[i]
for i in range(8, 16):
    pwd[23 - i] = judge_str[i]
for i in range(16, 32, 2):
    pwd[46 - i] = judge_str[i]
for i in range(31, 16, -2):
    pwd[i] = judge_str[i]

print("".join(pwd))
