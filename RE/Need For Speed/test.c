// NeSE{4321Good job keeping bus #1f2ac4ec speeding along!}

#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

void header(int argc, const char** argv, const char** envp);
unsigned int set_timer();
int get_key();
void print_flag();
__int64 decrypt_flag(int a1);
__int64 calculate_key();

// char flag[64] = "nhsHZ9"; // 假设的 flag 值
char flag[0x36 + 2] = {0x6E, 0x68, 0x73, 0x48, 0x5A, 0x39, 0x11, 0x3F, 0x13, 0x4A, 0x4C, 0x62,
                       0x40, 0x2D, 0x4E, 0x62, 0x47, 0x2D, 0x4D, 0x68, 0x43, 0x7D, 0x4E, 0x63,
                       0x4F, 0x2D, 0x4A, 0x78, 0x5A, 0x2D, 0x09, 0x3C, 0x4C, 0x3F, 0x4A, 0x6E,
                       0x18, 0x68, 0x4F, 0x2D, 0x5E, 0x7D, 0x4B, 0x68, 0x4A, 0x64, 0x41, 0x6A,
                       0x10, 0x6C, 0x5C, 0x62, 0x5F, 0x6A, 0x13, 0x7D};
__int64 key;

int main(int argc, const char** argv, const char** envp) {
    header(argc, argv, envp);
    // set_timer();
    get_key();
    print_flag();
    return 0;
}

void header(int argc, const char** argv, const char** envp) {
    unsigned int i;

    puts("Keep this thing over 50 mph!");
    for (i = 0; i <= 0x1B; ++i)
        putchar(61); // 输出 '=' 字符
    puts("\n");
}

// unsigned int set_timer() {
//     if (signal(SIGALRM, alarm_handler) == SIG_ERR) {
//         puts("\n\nSomething bad happened here. ");
//         exit(0);
//     }
//     Sleep(1000); // 代替 alarm(1u)，在这里做延时
//     return 1;    // 这里返回1只是为了保持函数的结构
// }

int get_key() {
    puts("Creating key...");
    key = calculate_key();
    return puts("Finished");
}

void print_flag() {
    puts("Printing flag:");
    decrypt_flag((unsigned int)key);
    puts(flag);
}

__int64 decrypt_flag(int a1) {
    __int64 result;
    int v2[4];
    unsigned int i;

    v2[0] = a1;
    for (i = 0;; ++i) {
        result = i;
        if (i > 0x36)
            break;
        flag[i] ^= *((unsigned char*)v2 + (int)i % 2);
        if ((int)i % 3 == 2)
            ++v2[0];
    }
    return result;
}

__int64 calculate_key() {
    // int i;
    // for (i = -729802176; i != -364901088; --i)
    //     ; // 这里的循环没有实际作用
    return 3930066208LL;
}

void alarm_handler(int signum) {
    // 可以在这里处理 alarm 信号
    // 由于 Windows 不直接支持 alarm，可以为空
}

// NeSE{4321Good job keeping bus #1f2ac4ec speeding along!}