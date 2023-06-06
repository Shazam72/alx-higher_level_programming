#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: list head
 * @number: number to insert
 * Return: new node address else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *node = NULL;

	if (*head == NULL)
	{
		node = add_nodeint_end(head, number);
		return (node);
	}
	for (tmp = *head; tmp; tmp = tmp->next)
	{
		if (tmp->n >= number)
		{
			add_nodeint_end(&node, number);

			node->next = tmp;
			*head = node;
			break;
		}
		if (tmp->next == NULL ||
				(tmp->next && tmp->n <= number && tmp->next->n >= number))
		{
			node = (listint_t *)malloc(sizeof(*node));
			node->n = number;
			node->next = tmp->next;
			tmp->next = node;
			break;
		}
	}
	return (node);
}
