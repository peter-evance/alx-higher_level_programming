#include "lists.h"

/**
 * get_dnodeint_at_index - Finds a node in a dlistint_t list.
 * @head: Head of the dlistint_t list.
 * @index: Index of the node to find.
 *
 * Return: If the node does not exist - NULL.
 *         Otherwise - the address of the located node.
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	size_t count = 0;

	while (head != NULL && count < index)
	{
		head = head->next;
		count++;
	}

	if (count == index)
		return (head);
	else
		return (NULL);
}

