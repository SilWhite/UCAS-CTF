#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

#define BUFSIZE 176
#define FLAGSIZE 64

void flag(unsigned int arg1, unsigned int arg2) {
    char buf[FLAGSIZE];
    FILE* f = fopen("flag.txt", "r");
    if (f == NULL) {
        printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
        exit(0);
    }

    fgets(buf, FLAGSIZE, f);
    if (arg1 != 0xDEADBEEF)
        return;
    if (arg2 != 0xC0DED00D)
        return;
    printf(buf);
}

void vuln() {
    char buf[BUFSIZE];
    gets(buf);
    puts(buf);
}

int main(int argc, char** argv) {

    setvbuf(stdout, NULL, _IONBF, 0);

    gid_t gid = getegid();
    setresgid(gid, gid, gid);

    puts("Please enter your string: ");
    vuln();
    return 0;
}
