#include "lists.h"

/**
 * check_cycle - check cycle existence in singly linked list
 * @list: list to check
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp2 = list;
	listint_t *tmp1 = list;

	while (tmp1 && tmp2 && tmp2->next)
	{
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;
		if (tmp1 == tmp2)
			return (1);
	}
	return (0);
}
