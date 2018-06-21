#include "stdlib.h"
#include "stdio.h"
#include "stdbool.h"

void custom_sort(char *b, int n) {
    
}

int main() {
    int ngames;

    scanf("%d", &ngames);

    // Run all games
    for (int g = 0; g < ngames; g++) {
        // Run one game here
        int n;
        char b[101]; // 1 <= n <= 100

        bool happy = true;

        scanf("%d", &n);
        scanf("%s", &b);

        b = custom_sort(b, n)

        // Finaly, prints
        printf("%s\n", happy ? "YES" : "NO");
    }
    return 0;
}
