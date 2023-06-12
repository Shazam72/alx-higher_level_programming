#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: head
 * Return: 1 if the list is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = NULL, *rvesed = NULL, *tmp = NULL;

	if ((*head) == NULL)
		return (1);
	curr = (*head);
	tmp = (*head);
	rvesed = reverse(&tmp);
	while (rvesed != NULL && curr != NULL)
	{
		if (rvesed->n != curr->n)
			return (0);
		rvesed = rvesed->next;
		curr = curr->next;
	}
	return (1);
}

/**
 * reverse - reverse a singly linked list
 * @head: head
 * Return: ptr to head
 */
listint_t *reverse(listint_t **head)
{
	listint_t *curr, *next;

	while ((*head) != NULL)
	{
		next = (*head)->next;
		(*head)->next = curr;
		curr = (*head);
		(*head) = next;
	}
	(*head) = curr;
	return (*head);
}
