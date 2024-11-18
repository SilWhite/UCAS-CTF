int __cdecl main(int argc, const char** argv, const char** envp) {
    _DWORD* v4; // [esp+8h] [ebp-Ch]

    v4 = mmap(0, 4u, 3, 33, -1, 0);
    *v4 = 1000000000;
    fork();
    fork();
    fork();
    fork();
    *v4 += 1234567890;
    doNothing(*v4);
    return 0;
}