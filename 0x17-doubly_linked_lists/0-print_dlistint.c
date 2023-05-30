#include "lists.h"
/**
 * print_dlistint - Prints all the elements of dlistint_t list.
 * @h: Head of dlistint_t list.
 *
 * Return: The number of nodes in dlistint_t list.
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t no_nodes = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		++no_nodes;
	}

	return (no_nodes);
}
