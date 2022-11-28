#include "lists.h"
/**
 * check_cycle - checks if a singly linked list is a cycle
 * @list - pointer to the head of the list
 * Return: 0 if there's no cycle and 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (!list)
		return (0);

	s = list;
	f = list->next;
	while (f && s && f->next)
	{
		if (s == f)
		{
			return (1);
		}
		s = s->next;
		f = f->next->next;
	}
	return (0);
}
