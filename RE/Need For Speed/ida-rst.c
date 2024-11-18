int __cdecl main(int argc, const char** argv, const char** envp) {
    header(argc, argv, envp);
    set_timer(argc);
    get_key(argc);
    print_flag();
    return 0;
}

int header() {
    unsigned int i; // [rsp+Ch] [rbp-4h]

    puts("Keep this thing over 50 mph!");
    for (i = 0; i <= 0x1B; ++i)
        putchar(61);
    return puts("\n");
}

unsigned int set_timer() {
    if (__sysv_signal(14, alarm_handler) == (__sighandler_t)-1LL) {
        puts("\n\nSomething bad happened here. ");
        exit(0);
    }
    return alarm(1u);
}

int get_key() {
    puts("Creating key...");
    key = calculate_key();
    return puts("Finished");
}

int print_flag() {
    puts("Printing flag:");
    decrypt_flag((unsigned int)key);
    return puts(flag);
}

__int64 __fastcall decrypt_flag(int a1) {
    __int64 result; // rax
    int v2[4];      // [rsp+0h] [rbp-14h]
    unsigned int i; // [rsp+10h] [rbp-4h]

    v2[0] = a1;
    for (i = 0;; ++i) {
        result = i;
        if (i > 0x36)
            break;
        flag[i] ^= *((_BYTE*)v2 + (int)i % 2);
        if ((int)i % 3 == 2)
            ++v2[0];
    }
    return result;
}

__int64 calculate_key() {
    int i; // [rsp+0h] [rbp-4h]

    for (i = -729802176; i != -364901088; --i)
        ;
    return 3930066208LL;
}

/*
.data:0000000000201020                 public flag
.data:0000000000201020 ; char flag[6]
.data:0000000000201020 flag            db 'nhsHZ9'             ; DATA XREF: decrypt_flag+16↑o
.data:0000000000201020                                         ; decrypt_flag+43↑o ...
.data:0000000000201026                 db  11h
.data:0000000000201027                 db  3Fh ; ?
.data:0000000000201028                 db  13h
.data:0000000000201029                 db  4Ah ; J
.data:000000000020102A                 db  4Ch ; L
.data:000000000020102B                 db  62h ; b
.data:000000000020102C                 db  40h ; @
.data:000000000020102D                 db  2Dh ; -
.data:000000000020102E                 db  4Eh ; N
.data:000000000020102F                 db  62h ; b
.data:0000000000201030                 db  47h ; G
.data:0000000000201031                 db  2Dh ; -
.data:0000000000201032                 db  4Dh ; M
.data:0000000000201033                 db  68h ; h
.data:0000000000201034                 db  43h ; C
.data:0000000000201035                 db  7Dh ; }
.data:0000000000201036                 db  4Eh ; N
.data:0000000000201037                 db  63h ; c
.data:0000000000201038                 db  4Fh ; O
.data:0000000000201039                 db  2Dh ; -
.data:000000000020103A                 db  4Ah ; J
.data:000000000020103B                 db  78h ; x
.data:000000000020103C                 db  5Ah ; Z
.data:000000000020103D                 db  2Dh ; -
.data:000000000020103E                 db    9
.data:000000000020103F                 db  3Ch ; <
.data:0000000000201040                 db  4Ch ; L
.data:0000000000201041                 db  3Fh ; ?
.data:0000000000201042                 db  4Ah ; J
.data:0000000000201043                 db  6Eh ; n
.data:0000000000201044                 db  18h
.data:0000000000201045                 db  68h ; h
.data:0000000000201046                 db  4Fh ; O
.data:0000000000201047                 db  2Dh ; -
.data:0000000000201048                 db  5Eh ; ^
.data:0000000000201049                 db  7Dh ; }
.data:000000000020104A                 db  4Bh ; K
.data:000000000020104B                 db  68h ; h
.data:000000000020104C                 db  4Ah ; J
.data:000000000020104D                 db  64h ; d
.data:000000000020104E                 db  41h ; A
.data:000000000020104F                 db  6Ah ; j
.data:0000000000201050                 db  10h
.data:0000000000201051                 db  6Ch ; l
.data:0000000000201052                 db  5Ch ; \
.data:0000000000201053                 db  62h ; b
.data:0000000000201054                 db  5Fh ; _
.data:0000000000201055                 db  6Ah ; j
.data:0000000000201056                 db  13h
.data:0000000000201057                 db  7Dh ; }
.data:0000000000201057 _data           ends
.data:0000000000201057
.bss:0000000000201058 ; ===========================================================================
*/