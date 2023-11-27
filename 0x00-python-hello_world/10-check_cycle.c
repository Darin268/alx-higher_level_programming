#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - to checks if a singly linked list has a cycle in it
 * @list: is the list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;

	if (list == NULL)
	{
		return (0);
	}

	while (f && s && f->next)
	{
		s = s->next;
		f = f->next->next;

		if (s == f)
			return (1);
	}
	return (0);
}
