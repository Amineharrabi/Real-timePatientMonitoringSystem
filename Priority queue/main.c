#include <stdlib.h>
#include <assert.h>
#include "Queue.h"
#include <stdio.h>
#include <string.h>

void main() {
    FILE *file = fopen("results.csv", "r");
    if (file == NULL) {
        printf("Error: Could not open results.csv\n");
        return;
    }

    struct queue **T = malloc(sizeof(struct queue *) * 5);
    for (int i = 0; i < 5; i++) {
        T[i] = createQueue();
        if (T[i] == NULL) {
            printf("Memory allocation failed\n");
            EXIT_FAILURE;
        }
    }

    char line[256];
    fgets(line, sizeof(line), file); // Skip header
    while (fgets(line, sizeof(line), file)) {
        int patientID, riskLevel;
        sscanf(line, "%d,%d", &patientID, &riskLevel);
        addElement(T[riskLevel], patientID);
    }
    fclose(file);

    printf("Patients sorted into priority queues:\n");
    printAllTheQueue(T);

    // Cleanup
    for (int i = 0; i < 5; i++) {
        while (!empty(*T[i])) {
            removeElement(T[i]);
        }
        free(T[i]);
    }
    free(T);
}