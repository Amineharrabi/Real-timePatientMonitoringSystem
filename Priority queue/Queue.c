#include <stdlib.h>
#include <assert.h>
#include "Queue.h"
#include <stdio.h>


struct  queue * createQueue() {
    struct queue* e ;
    e = (struct queue *)malloc(sizeof(struct queue));
    assert(e);
    e -> first = NULL;
    e -> last = NULL;
    return e;
}
unsigned empty(struct queue  q) {
    return q.first == NULL && q.last == NULL;
    }

void addElement(struct queue * q , int x) {
    struct element * s ;
    s = (struct element *)malloc(sizeof(struct element));
    assert(s != NULL);
    s-> key = x;
    s -> next = NULL;
    
    if (empty(*q)) {
        q->first=s;
            }
    else { q -> last -> next =s;
     } 
     q->last = s;

    }
void removeElement(struct queue * q) {
    assert(q) ;
    struct element * s ;
    s = q -> first;
    q -> first = q -> first ->next;
    free (s);

    if(q -> first == NULL) {
        q -> last = NULL;
    }
}
void printAllTheQueue( struct queue ** T ) {
    for (int i = 0; i < 5 ; i++) {
        struct element * temp;
        temp = T[i] -> first;
        printf("Queue %d: \n ", i + 1);
        while (temp != NULL) {
            printf("%d , " , temp->key);
            temp = temp->next;
        {
            printf("\n\n");
        }
        
    }

    }
}


