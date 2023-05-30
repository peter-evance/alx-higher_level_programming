#include "lists.h"

/**
 * dlistint_len - Number of elements in a linked dlistint_t list
 * @h: Head of dlistint_t list
 * Return: Number of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t no_nodes = 0;

	while (h != NULL)
	{
		h = h->next;
		++no_nodes;
	}

	return (no_nodes);
}
