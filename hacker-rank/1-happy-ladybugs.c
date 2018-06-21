#include "stdlib.h"
#include "stdio.h"
#include "stdbool.h"

int main() {
    int ngames;

    scanf("%d", &ngames);

    // Run all games
    for (int g = 0; g < ngames; g++) {
        // Run one game here
        int n;
        char b[102]; // 1 <= n <= 100

        int letters['Z' - 'A' + 1] = {0};
        int underscores = 0;
        bool happy = true;

        scanf("%d", &n);
        scanf("%s", &b);

        // count letters and underscores in b
        for (int i = 0; i < n; i++) {
            if (b[i] == '_') {
                underscores++;
            } else {
                letters[b[i] - 'A']++;
            }
        }

        // check if exists one letter alone
        for (int i = 0; i < 'Z' - 'A' + 1; i++) {
            happy &= (letters[i] != 1);
        }

        if (happy) {
            // all letters maybe have company
            if (underscores == 0) {
                // no chance of reorder
                // we need check if already are in order
                char last = b[0];
                int count = 0;
                for (int i = 1; i < n; i++) {
                    if (b[i] == last) {
                        count++;
                    } else if (count > 0) {
                        count = 0;
                        last = b[i];
                    } else {
                        happy = false;
                    }
                }
            }
        }

        // Finaly, prints
        //char result[5];
        //scanf("%s", &result);
        //printf("%s - %s\n", happy ? "YES" : "NO", result);
        printf("%s\n", happy ? "YES" : "NO");
    }
    return 0;
}
