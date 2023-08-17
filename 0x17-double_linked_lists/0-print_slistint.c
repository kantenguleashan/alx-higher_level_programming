#include <stdio.h>
#include <stddef.h>  // For size_t definition

typedef struct dlistint_s {
    int n;
    struct dlistint_s *prev;
    struct dlistint_s *next;
} dlistint_t;

size_t print_dlistint(const dlistint_t *h) {
    size_t count = 0;

    while (h != NULL) {
        printf("%d\n", h->n);
        h = h->next;
        count++;
    }

    return count;
}

int main() {
    // Assuming you have a doubly linked list named 'head'
    dlistint_t *head = NULL;  // Initialize your list here

    // Call the function to print the elements
    size_t count = print_dlistint(head);
    printf("Total elements: %zu\n", count);

    return 0;
}
