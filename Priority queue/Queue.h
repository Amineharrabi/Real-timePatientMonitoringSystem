struct element {
	int key;
	struct element * next;
};
struct queue {
	struct element * last;
	struct element * first;
};
struct queue * createQueue ();
void addElement(struct queue * , int);
void removeElement(struct queue *);
unsigned empty(struct queue);
void printAllTheQueue( struct queue ** T );

